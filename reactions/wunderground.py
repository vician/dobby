from reactions.reaction import Reaction

class Wunderground(Reaction):
    help = "Weather forecast from https://alojz.cz - only in czech!\nRun: $ alojz [city=praha]"
    aliasses = [ "wunderground", "pywu", "weather" ]

    attributes = [ "api", "city" ]

    downloader = None
    parser = None

    def init(self):
        # Default values
        self.ini.set("city","Prague")
        self.ini.set("api","-")
 
    def do(self,city=None):
        if city is None or city == "":
            city = self.ini.get("city")
        return self.weather(city.lower())

    def weather(self,city):
        return "preparing"
