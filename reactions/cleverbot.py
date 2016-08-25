import cleverbot
from reactions.reaction import Reaction

class Cleverbot(Reaction):

    help = "Answers from cleverbot"

    def __init__(self):
        self.__bot = cleverbot.Cleverbot()

    def do(self,message):
        return self.__bot.ask(message)
