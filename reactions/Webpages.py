#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 15 Aug 2014

@author: rlat
'''

import urllib2
import re

import lxml.html
from lxml import etree
try:
    from bs4 import BeautifulSoup # available via pip as BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


import sys

class Webpages(object):
    '''
    Gets content from specific web pages.
    '''

    HTML_BODY_START_B = b'<html><head></head><body>'
    HTML_BODY_END_B = b'</body></html>'
    HTML_BODY_START = '<html><head></head><body>'
    HTML_BODY_END = '</body></html>'

    def __init__(self):
        '''
        Constructor
        '''
        reload(sys)  # Reload does the trick!
        sys.setdefaultencoding('UTF8')
        self.parser = etree.HTMLParser(remove_blank_text=True, remove_comments=True, remove_pis=True)
            
    def __add_body(self, string=b''):
        '''
        Adds body tags to given source code.
        :param string: Input string.
        :type string: str or bytes.
        '''
        if isinstance(string, str):
            return self.HTML_BODY_START + string + self.HTML_BODY_END
        else:
            return self.HTML_BODY_START_B + string + self.HTML_BODY_END_B
        
    def __get_root(self, source_code):
        '''
        Tries to parse give source code using different parsers and parser
        settings.
        :return: etree.Element representing the document root if parsing
              has succeeded, None otherwise.
        '''
        try:  # try to parse using lxml, if it fails use bs4 parser to fix the code
            return lxml.html.fromstring(source_code, parser=self.parser)
        except Exception:
            pass
        
        try:  # use bs4 to fix code
            return lxml.html.fromstring(str(BeautifulSoup(source_code)), parser=self.parser)
        except Exception:
            pass
        
        # try put content into HTML body
        new_sc = self.__add_body(source_code)
        
        try:  # try to parse using lxml, if it fails use bs4 parser to fix the code
            return lxml.html.fromstring(new_sc, parser=self.parser)
        except Exception:
            pass
        
        try:  # use bs4 to fix code
            return lxml.html.fromstring(str(BeautifulSoup(new_sc)), parser=self.parser)
        except Exception:
            pass
        
        return None
    
    def __rem_html(self, html_root):
        """
        Removes HTML syntax.
        :param html_root: Root element.
        """
        return etree.tostring(html_root, method="text", encoding="utf-8").decode('utf-8').strip() 
 
    @staticmethod
    def downloadURL(url):
        """
        Download url to string
        """
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
         
        req = urllib2.Request(url, headers=hdr)
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            return -1
        except urllib2.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
            return -2
        else:
            html = response.read()
            return html
     
    def getRacekMenu(self):
        """
        :return: Returns tuple (success, data), where if success is True, data
        is current menu from racek. If success is False, data is error message.
        """
        html = self.downloadURL("http://www.restaurace-racek.cz/sluzby/")
        parsed_html = self.__get_root(html.decode('utf-8', errors='ignore'))
        if parsed_html is None:
            return (False, "Parsing of the web page failed.")
         
        text = self.__rem_html(parsed_html.find("./body//table"))
        
        #remove tabs               
        text = re.sub('[\t\xa0]+|\s*!!!.*', '', text, flags=re.S)
        
        # merge new lines into one
        text = re.sub('\n+', '\n', text, flags=re.M)
        
        # format output
        return re.sub('MENU ([IV]+)\n([0-9]+,-)\n([0-9]+g)\n([^\n]+)', '\\1: \\4 (\\3) \\2', text, flags=re.S|re.M)

    def getUrban(self):
        """
        :return: Returns tuple (success, data), where if success is True, data
        is current menu from racek. If success is False, data is error message.
        """
        html = self.downloadURL("http://www.urban-restaurant.cz/denni-menu")

        soup = BeautifulSoup(html.decode('utf-8', errors='ignore'))
        menu = soup.find("div", {"class": "daily_menu"})


        # format output
        return menu("p", "title")


if __name__ == "__main__":
    w = Webpages()
    print(w.getUrban())

