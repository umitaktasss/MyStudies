#doviz.com sitesinden veri al�p g�ncel dolar�n,euronun,alt�n�n ve borsan�n de�erleri
from locale import currency
import requests
from bs4 import BeautifulSoup

url="https://www.doviz.com/"

response=requests.get(url)

if response.status_code == 200:
    soup=BeautifulSoup(response.content,'html.parser')
    
    #print(soup.prettify())
    currency_data=soup.find_all('div',class_='item') 
    
    for currency in currency_data:
          name = currency.find('span', class_='name').text
          value = currency.find('span', class_='value').text
          print(f"{name}: {value}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
