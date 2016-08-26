from reactions.reaction import Reaction

from helpers.downloader import Downloader
from helpers.parser import Parser

class Alojz(Reaction):
    help = "Weather forecast from https://alojz.cz - only in czech!\nRun: $ alojz [city=praha]"
    aliasses = [ "alojz", "weather" ]

    downloader = None
    parser = None

    def init(self):
        self.downloader = Downloader()
        self.parser = Parser()
        # Default values
        self.ini.set("city","praha")

    def parameters_init(self):
        self.parameters = Class()
        self.parameters.city = "praha"

    def do(self,city=None):
        if city is None or city == "":
            city = self.ini.get("city")
        return self.weather(city.lower())

    def weather(self,city):
        page = self.downloader.download("https://alojz.cz/"+city)

        return self.parser.parse_class(page,"h2","actual-forecast")
