from reactions.reaction import Reaction

import netifaces as ni

class Ip(Reaction): # Change name of this class!

    help = "Show IP addresses on network interfaces."
    aliasses = [ "ip" ]

    def do(self,message):
        ifaces = ni.interfaces()

        reply = "My IPs are:"

        for iface in ifaces:
            ni.ifaddresses(iface)
            ip4 = ni.ifaddresses(iface)[2][0]['addr']
            ip6 = ni.ifaddresses(iface)[10][0]['addr']
            reply += "\n{}: {}".format(str(iface), str(ip4))
            reply += "\n{}: {}".format(str(iface), str(ip6))

        return reply
