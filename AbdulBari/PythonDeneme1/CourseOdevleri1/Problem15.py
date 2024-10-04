#Kullan�c�dan ald���n�z bir say�n�n "Armstrong" say�s� olup olmad���n� bulmaya �al���n.

#�rnek olarak, Bir say� e�er 4 basamakl� ise ve olu�turan rakamlardan herbirinin 
#4. kuvvetinin toplam�( 3 basamakl� say�lar i�in 3.kuvveti ) o say�ya e�itse bu say�ya "Armstrong" say�s� denir.

#�rnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
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
    
    
       
