from reactions.reaction import Reaction

class Read(Reaction):

    help = "Read my message."
    aliasses = [ "read" ]

    def do(self,message):
        return message # Change to your behaviour
