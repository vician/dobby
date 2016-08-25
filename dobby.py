#!/usr/bin/env python3

import sys
from datetime import datetime # date
import netifaces as ni # show_ip
import random #jidlo

import urllib3 # talker
import urllib.request
import bleach

from reactions.Cleverbot import Cleverbot
from reactions import lunchTime
from reactions.talker import Talker

try:
    from bs4 import BeautifulSoup # available via pip as BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

def say(message,talker=None):
    if talker != None:
        talker.addAndSayMessage(message)
    print(message)

def downloadURL(url):
    """ 
    Download url to string
    """

    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8')
    return text

    #req = urllib3.Request(url)
    #try:
    #    response = urllib3.urlopen(req)
    #except urllib3.HTTPError as e:
    #    print('The server couldn\'t fulfill the request.')
    #    print('Error code: ', e.code)
    #    return -1
    #except urllib3.URLError as e:
    #    print('We failed to reach a server.')
    #    print('Reason: ', e.reason)
    #    return -2
    #else:
    #    html = response.read()
    #    return html


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

def alojz():
    page = downloadURL("https://alojz.cz/")
    html = BeautifulSoup(page,"lxml")
    h2 = html.body.find('h2', {"class" : "actual-forecast"}).text
    reply = bleach.clean(h2)
    reply = ' '.join(reply.split()) # Remove redundant whitspaces
    say(reply)


if __name__ == '__main__':

    talker = Talker()
    talker.useEpos()
    say("Hi, I'm your house-elf Dobby. How can I help you?",talker)

    cleverbot = Cleverbot()

    while True:
        print ("$ ", end="", flush=True)
        userinput = sys.stdin.readline().rstrip('\n')
        first = userinput.partition(' ')[0]
        if first == 'quit' or first == 'exit' or first == 'bye':
            break
        elif first == "date":
            say("Today is "+datetime.now().strftime('%Y-%m-%d'))
        elif first == "ip":
            show_ip()
        elif first == "jidlo":
            jidlo()
        elif first == "alojz":
            alojz()
        elif first == "weather":
            alojz()
        else:
            reply = cleverbot.ask(userinput)
            say(reply)

    say("Yes, master. I'm going to sleep.")
