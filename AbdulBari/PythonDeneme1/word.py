class Ogrenci:
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.bolum = bolum
        self.__telefonno = telefonno  # erisim kisitlandi

    # encapsulation
    def get_telefonno(self):
        return self.__telefonno

    def set_telefonno(self, yeni_telefonno):
        self.__telefonno = yeni_telefonno

# inheritance (kalitim)
class GeziToplulugu(Ogrenci):
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        super().__init__(ad, soyad, numara, bolum, telefonno)

    def ogrenci_ekle(self, ogrenci):
        # Gezi topluluguna eklenen ogrenciye ozel bir islem uygulayin (overriding)
        print(f"{ogrenci.ad} {ogrenci.soyad} gezi topluluguna eklendi ve karti verildi.")


class YBSToplulugu(Ogrenci):
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        super().__init__(ad, soyad, numara, bolum, telefonno)

    def ogrenci_ekle(self, ogrenci):
        # YBS topluluguna eklenen ogrenciye ozel bir islem uygulayin (overriding)
        print(f"{ogrenci.ad} {ogrenci.soyad} YBS topluluguna eklendi ve rozet takildi.")


class YazilimToplulugu(Ogrenci):
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        super().__init__(ad, soyad, numara, bolum, telefonno)

    def ogrenci_ekle(self, ogrenci):
        # Yazilim topluluguna eklenen ogrenciye ozel bir islem uygulayin (overriding)
        print(f"{ogrenci.ad} {ogrenci.soyad} yazilim topluluguna eklendi ve erisim karti verildi.")


class OgrenciToplulugu:
    def __init__(self):
        self.gezi_ogrenciler = []
        self.ybs_ogrenciler = []
        self.yazilim_ogrenciler = []

    # polymorphism
    def ogrenci_ekle(self, ogrenci, topluluk):
        if topluluk == "gezi":
            self.gezi_ogrenciler.append(ogrenci)
            print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()} gezi ogrenci listesine eklendi.")
        elif topluluk == "ybs":
            self.ybs_ogrenciler.append(ogrenci)
            print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()} YBS ogrenci listesine eklendi.")
        elif topluluk == "yazilim":
            self.yazilim_ogrenciler.append(ogrenci)
            print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()} yazilim ogrenci listesine eklendi.")
        else:
            print("Gecersiz topluluk.")

    # polymorphism (each subclass removes students from its list)
    def ogrenci_cikar(self, ogrenci, topluluk):
        if topluluk == "gezi":
            if ogrenci in self.gezi_ogrenciler:
                self.gezi_ogrenciler.remove(ogrenci)
                print(f"{ogrenci.ad} {ogrenci.soyad} gezi ogrencisi topluluktan cikarildi.")
            else:
                print("Ogrenci listede bulunamadi.")
        elif topluluk == "ybs":
            if ogrenci in self.ybs_ogrenciler:
                self.ybs_ogrenciler.remove(ogrenci)
                print(f"{ogrenci.ad} {ogrenci.soyad} YBS ogrencisi topluluktan cikarildi.")
            else:
                print("Ogrenci listede bulunamadi.")
        elif topluluk == "yazilim":
            if ogrenci in self.yazilim_ogrenciler:
                self.yazilim_ogrenciler.remove(ogrenci)
                print(f"{ogrenci.ad} {ogrenci.soyad} yazilim ogrencisi topluluktan cikarildi.")
            else:
                print("Ogrenci listede bulunamadi.")
        else:
            print("Gecersiz topluluk.")

    def ogrenci_listele(self, topluluk):
        if topluluk == "gezi":
            ogrenci_listesi = self.gezi_ogrenciler
        elif topluluk == "ybs":
            ogrenci_listesi = self.ybs_ogrenciler
        elif topluluk == "yazilim":
            ogrenci_listesi = self.yazilim_ogrenciler
        else:
            print("Gecersiz topluluk.")
            return

        for ogrenci in ogrenci_listesi:
            print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()}")


def main():
    topluluk = OgrenciToplulugu()

    while True:
        print("\n1. Ogrenci Ekle")
        print("2. Ogrenci Cikar")
        print("3. Ogrenci Listele")
        print("4. Cikis")

        secim = input("Lutfen bir secim yapiniz: ")

        if secim == "1":
            ad = input("Ogrenci adi: ")
            soyad = input("Ogrenci soyadi: ")
            numara = input("Ogrenci numarasi: ")
            bolum = input("Ogrenci bolumu: ")
            telefonno = input("Ogrenci Telefon no: ")
            topluluk_secim = input("Ogrenci hangi topluluga eklenecek (gezi/ybs/yazilim): ")
            ogrenci = None
            if topluluk_secim == "gezi":
                ogrenci = GeziToplulugu(ad, soyad, numara, bolum, telefonno)
            elif topluluk_secim == "ybs":
                ogrenci = YBSToplulugu(ad, soyad, numara, bolum, telefonno)
            elif topluluk_secim == "yazilim":
                ogrenci = YazilimToplulugu(ad, soyad, numara, bolum, telefonno)
            else:
                print("Gecersiz topluluk.")
                continue
            topluluk.ogrenci_ekle(ogrenci, topluluk_secim)
        elif secim == "2":
            ad = input("Ogrenci adi: ")
            soyad = input("Ogrenci soyadi: ")
            topluluk_secim = input("Ogrenci hangi topluluktan cikarilacak (gezi/ybs/yazilim): ")
            silinecek_ogrenci = None
            if topluluk_secim == "gezi":
                for ogrenci in topluluk.gezi_ogrenciler:
                    if ogrenci.ad == ad and ogrenci.soyad == soyad:
                        silinecek_ogrenci = ogrenci
                        break
            elif topluluk_secim == "ybs":
                for ogrenci in topluluk.ybs_ogrenciler:
                    if ogrenci.ad == ad and ogrenci.soyad == soyad:
                        silinecek_ogrenci = ogrenci
                        break
            elif topluluk_secim == "yazilim":
                for ogrenci in topluluk.yazilim_ogrenciler:
                    if ogrenci.ad == ad and ogrenci.soyad == soyad:
                        silinecek_ogrenci = ogrenci
                        break
            else:
                print("Gecersiz topluluk.")
                continue
            if silinecek_ogrenci:
                topluluk.ogrenci_cikar(silinecek_ogrenci, topluluk_secim)
            else:
                print("Ogrenci listede bulunamadi.")
        elif secim == "3":
            topluluk_secim = input("Hangi toplulugun ogrencileri listelenecek (gezi/ybs/yazilim): ")
            topluluk.ogrenci_listele(topluluk_secim)
        elif secim == "4":
            print("Programdan cikiliyor...")
            break
        else:
            print("Gecersiz bir secim yaptiniz. Lutfen tekrar deneyin.")

if __name__ == "__main__":
    main()

         

