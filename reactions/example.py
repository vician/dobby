from reactions.reaction import Reaction
# Import what you need

class Example(Reaction): # Change name of this class!

    help = "Here write information about this module!"
    aliasses = [ "example" ]
    attributes = [] # Specify your attributes

    def init(self):
        # Your init function. Do not use __init__!!!a
        self.ini.set("foo","bar") # Init your attributes
        pass

    def do(self,message):
        something = self.ini.get("foor") # Use your attribute
        return "Whatevere you want!" # Change to your behaviour
