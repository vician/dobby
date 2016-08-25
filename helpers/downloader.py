import urllib.request

class Downloader():

    def download(self,url):
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        return text
