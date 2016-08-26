from tts.tts import Tts

from gtts import gTTS
import tempfile
import os

from helpers.mplayer import Mplayer

class Gtts(Tts):

    attributes = [ "lang", "disabled" ]

    def init(self):
        self.mplayer = Mplayer()
        self.ini.set("lang","en")
        self.ini.set("disabled","0")

    def say(self,message):
        if self.ini.get("disabled") != "1":
            if message is str and len(message) > 0:
                audio_file = tempfile.mktemp()
                tts = gTTS(text=message, lang=self.ini.get("lang"))
                tts.save(audio_file)
                self.mplayer.play(audio_file)

    def do(self,message=None):
        if message == "stop" or message == "quiet":
            self.mplayer.stop()
        return ""
