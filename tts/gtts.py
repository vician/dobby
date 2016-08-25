from tts.tts import Tts

from gtts import gTTS
import subprocess

class Gtts(Tts):

    def say(self,message):
        audio_file = "hello.mp3"
        tts = gTTS(text=message, lang="en")
        tts.save(audio_file)
        return_code = subprocess.call(["mplayer", audio_file])
