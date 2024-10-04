#Sayi Tahmin Oyunu
import random
import time
print("""
********************

            
Sayi Tahmin Oyunu Hos geldiniz...
      

********************
""")
rastgele_Sayi=random.randint(1,40)
tahmin_hakki=7
while True:
    tahmin=int(input("Tahmininizi giriniz: "))
   
    
    if (tahmin<rastgele_Sayi and tahmin<40 and tahmin>0):
           print("Bilgiler sorgulaniyor lutfen bekleyiniz")
           time.sleep(1)
           print("Tahmin ettiginiz sayi asil sayidan kucuktur. Buyuk bir sayi giriniz lutfen")
           tahmin_hakki-=1
    elif (tahmin>rastgele_Sayi and tahmin<40 and tahmin>0):
           print("Bilgiler sorgulaniyor lutfen bekleyiniz")
           time.sleep(1)
           print("Tahmin ettiginiz sayi asil sayidan buyuktur. Kucuk bir sayi giriniz lutfen")
           tahmin_hakki-=1
    elif (tahmin==rastgele_Sayi):
           print("Bilgiler sorgulaniyor lutfen bekleyiniz")
           time.sleep(1)
           print("Tebrikler Oyunu Kazandiniz!")
           break
    else:
          print("Tahmin aralagindan farkli bir deger girdiniz...")
          tahmin_hakki-=1
          print("Tahmin Hakkiniz:", tahmin_hakki)
    if(tahmin_hakki==0):
          print("Tahmin Hakkiniz Bitti, Sayi:",rastgele_Sayi)  
          break
    
    