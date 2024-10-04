#Kullanýcýdan ad,soyad ve numara bilgisini alarak bunlarý alt alta ekrana yazdirin
ad=input("Lutfen Adinizi Giriniz:")
soyad=input("Lutfen Soy Adinizi Giriniz:")
numara=input("Lutfen Ogrenci Numaranizi Giriniz:")
bilgiler=[ad,soyad,numara]
print("Girdiginiz Bilgileriniz:")
print("Ad: {}\nSoyad: {}\nNumara: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))