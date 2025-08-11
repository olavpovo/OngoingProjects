import requests
from bs4 import BeautifulSoup

source = requests.get("https://adhdefined.com/").text
soup = BeautifulSoup(source, 'lxml')

# test=soup.find("hfeed site")

print(soup.title.text)
