#Objemizin metodlarini ve �zelliklerini tan�mlad�g�m�z yer bizim classlarimizdir.
class Araba():
    model= "Renault Megane"
    renk="Gumus"                 #S�n�f�m�z�n �zellikleri (attiributsleri)
    beygir_gucu= 110
    silindir= 4
    #objelerimizi olusturuyoruz
    def __init__ (self):
        print("Init fonksiyonu cagriliyor")
araba1= Araba()
araba2=Araba()
print(araba1.model)
#_init_()
#Bu fonksiyon yap�c�(constructor) fonksiyondur, objeler �agr�l�rken ilk olu�turulan fonksiyondur. Bu metodu �zel oalrak tan�mlayarak objelerimizi farkl� degerlerle olu�turabiliriz
dir(araba1)
