#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# TALKER - epos wrapper
# initialize epos, reads message
#
# Licence: MIT
# Author: Jan Lipovský <janlipovsky@gmail.com>

import subprocess
import threading
import time
import urllib
import logging
import re

class Talker(object):
    epos_daemon = "eposd"
    mplayer = "mplayer"
    voice = "violka"
    messages = []
    speakThread = None
    useGoogleT = False
    googleLang = "cs"
    logger = None

    def initLogging(self):
        """Initialize logger"""
        self.logger = logging.getLogger('TALKER')
        self.logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s: %(levelname)s - %(message)s')

        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def __init__(self):
        self.messages = []
        self.initLogging()
        if (self.isEposInstalled()):
            if(not self.isMplayerInstalled()):
                self.logger.error('mplayer is NOT installed on the system')
                raise Exception('mplayer is NOT installed on the system')

            self.useGoogleT = False
            if (self.isEposRunning() == True):
                self.logger.info('Epos is already running')
            else:
                self.logger.info('Epos is not running')
                self.logger.info('Starting epos...')
                self.runEpos()
        else:
            if(self.isMplayerInstalled()):
                self.useGoogleT = True
            else:
                self.logger.error('Epos and mplayer are NOT installed on the system')
                raise Exception('Epos and mplayer are NOT installed on the system')

    def splitSentences(self, text):
        """
        Splits text into sentences
        :param text: text to split
        :return:
        """
        sentenceEnders = re.compile('[.!?]')
        sentenceList = sentenceEnders.split(text)
        return sentenceList

    def sayThread(self):
        while (len(self.messages) > 0):
            text = self.messages.pop(0)
            if(self.useGoogleT == True):
                url = "http://translate.google.cz/translate_tts?ie=UTF-8&tl=" + self.googleLang + "&textlen=" + str(
                    len(text)) + "&client=t&q=" + urllib.quote(text.encode('utf-8'))+"&ttsspeed=1.0"
                #https://translate.google.cz/translate_tts?ie=UTF-8&q=ahoj&tl=cs&total=1&idx=0&textlen=4&tk=303904&client=t&prev=input
                #https://translate.google.cz/translate_tts?ie=UTF-8&q=ahoj%20zkus%20me%20precist&tl=cs&total=1&idx=0&textlen=20&tk=619507&client=t&prev=input&ttsspeed=0.24
                #https://translate.google.cz/translate_tts?ie=UTF-8&q=ahoj&tl=cs&total=1&idx=0&textlen=4&tk=303904&client=t&prev=input&ttsspeed=0.24
                subprocess.call(["mplayer", url])
            else:
                print("SAY:", text)
                subprocess.call(["./say_it.sh", text])

    def useGoogle(self):
        self.useGoogleT = True

    def useEpos(self):
        self.useGoogleT = False

    def setGoogleLanguage(self, lang):
        self.googleLang = lang

    def addMessage(self, text):
        if len(text) > 95:
            splited = self.splitSentences(text)
            for s in splited:
                if len(s) <= 95:
                    self.messages.append(s)
                else:
                    tmp = s
                    while len(tmp) > 95:
                        pos = tmp.rfind(' ', 0, 95)
                        if pos == -1:
                            pos = 95
                        substr = tmp[0:pos]
                        tmp = tmp[pos+1:]
                        self.messages.append(substr)
                    self.messages.append(tmp)

        else:
            self.messages.append(text)


    def addAndSayMessage(self, text):
        self.addMessage(text)
        self.sayIt()


    def sayIt(self):
        if (threading.active_count() <= 1):
            self.speakThread = threading.Thread(target=self.sayThread)
            self.speakThread.start()


    def isEposRunning(self):
        """Checks if eposd is running"""
        s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
        for x in s.stdout:
            if (x.decode("utf-8").find(self.epos_daemon) >= 0):
                return True
        return False


    def isEposInstalled(self):
        """Checks if epos is installed on the system"""
        try:
            subprocess.check_output(["which", self.epos_daemon], universal_newlines=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def isMplayerInstalled(self):
        """Checks if mplayer is installed on the system"""
        try:
            subprocess.check_output(["which", self.mplayer], universal_newlines=True)
            return True
        except subprocess.CalledProcessError:
            return False


    def runEpos(self):
        setVoice = '--voice '+self.voice;
        subprocess.call("eposd "+setVoice,shell=True)

        if(self.isEposRunning()):
            self.logger.info("Epos was started with voice "+self.voice)
        else:
            self.logger.error('Epos was NOT started')

    def restartEpos(self):
        self.killEpos()
        time.sleep(1)
        if(self.isEposRunning()):
            self.killEpos()

        self.runEpos()


    def switchToMale(self):
        if (self.voice == "violka"):
            self.voice = "machac"
            self.restartEpos()


    def switchToFemale(self):
        if (self.voice == "machac"):
            self.voice = "violka"
            self.restartEpos()

    def killEpos(self):
        subprocess.Popen(["killall", self.epos_daemon],stdout=subprocess.PIPE)


if __name__ == "__main__":
    print("Talker class")
    talker = Talker()
    talker.useGoogle()
    talker.setGoogleLanguage("cs")
    talker.addAndSayMessage("Ahoj světe!".decode('UTF-8'))

