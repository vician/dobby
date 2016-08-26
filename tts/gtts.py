from tts.tts import Tts

from gtts import gTTS
import subprocess
import tempfile

class Gtts(Tts):

    def say(self,message):
        audio_file = tempfile.mktemp()
        tts = gTTS(text=message, lang="en")
        tts.save(audio_file)
        return_code = subprocess.call(["mplayer", "-really-quiet", audio_file])
