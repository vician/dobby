from tts.tts import Tts

from gtts import gTTS
import tempfile
import os

from helpers.mplayer import Mplayer
from helpers.language import Language

class Gtts(Tts):

    def tts_init(self):
        self.mplayer = Mplayer()
        self.language = Language()

    def tts_say(self,message):
        audio_file = tempfile.mktemp()
        tts = gTTS(text=message, lang=self.language.to_short(self.ini.get("language")))
        tts.save(audio_file)
        self.mplayer.play(audio_file,self.ini.get("thread"))

    def stop(self):
        self.mplayer.stop()

