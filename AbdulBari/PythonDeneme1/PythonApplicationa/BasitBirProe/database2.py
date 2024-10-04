from database1 import *


print("""**************************************************
 Kutuphane Programina Hos Geldiniz.

 Islemler: 
 1- Kitaplari Goster.  
 2- Kitap Sorgula
 3- Kitap Ekle
 4- Kitap Sil
 5- Baski Yukselt
    
 Cikis icin '*'
************************************************** """)

kutuphane = Kutuphane()


while True:
    islem = input("Yapacaginiz Islem: ")
    if (islem=='*'):
        print("Program Sonlandiriliyor...")
        break
    elif (islem=='1'):
        kutuphane.kitaplari_goster()
        
    elif (islem=='2'):
        isim=input("Hangi kitabi istiyorsunuz ?")
        print("Kitap sorgulaniyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)
        
    elif (islem=='3'):
        isim = input("Isim: ")
        yazar = input("Yazar: ")
        yayinevi= input("Yayinevi: ")
        tur=input("Tur: ")
        baski = int(input("Baski Yili: "))
        
        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)
        
        print("Kitap ekleniyor.....")
        time.sleep(2)
        
        kutuphane.kitap_ekle(yeni_kitap)
        
        print("Isleminiz basariyla gerceklesti")

    elif (islem=='4'):
        isim=input("Hangi kitabi silmek istiyorsunuz?")
        
        cevap = input("Bu kitabi silmek istediginizden emin misiniz? E / H")
        if (cevap=='E'):
            print("Kitap siliniyor....")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Isleminiz basariyla gerceklesti.")
        elif(cevap=='H'):
            pass
        else:
            print("Hatali Islem!")
    elif (islem=='5'):
        isim=input("Hangi kitabin baskisini yukseltmek istiyorsunuz ?")
        print("Baski yukseltiliyor....")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Islem basariyla gerceklesti....")
    else:
        print("Gecersiz islem!!!")