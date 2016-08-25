"""
Created on 21 Aug 2014
@author: rlat
"""

import cleverbot

class Cleverbot(object):
    """
    A class for talking to cleverbot.
    :see: https://pypi.python.org/pypi/cleverbot
    """

    def __init__(self):
        """
        Constructor
        """
        self.__bot = cleverbot.Cleverbot()

    def ask(self, message):
        """
        Ask the bot a message.
        :param message: A message to ask.
        :return: Bot's response.
        """
        return self.__bot.ask(message)