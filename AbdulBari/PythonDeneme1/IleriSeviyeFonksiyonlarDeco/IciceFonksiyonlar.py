def selamla(isim):
    print("Selam",isim)


selamla("Aliye")

#selamla fonksiyonunu merhaba objesine atayabiliyoruz.
merhaba  = selamla


merhaba("Kemal")
#Selamla fonksiyonunu silmemize ragmen merhaba fonksiyonu �al��acakt�r.
del selamla
merhaba("Abi")

def fonksiyon5():
    #Bu fonksiyona sadece i�eriden eri�im vard�r!!! D��ar�dan eri�ilemez...
    def fonksiyonIc():
        print("Kucuk Fonksiyondan Merhaba!")
    fonksiyonIc()
    print("Buyuk fonksiyondan merhaba!")


fonksiyon5()


def fonksiyon6(*args):
    
    def toplama(args):
        toplam =0
        
        for i in args:
            toplam += i
        return toplam
    print(toplama(args))


fonksiyon6(1,3,5,7,11,13,15,17,19,21)