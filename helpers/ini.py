import configparser

class Ini():
    
    attributes = []
    
    def __init__(self):
        pass

    def set(self,name,value):
        setattr(self,name,value)
        self.attributes.append(name)

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
        
