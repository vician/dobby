from reactions.reaction import Reaction

import subprocess
import threading
import pafy
import os

from helpers.mplayer import Mplayer

class Youtube(Reaction):

    help = "Simple playing audio from youtube."
    aliasses = [ "yt" ]

    mplayer = None
    yturl = ""
    playThread = None

    def __init__(self):
        self.mplayer = Mplayer()

    def do(self,message):
        if message == "stop":
            self.stop_youtube
        self.stop_youtube()
        self.play_youtube(message)
        pass

    #def ytThread(self):
    #    if len(self.yturl) > 0:
    #        #subprocess.call(["mplayer", self.yturl])
    #        args = ["mplayer", self.yturl]
    #        subprocess.Popen(args)


    def play_youtube(self,url):
        if len(url) > 0:
            v = pafy.new(url)
            bestaudio = v.getbestaudio()
            self.yturl = bestaudio.url
            self.mplayer.play(bestaudio.url)
            #if threading.active_count() <= 1:
            #    self.playThread = threading.Thread(target=self.ytThread)
            #    self.playThread.start()
            #    return "playing: {}".format(v.title)
            #else:
            #    return "ERROR: threading.active_count() == {}".format(threading.active_count())

    def stop_youtube(self):
        self.mplayer.stop()
        #if self.playThread is not None:
        #    subprocess.call(["killall", self.mplayer])
        #    self.playThread.join()
        #    self.playThread = None
        #    return "YouTube player was stopped"
        #else:
        #    return "YouTube player was not running. Nothing to stop."

