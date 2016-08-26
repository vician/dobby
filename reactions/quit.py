import sys
from reactions.reaction import Reaction

class Quit(Reaction):

    help = "Will quit this program"
    aliasses = [ "quit", "bye", "exit" ]

    def do(self,message):
        sys.exit(0)
