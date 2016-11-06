from bs4 import BeautifulSoup
import requests
from datetime import datetime


class Nod:
    def __init__(self, version, data):
        self.version = version
        self.data = data
    def get(self):
        url = "https://www.eset.com/us/threat-center/threatsense-updates/"
        file_name = requests.get(url)


url = "https://www.eset.com/us/threat-center/threatsense-updates/"
file_name = requests.get(url)
#html = open(file_name.text, 'r')
soup = BeautifulSoup(file_name.text, "lxml")
string = soup.h2.text
version = string[10:15]
data = (string[17:-1]).replace(',', '')
date_object = datetime.strptime(data, '%B %d %Y')
#print (version)
#print (date_object.date())

Eset_version = Nod(version, date_object)
#print (Eset_version.version, Eset_version.data.date())


