#Objemizin metodlarini ve özelliklerini tanýmladýgýmýz yer bizim classlarimizdir.
class Araba():
    model= "Renault Megane"
    renk="Gumus"                 #Sýnýfýmýzýn özellikleri (attiributsleri)
    beygir_gucu= 110
    silindir= 4
    #objelerimizi olusturuyoruz
    def __init__ (self):
        print("Init fonksiyonu cagriliyor")
araba1= Araba()
araba2=Araba()
print(araba1.model)
#_init_()
#Bu fonksiyon yapýcý(constructor) fonksiyondur, objeler çagrýlýrken ilk oluþturulan fonksiyondur. Bu metodu özel oalrak tanýmlayarak objelerimizi farklý degerlerle oluþturabiliriz
dir(araba1)
