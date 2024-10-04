#OverRidding(Iptal Etme)
#Eðer biz biraz aldýðýmýz metodlari ayni isimle kendi sýnýfýmýzda tekrar
#tanýmlarsak, artýk metodu çaðýrdýðýmýz zaman miras aldýðýmýz deðil kendi metodumuz çalýþacaktýr
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
#Super anahtar kelimesi özellikle override ettiðimiz bir metodun içinde
#ayný zamanda miras aldýðýmýz bir metodu kullanmak istersek kullanabilir. 
#Yani super en genel anlamýyla miras aldýðýmýz sýnýfýn metodlarýný alt sýnýflardan kullanmamýzý saðlar
