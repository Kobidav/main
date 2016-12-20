from bs4 import BeautifulSoup
import requests

url = "http://www.rmblaw.co.il/legal_team/"
file_name = requests.get(url)
# html = open(file_name.text, 'r')
soup = BeautifulSoup(file_name.text, "lxml")
abc_pages = soup.find_all("div", attrs={"class": "abc_letter"})
list_of_abc = []
list_of_image = {}
for a in abc_pages:
    list_of_abc.append(('http://www.rmblaw.co.il' + a.find('a').get('href')))

for abc_link in list_of_abc:
    file_name = requests.get(abc_link)
    soup = BeautifulSoup(file_name.text, "lxml")
    lawyers_on_page = soup.find_all(
        "div", attrs={"class": "views-field-title"})
    list_of_law_link = {}
    for a in lawyers_on_page:
        list_of_law_link[
            (('http://www.rmblaw.co.il' + a.find('a').get(
                'href')))] = a.find('a').text
    for law_link in list_of_law_link.keys():
        file_name = requests.get(law_link)
        soup = BeautifulSoup(file_name.text, "lxml")
        image_on_page = soup.find_all("div", attrs={"id": "lawyer_image"})
        for link_image in image_on_page:
            list_of_image[(list_of_law_link[law_link])[0:-6]] = (
                'http://www.rmblaw.co.il' + (link_image.find(
                    'img').get('src')))


for a in list_of_image.keys():
    print (a, ",", list_of_image[a] )

