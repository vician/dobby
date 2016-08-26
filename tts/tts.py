from reactions.reaction import Reaction

class Tts(Reaction):
    ''' Base class for TTS. '''

    aliasses = [ "tts" ]

    def say(self,message):
        pass
