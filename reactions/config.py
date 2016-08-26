from reactions.reaction import Reaction

class Config(Reaction): # Change name of this class!

    help = "Config other reactions!"
    aliasses = [ "config" ]

    def get_reaction(self,message):
        first = message.partition(' ')[0]
        return first

    def set(self,message,target_reaction):
        values = message.split(' ')
        if len(values) == 2:
            return target_reaction.ini.get(values[1])

        if len(values) < 3:
            return "Wrong usage! See help!"

        reaction = values[0]
        name = values[1]
        value = values[2]
        target_reaction.ini.set(name,value)
        return "Configured for "+reaction+": "+name+"="+value
