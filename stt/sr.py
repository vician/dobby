# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr

from stt.stt import Stt

class SpeechRecognition(Stt):

    r = None

    def stt_init(self):
        self.r = sr.Recognizer()
        self.attributes.append("wit")

    def stt_listen(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        WIT_AI_KEY = self.ini.get("wit") # Wit.ai keys are 32-character uppercase alphanumeric strings
        try:
            said = self.r.recognize_wit(audio, key=WIT_AI_KEY)
            print("Wit.ai: " + said)
            return said
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))


### TESTS ###

#import sphinxbase
#import pocketsphinx

#r = sr.Recognizer()
#with sr.Microphone() as source:                # use the default microphone as the audio source
#    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
#
## recognize speech using Sphinx
#try:
#    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#except sr.UnknownValueError:
#    print("Sphinx could not understand audio")
#except sr.RequestError as e:
#    print("Sphinx error; {0}".format(e))
#

# recognize speech using Wit.ai
