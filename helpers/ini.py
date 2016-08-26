

class Ini():

    name = ""

    def __init__(self):
        pass

    def set(self,name,value):
        setattr(self,name,value)

    def get(self,name):
        return getattr(self,name)
