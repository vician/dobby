#!/usr/bin/python
# -*- coding: utf-8 -*-
# Youtoobe player

import subprocess
import threading
import pafy
import time
import urllib
import logging

class Ytplayer(object):
    mplayer = "mplayer"
    logger = None
    yturl = ''
    playThread = None

    def initLogging(self):
        """Initialize logger"""
        self.logger = logging.getLogger('YOUTUBE')
        self.logger.setLevel(logging.DEBUG)
    
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s: %(levelname)s - %(message)s')
        
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def __init__(self):
        self.initLogging()

    def ytThread(self):
        if len(self.yturl) > 0:
            #subprocess.call(["mplayer", self.yturl])
            args = ["mplayer", self.yturl]
            subprocess.Popen(args)

    def play_youtube(self, url):
        if len(url) > 0:
            v = pafy.new(url)
            bestaudio = v.getbestaudio()
            self.yturl = bestaudio.url
            if threading.active_count() <= 1:
                self.playThread = threading.Thread(target=self.ytThread)
                self.playThread.start()
                return "playing: {}".format(v.title)
            else:
                return "ERROR: threading.active_count() == {}".format(threading.active_count())

    def stop_youtube(self):
        if self.playThread is not None:
            subprocess.call(["killall", self.mplayer])
            self.playThread.join()
            self.playThread = None
            return "YouTube player was stopped"
        else:
            return "YouTube player was not running. Nothing to stop."


if __name__ == "__main__":
    print("yt class")
    yt = Ytplayer()
    print(yt.play_youtube("https://www.youtube.com/watch?v=Ug88HO2mg44"))
    time.sleep(10)
    yt.stop_youtube()
