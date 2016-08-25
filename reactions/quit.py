import sys
from reactions.reaction import Reaction

class Quit(Reaction):

    help = "Will quit this program"
    aliasses = [ "bye", "exit" ]

    def do(self,message):
        sys.exit(0)
