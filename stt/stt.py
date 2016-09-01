from reactions.reaction import Reaction

class Stt(Reaction):
    ''' Base class for STT. '''

    aliasses = [ "stt" ]
    attributes = [ "disabled", "language", "called" ]

    def init(self):
        self.ini.set("disabled","0")
        self.ini.set("language","English")
        self.stt_init()

    def stt_init(self):
        pass

    def listen(self):
        if self.ini.get("disabled") != "1":
            message = self.stt_listen()
            first = message.partition(' ')[0]
            if message == self.ini.get("called"):
                return message.split(' ', 1)[1]
        return ""

    def stt_listen(self):
        pass

    def stop(self):
        pass

    def do(self,message=None):
        return self.stt_listen()
