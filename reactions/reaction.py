from helpers.ini import Ini

class Reaction():
    ''' Base class for all reactions. '''

    help = ""
    aliasses = []
    attributes = []

    ini = None

    def __init__(self):
        self.ini = Ini(self.attributes)
        self.init()

    def init(self):
        pass

    def get_help(self,command=None):
        reply = "Help for "+self.get_name()
        reply += "\n- aliasses: "+self.print_aliasses()
        reply += "\n- attributes: "+self.print_attributes()
        return reply+"\n"+self.help

    def print_aliasses(self):
        return ', '.join(self.get_aliasses())

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

    def print_attributes(self):
        return ', '.join(self.attributes)
