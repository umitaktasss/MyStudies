from re import A
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

print(response)

html_icerigi=response.content

soup=BeautifulSoup(html_icerigi,"html.parser")
#a etiketine sahip tüm özellikleri çeker.
for i in soup.findAll("a"):
    print(i.get("href"))
    print("******************************")