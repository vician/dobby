from reactions.reaction import Reaction

class Read(Reaction):

    help = "Read my message."


    def do(self,message):
        return message # Change to your behaviour
