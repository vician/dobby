from datetime import datetime
from reactions.reaction import Reaction

class Todaydate(Reaction):

    help = "Show today's date"
    aliasses = [ "today", "date" ]

    def do(self,message):
        return "Today is "+datetime.now().strftime('%Y-%m-%d')
