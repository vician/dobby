from bs4 import BeautifulSoup
import bleach

class Parser():

    def parse(self,page,element,type_nane,name):

        html = BeautifulSoup(page,"lxml")

        h2 = html.body.find(element, {type_nane : name}).text

        reply = bleach.clean(h2)

        reply = ' '.join(reply.split()) # Remove redundant whitspaces

        return reply

    def parse_class(self,page,element,name):
        return self.parse(page,element,"class",name)
    
    def parse_id(self,page,element,name):
        return self.parse(page,element,"id",name)
