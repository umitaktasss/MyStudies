import requests
from bs4 import BeautifulSoup

# API anahtarýnýzý buraya girin
api_key = '2a3413cd2011ead5981354dbf2c11e9a'

# Fixer.io API URL
url = f'http://data.fixer.io/api/latest?access_key={api_key}'

# API'ye istekte bulunalým
response = requests.get(url)

# Gelen yanýtý JSON formatýna çevirelim
data = response.json()

print("""******************************************
 1-USD: Amerika Dolari
 2-EUR: Euro
 3-TRY: Turk Lirasi
 4-GBP: Ingiliz Sterlini
 5-CAD: Kanada Dolari
 6-AUD: Avustralya Dolari
 7-JPY: Japon Yeni
 8-CHF: Isvicre Frangi
 9-CNY: Cin Yuani     
 10-RUB: Rus Rublesi
 11-INR: Hindistan Rupisi     
 12-BRL: Brezilya Reali     
 13-MXN: Meksika Pesosu 
 14-ZAR: Guney Afrika Randi
******************************************    
            """)


doviz_1=input("Ilk Doviz Biriminizi Giriniz(OR:EUR): ").upper()
doviz_2=input("Ikinci Doviz Biriminizi Giriniz(OR:TRY):").upper()
miktar=float(input("Miktar giriniz: "))

# Eðer isteðimiz baþarýlý ise
if data['success']:
    # Her iki döviz birimi için EUR karþýlýðý alýnýr
    euro_to_doviz_1 = data['rates'][doviz_1]
    euro_to_doviz_2 = data['rates'][doviz_2]
    
    # doviz_1'i doviz_2'ye dönüþtürmek için formül:
    doviz_1_to_doviz_2 = miktar * (euro_to_doviz_2 / euro_to_doviz_1)
    
    print(f"{miktar} {doviz_1} = {doviz_1_to_doviz_2:.3f} {doviz_2}")
else:
    # Eðer istek baþarýsýz olduysa, hatayý yazdýralým
    print(f"Hata: {data['error']['info']}")
