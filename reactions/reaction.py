class Reaction():
    ''' Base class for all reactions. '''

    help = ""
    aliasses = []

    def __init__(self):
        pass

    def get_help(self,command=None):
        return self.help

    def get_aliasses(self):
        return self.aliasses

    def do(self,message):
        return "Not implemented!"
