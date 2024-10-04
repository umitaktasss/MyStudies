#Kalitim
#Bir sýnýfýn baþka bir sýnýfýn özelliklerini ve metodlarýný miras almasýdýr.
#Ana fonksiyon
from pyclbr import Class
from re import S
from typing import Self


class Calisan():
    def __init__(self,isim,maas,departman):
        self.isim= isim
        self.maas=maas
        self.departman=departman
    def bilgilerigoster(self):
        print("Calisan Sinifinin Bilgileri.........")
        print("Isim: {}\nMaas: {}\nDepartman: {}".format(self.isim,self.maas,self.departman))
    def departman_degistir(self,yeni_departman):
            self.departman=yeni_departman



class Yonetici(Calisan):
    def zam_yap(self,yeni_zam):
        self.maas+=yeni_zam 

yonetici=Yonetici("Umit Aktas",3000,"Game Development")
yonetici.bilgilerigoster()
yonetici.departman_degistir("VFX Studio")
yonetici.bilgilerigoster()
