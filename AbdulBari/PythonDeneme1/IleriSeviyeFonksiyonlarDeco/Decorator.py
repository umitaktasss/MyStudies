#Kod tekrarlý kod.
import time
#Goruldugu üzere bu kodlar içerisinde kendini tekrar eden kod bloklarý var.
def kareleri_hesapla(sayilar):
    
    kare=list()
    baslama=time.time()
    for i in sayilar:
        kare.append(i**2)
    bitis=time.time()
    print("Bu fonksiyon"+str(bitis-baslama)+"saniye surdu.")
    return kare


        
def kupleri_hesapla(sayilar):
    
    kup=list()
    baslama=time.time()
    for i in sayilar:
        kup.append(i**3)
    bitis=time.time()
    print("Bu fonksiyon"+str(bitis-baslama)+"saniye surdu.")
    return kup

kareleri_hesapla(range(100000))
kupleri_hesapla(range(100000))
