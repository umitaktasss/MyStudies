#OverRidding(Iptal Etme)
#E�er biz biraz ald���m�z metodlari ayni isimle kendi s�n�f�m�zda tekrar
#tan�mlarsak, art�k metodu �a��rd���m�z zaman miras ald���m�z de�il kendi metodumuz �al��acakt�r
#Buna NTP bir metodu override  etmek denir.
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
    #Override
    def __init__(self, isim, maas, departman,kisi_Sayisi):
        self.isim= isim
        self.maas=maas
        self.departman=departman 
        self.kisi_Sayisi=kisi_Sayisi
     
    def zam_yap(self,yeni_zam):
        self.maas+=yeni_zam
    #Override
    def bilgilerigoster(self):
        print("Calisan Sinifinin Bilgileri.........")
        print("Isim: {}\nMaas: {}\nDepartman: {}\nSorumlu kisi sayisi: {}".format(self.isim,self.maas,self.departman,self.kisi_Sayisi))
 
yonetici=Yonetici("Oguz Artiran",3600,"Bilisim",10)
yonetici.bilgilerigoster()
#Super
#Super anahtar kelimesi �zellikle override etti�imiz bir metodun i�inde
#ayn� zamanda miras ald���m�z bir metodu kullanmak istersek kullanabilir. 
#Yani super en genel anlam�yla miras ald���m�z s�n�f�n metodlar�n� alt s�n�flardan kullanmam�z� sa�lar
