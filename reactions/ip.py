from reactions.reaction import Reaction

import netifaces as ni

class Ip(Reaction): # Change name of this class!

    help = "Show IP addresses on network interfaces.\nConfig: ipv4=[0/1] ipv6=[0/1]"
    aliasses = [ "ip" ]
    attributes = [ "ipv4", "ipv6" ]

    def init(self):
        self.ini.set("ipv4","1")
        self.ini.set("ipv6","1")

    def do(self,message):
        if self.ini.get("ipv4") != "1" and self.ini.get("ipv6") != "1":
            return "Please allow ipv4 and/or ipv6 in config"

        ifaces = ni.interfaces()

        reply = "My IPs are:"
        reply4 = ""
        reply6 = ""

        for iface in ifaces:
            ni.ifaddresses(iface)
            ip4 = ni.ifaddresses(iface)[2][0]['addr']
            ip6 = ni.ifaddresses(iface)[10][0]['addr']
            reply4 += "\n- {}: {}".format(str(iface), str(ip4))
            reply6 += "\n- {}: {}".format(str(iface), str(ip6))

        if self.ini.get("ipv4") == "1":
            reply += "\nIPv4:"+reply4
        if self.ini.get("ipv6") == "1":
            reply += "\nIPv6:"+reply6

        return reply
