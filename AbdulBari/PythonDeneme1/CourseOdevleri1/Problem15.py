#Kullanýcýdan aldýðýnýz bir sayýnýn "Armstrong" sayýsý olup olmadýðýný bulmaya çalýþýn.

#Örnek olarak, Bir sayý eðer 4 basamaklý ise ve oluþturan rakamlardan herbirinin 
#4. kuvvetinin toplamý( 3 basamaklý sayýlar için 3.kuvveti ) o sayýya eþitse bu sayýya "Armstrong" sayýsý denir.

#Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
print("""******************
Armstrong Sayisi Bulma Programi
Cikis icin 0 veya sifirdan kucuk bir deger giriniz.      
******************  """)

while True:
    sayiyiGirdi=int(input("Lutfen Sorgulanacak Sayiyi Giriniz:"))
    temp=sayiyiGirdi
    basamakDegeri=0
    toplam=0
    if sayiyiGirdi==0 or sayiyiGirdi<0:
       print("Cikis isleminiz gerceklestiriliyor...")
       break
    
    for _ in str(temp):
       basamakDegeri += 1
    for i in str(temp):
       toplam += int(i)**basamakDegeri
    if sayiyiGirdi==toplam:
       print("{} sayisi armstrong sayisidir!".format(sayiyiGirdi))
    else:
       print("{} sayisi armstrong degildir!".format(sayiyiGirdi))
    print("Basamak Degeri:", basamakDegeri)
    print("Toplam Deger:", toplam)
    
    
       
