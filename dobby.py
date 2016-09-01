#!/usr/bin/env python3

import sys
import configparser

# TTS
from tts.gtts import Gtts

# Stt

from stt.sr import SpeechRecognition

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
from reactions.wunderground import Wunderground
from reactions.time import Time

class Dobby():

    tts = None
    stt = None
    
    list_reactions = []
    list_aliasses = []
    reactions = []

    count_reactions = 0

    config_ini = None

    def __init__(self):
        # TTS
        self.tts = Gtts()
        # STT
        self.stt = SpeechRecognition()
        #self.stt = None
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
        self.load_reaction(Wunderground())
        self.load_reaction(Time())

        self.config_ini = configparser.ConfigParser()

        self.load_ini()

    def load_ini(self):
        self.config_ini.read("dobby.ini")

        for section in self.config_ini.sections():
            for variable in self.config_ini[section]:
                getattr(self,section).ini_set(variable,self.config_ini[section][variable])

    def save_ini(self):
        new_config_ini = configparser.ConfigParser()

        self.tts.save_ini(new_config_ini)

        for reaction in self.list_reactions:
            getattr(self,reaction).save_ini(new_config_ini)


        configfile = open('dobby.ini', 'w')
        new_config_ini.write(configfile)

    def load_reaction(self,reaction_object):
        name = "reaction"+str(self.count_reactions)
        setattr(self,name,reaction_object)
        self.count_reactions += 1
        real_name = getattr(self,name).get_name()
        self.list_reactions.append(real_name)
        for alias in getattr(self,name).get_aliasses():
            setattr(self,alias,getattr(self,name))

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
            #self.stt.ini_set("disabled","0")
            #userinput = self.stt.listen()
            #self.stt.ini_set("disabled","1")
            # Get first word
            first = userinput.partition(' ')[0]
            if first != userinput:
                rest = userinput.split(' ', 1)[1]
            else:
                rest = ""
            # Parse commands
            if first == '' or first == 'help':
                self.help(userinput)
            elif first == 'save':
                self.save_ini()
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
