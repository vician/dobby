from tts.tts import Tts

from espeak import espeak

class Espeak(Tts):

    def say(self,message):
        espeak.synth(message)
