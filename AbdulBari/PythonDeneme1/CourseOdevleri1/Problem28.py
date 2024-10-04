import math
help(math)
print("""******************
Gelismis Hesap Makinesine Hos geldiniz...
Yapmak Istediginiz Islemi Secin:
1-Logaritma Almak
    a-Logaritmik Islemleri Topla
    b-Logaritmik Islemleri Carp
    C-Logaritmik Islemleri Bol
    d-Logaritmik Islemleri Cikar
2-Us almak
    a-Uslu Sayilari Topla
    b-Uslu Sayilari Carp
    C-Uslu Sayilari Bol
    d-Uslu Sayilari Cikar      
3-Karekok Almak
    a-Karekoklu Sayilari Topla
    b-Karekoklu Sayilari Carp
    C-Karekoklu Sayilari Bol
    d-Karekoklu Sayilari Cikar         
4-Trigonometri
      
Cikis icin '*' Tusuna Basiniz.      
      """)



while True:
    girdi=input("Lutfen Bir Deger Giriniz")
    if girdi=='*':
        break
    girdi=int(girdi)
    if girdi==1:
        girdi2=input("Yapmak Istediginiz islemi secin")
        if girdi2=='a':
            pass