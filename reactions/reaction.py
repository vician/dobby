from helpers.ini import Ini

class Reaction():
    ''' Base class for all reactions. '''

    help = ""
    aliasses = []

    ini = None

    def __init__(self):
        self.ini = Ini()
        self.init()

    def init(self):
        pass

    def get_help(self,command=None):
        return self.help

    def get_aliasses(self):
        return self.aliasses

    def do(self,message):
        return "Not implemented!"

    def ini_set(self,name,value):
        self.ini.set(name,value)

    def get_name(self):
        return self.aliasses[0]

    def save_ini(self,config):
        self.ini.save(config,self.get_name())
