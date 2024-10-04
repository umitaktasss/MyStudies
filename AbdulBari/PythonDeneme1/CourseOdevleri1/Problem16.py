#Problem 1
#Kullanýcýdan aldýðýnýz bir sayýnýn mükemmel olup olmadýðýný bulmaya çalýþýn.

#Bir sayýnýn kendi hariç bölenlerinin toplamý kendine eþitse bu sayýya "mükemmel sayý" denir. Örnek olarak, 6 mükemmel bir sayýdýr. (1 + 2 + 3 = 6)

#Oncelikle bir sayýnýn bölenler 6- kendisi 3 2 1
#                               12- kendisi 6 3 2 1
#                                N- kendisi yarýsý ....
print("""********************
MUKEMMEL SAYI SORGULAMA EKRANI
Cikis icin "0" veya negatif bir deger giriniz      
********************""") 
cikis='*'
while True:
    toplam=0
    SorgulanacakSayi=int(input("Lutfen sayinizi giriniz:"))
    if SorgulanacakSayi ==0 or SorgulanacakSayi <0:
        print("Cikis isleminiz gerceklestiriliyor...")
        break
    else:    
        for sayac in range(1,int((SorgulanacakSayi/2))+1):
            if SorgulanacakSayi % sayac == 0 :
                toplam+=sayac
            
        if SorgulanacakSayi==toplam:    
         print("{} sayisi mukemmel bir sayidir!".format(SorgulanacakSayi))
        else:
         print("{} mukemmel sayi degildir.".format(SorgulanacakSayi))
     
        