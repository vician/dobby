from reactions.reaction import Reaction

import random
import datetime

class Eat(Reaction):

    help = "When I should eat?"
    aliasses = [ "lunch" ]

    def do(self,message):
        tmp = random.randint(0, 11) 

        if(tmp <= 7): 
            cas = self.getLunchTimeNow(59)
            if(cas == False):
                reply = 'ERROR: getLunchTimeFromNow'
            else:
                reply = "OK, takze jidlo bude presne v "+cas

        if(tmp == 8): 
            reply = 'Vsechno bude, neboj!'
        if(tmp == 9): 
            reply = 'Bezte si zrat kdy chcete!'
        if(tmp == 10):
            reply = 'Jidlo, jidlo? Makat se bude!'
        if(tmp == 11):
            reply = 'Diky, zatim nemam hlad.'
        return reply


    def getLunchTime(self,hour, low, high):
        """ 
            Generates lunch time in time from hour:low to hout:high interval
        """
        # function precondition
        if low < 0 or low > 59 or high < 0 or high > 59 or (high - low < 0) or hour < 0 or hour > 23: 
            return False

        minute = random.randint(low, high)
        prefix = str(hour)+":0" if minute < 10 else str(hour)+":"
        return prefix+str(minute)

    def getActualMinute(self):
        return datetime.datetime.now().minute
        
    def getActualHour(self):
        return datetime.datetime.now().hour


    def getLunchTimeFromNow(self,hour,high):
        """ 
            Returns lunch time in @hour from actual minute to a minute defined by @high
        """
        return self.getLunchTime(hour,self.getActualMinute(),high)
        
        
    def getLunchTimeNow(self,high):
        """ 
            Returns lunch time in @hour from actual minute to a minute defined by @high
        """
        return self.getLunchTime(self.getActualHour(),self.getActualMinute(),high)
