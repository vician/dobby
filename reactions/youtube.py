from reactions.reaction import Reaction

import pafy
import youtube_dl

from helpers.mplayer import Mplayer

class Youtube(Reaction):

    help = "Simple playing audio from youtube."
    aliasses = [ "youtube" "yt" ]

    mplayer = None

    def init(self):
        self.mplayer = Mplayer()

    def do(self,message):
        if message == "stop":
            self.stop_youtube
        self.stop_youtube()
        self.play_youtube(message)
        pass

    def play_youtube(self,url):
        if len(url) > 0:
            v = pafy.new(url)
            bestaudio = v.getbestaudio()
            self.yturl = bestaudio.url
            self.mplayer.play(bestaudio.url)

    def stop_youtube(self):
        self.mplayer.stop()
