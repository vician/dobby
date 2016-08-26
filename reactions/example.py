from reactions.reaction import Reaction
# Import what you need

class Example(Reaction): # Change name of this class!

    help = "Here write information about this module!"
    aliasses = [ "sample" ] # Additionaly choose alias, or remove this variable

    def init(self):
        # Your init function. Do not use __init__!!!
        pass

    def do(self,message):
        return "Whatevere you want!" # Change to your behaviour
