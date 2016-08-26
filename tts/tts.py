from reactions.reaction import Reaction

class Tts(Reaction):
    ''' Base class for TTS. '''

    aliasses = [ "tts" ]
    attributes = [ "disabled", "language" ]

    def init(self):
        self.ini.set("disabled","0")
        self.ini.set("language","English")
        self.tts_init()

    def tts_init(self):
        pass

    def say(self,message):
        if self.ini.get("disabled") != "1":
            if isinstance(message, str) and len(message) > 0:
                self.tts_say(message)

    def tts_say(message):
        pass

    def stop(self):
        pass

    def do(self,message=None):
        if message == "stop" or message == "quiet":
            self.stop()
        return ""
