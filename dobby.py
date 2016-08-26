#!/usr/bin/env python3

import sys

# TTS
from tts.gtts import Gtts

# Import reactions
from reactions.quit import Quit
from reactions.config import Config
from reactions.todaydate import Todaydate
from reactions.cleverbot import Cleverbot
from reactions.alojz import Alojz
from reactions.ip import Ip
from reactions.eat import Eat
from reactions.youtube import Youtube
from reactions.read import Read

class Dobby():

    tts = None
    
    list_reactions = []
    reactions = []

    count_reactions = 0

    def __init__(self):
        # TTS
        self.tts = None
        # Reactions
        self.load_reaction(Quit())
        self.load_reaction(Config())
        self.load_reaction(Cleverbot())
        self.load_reaction(Todaydate())
        self.load_reaction(Alojz())
        self.load_reaction(Ip())
        self.load_reaction(Eat())
        self.load_reaction(Youtube())
        self.load_reaction(Read())

    def load_reaction(self,reaction_object):
        name = "reaction"+str(self.count_reactions)
        setattr(self,name,reaction_object)
        self.count_reactions += 1
        self.list_reactions.append(name)
        for alias in getattr(self,name).get_aliasses():
            self.alias(alias, getattr(self,name))

    def alias(self,alias,alias_reaction):
        self.list_reactions.append(alias)
        setattr(self,alias,alias_reaction)

    def say(self,message):
        if self.tts != None:
            self.tts.say(message)
        print(message)

    def help(self,message):
        split = message.split()
        if message == "" or len(split) == 1:
            self.say("Availible commands are: "+', '.join(self.list_reactions)+"\nPrint help for command as: $ help command")
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
            if first != userinput:
                rest = userinput.split(' ', 1)[1]
            else:
                rest = ""
            # Parse commands
            if first == '' or first == 'help':
                self.help(userinput)
            elif first == 'config':
                name_reaction = self.config.get_reaction(rest)
                if hasattr(self,name_reaction):
                    self.say(self.config.set(rest,getattr(self,name_reaction)))
            else:
                # If reaction loaded
                if hasattr(self,first):
                    self.say(getattr(self,first).do(rest))
                else:
                    # Cleverbot is default
                    self.say(self.cleverbot.do(userinput))


dobby = Dobby()
dobby.listen()
