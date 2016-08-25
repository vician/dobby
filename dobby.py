#!/usr/bin/env python3

import sys

# Import reactions
from reactions.quit import Quit
from reactions.todaydate import Todaydate
from reactions.cleverbot import Cleverbot
from reactions.alojz import Alojz

class Dobby():

    talker = None
    
    list_reactions = []

    def __init__(self):
        self.load_reaction("quit",Quit())
        self.load_reaction("cleverbot",Cleverbot())
        self.load_reaction("todaydate",Todaydate())
        self.load_reaction("alojz",Alojz())

    def load_reaction(self,name,reaction_object):
        setattr(self,name,reaction_object)
        self.list_reactions.append(name)
        for alias in getattr(self,name).get_aliasses():
            self.alias(alias, getattr(self,name))

    def alias(self,alias,alias_reaction):
        self.list_reactions.append(alias)
        setattr(self,alias,alias_reaction)

    def say(self,message):
        if self.talker != None:
            talker.say(message)
        print(message)

    def help(self,message):
        split = message.split()
        if len(split) == 1:
            self.say("Availible commands are: "+', '.join(self.list_reactions))
            self.say("Print help for command as: $ help command")
        else:
            command = split[1]
            if len(split) >= 3:
                argument = split[2]
            else:
                argument = ""
            if hasattr(self,command):
                self.say(getattr(self,command).get_help(argument))
            else:
                self.say("Help for "+command+" not found!")

    def listen(self):
        
        while True:
            print ("$ ", end="", flush=True)
            # Load user input
            userinput = sys.stdin.readline().rstrip('\n')
            # Get first word
            first = userinput.partition(' ')[0]
            # Parse commands
            if first == '' or first == 'help':
                self.help(userinput)
            else:
                # If reaction loaded
                if hasattr(self,first):
                    self.say(getattr(self,first).do(userinput))
                else:
                    # Cleverbot is default
                    self.say(self.cleverbot.do(userinput))


dobby = Dobby()
dobby.listen()
