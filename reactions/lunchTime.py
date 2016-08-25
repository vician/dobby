import random
import datetime

def getLunchTime(hour, low, high):
    """
        Generates lunch time in time from hour:low to hout:high interval
    """
    # function precondition
    if low < 0 or low > 59 or high < 0 or high > 59 or (high - low < 0) or hour < 0 or hour > 23:
        return False

    minute = random.randint(low, high)
    prefix = str(hour)+":0" if minute < 10 else str(hour)+":"
    return prefix+str(minute)

def getActualMinute():
    return datetime.datetime.now().minute
    
def getActualHour():
    return datetime.datetime.now().hour


def getLunchTimeFromNow(hour,high):
    """
        Returns lunch time in @hour from actual minute to a minute defined by @high
    """
    return getLunchTime(hour,getActualMinute(),high)
    
    
def getLunchTimeNow(high):
    """
        Returns lunch time in @hour from actual minute to a minute defined by @high
    """
    return getLunchTime(getActualHour(),getActualMinute(),high)

#print getLunchTimeFromNow(11,59)
