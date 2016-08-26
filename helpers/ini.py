import configparser

class Ini():
    
    attributes = []
    
    def __init__(self,attributes):
        self.attributes = attributes

    def set(self,name,value):

        if name in self.attributes:
            setattr(self,name,value)
        else:
            print("ERROR: "+name+" is not valid attribute!")
            print("Valid is: "+', '.join(self.attributes))

    def get(self,name):
        if hasattr(self,name):
            return getattr(self,name)
        else:
            return ""

    def save(self,config,section_name):
        config.add_section(section_name)
        
        for attribute in self.attributes:
            if hasattr(self,attribute):
                print("saving ["+section_name+"] "+attribute+":"+getattr(self,attribute))
                config.set(section_name,attribute,getattr(self,attribute))
        
