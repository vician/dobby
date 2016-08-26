from datetime import datetime
from reactions.reaction import Reaction

class Time(Reaction):

    help = "Show current time"
    aliasses = [ "time", "now" ]

    def do(self,message):
        return "Now is "+datetime.now().strftime('%H:%M')
