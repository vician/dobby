#!/usr/bin/env python3

import sys
from datetime import datetime # date
import netifaces as ni # show_ip
import random #jidlo

from reactions.Cleverbot import Cleverbot
from reactions import lunchTime

def say(message):
    print(message)

def show_ip():
    ifaces = ni.interfaces()
    reply = "My IPs are:"

    for iface in ifaces:
        ni.ifaddresses(iface)
        ip4 = ni.ifaddresses(iface)[2][0]['addr']
        ip6 = ni.ifaddresses(iface)[10][0]['addr']
        reply += "\n{}: {}".format(str(iface), str(ip4))
        reply += "\n{}: {}".format(str(iface), str(ip6))

    say(reply)

def jidlo():
    """Dobby says at what time my masters eat today."""
    tmp = random.randint(0, 11)

    if(tmp <= 7):
        cas = lunchTime.getLunchTimeNow(59)
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
    say(reply)


if __name__ == '__main__':

    say("Hi, I'm your house-elf Dobby. How can I help you?")

    cleverbot = Cleverbot()

    while True:
        print ("$ ", end="", flush=True)
        userinput = sys.stdin.readline().rstrip('\n')
        first = userinput.partition(' ')[0]
        if first == 'quit':
            break
        elif first == "date":
            say("Today is "+datetime.now().strftime('%Y-%m-%d'))
        elif first == "ip":
            show_ip()
        elif first == "jidlo":
            jidlo()
        else:
            reply = cleverbot.ask(userinput)
            say(reply)

    say("Yes, master. I'm going to sleep.")
