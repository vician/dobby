from tts.tts import Tts

from gtts import gTTS
import subprocess
import tempfile
import os

from helpers.mplayer import Mplayer

class Gtts(Tts):

    mplayer = None

    def __init__(self):
        self.mplayer = Mplayer()

    def say(self,message):
        audio_file = tempfile.mktemp()
        tts = gTTS(text=message, lang="en")
        tts.save(audio_file)
        #return_code = subprocess.call(["mplayer", "-really-quiet", audio_file])
        self.mplayer.play(audio_file)
        os.remove(audio_file)
