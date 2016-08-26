from tts.tts import Tts

from gtts import gTTS
import tempfile
import os

from helpers.mplayer import Mplayer

class Gtts(Tts):

    def init(self):
        self.mplayer = Mplayer()
        self.ini.set("lang","en")

    def say(self,message):
        if message != None and len(message) > 0:
            audio_file = tempfile.mktemp()
            tts = gTTS(text=message, lang=self.ini.get("lang"))
            tts.save(audio_file)
            self.mplayer.play(audio_file)

    def do(self,message=None):
        if message == "stop" or message == "quiet":
            self.mplayer.stop()
        return ""
