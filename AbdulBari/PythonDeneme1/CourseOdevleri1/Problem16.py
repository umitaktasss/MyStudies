#Problem 1
#Kullan�c�dan ald���n�z bir say�n�n m�kemmel olup olmad���n� bulmaya �al���n.

#Bir say�n�n kendi hari� b�lenlerinin toplam� kendine e�itse bu say�ya "m�kemmel say�" denir. �rnek olarak, 6 m�kemmel bir say�d�r. (1 + 2 + 3 = 6)

#Oncelikle bir say�n�n b�lenler 6- kendisi 3 2 1
#                               12- kendisi 6 3 2 1
#                                N- kendisi yar�s� ....
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
     
        