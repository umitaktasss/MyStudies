
#1'den 1000'e kadar olan sayýlardan mükemmel sayý olanlarý ekrana yazdýrýn. 
#Bunun için bir sayýnýn mükemmel olup olmadýðýný dönen bir tane fonksiyon yazýn.

#Bir sayýnýn bölenlerinin toplamý kendine eþitse bu sayý mükemmel bir sayýdýr. 
#Örnek olarak 6 mükemmel bir sayýdýr (1 + 2 + 3 = 6).

#1 den 1000e olan sayilari sorgula

#bir sayiyi sorgulayacak bir program yaz


def mukemmelSayi(sayi):
    toplam=0
    for i in range(1,(sayi//2)+1):
        if sayi % i ==0:
            toplam+=i
    if toplam == sayi:
        return True
    else:
        return False



sayilar=list(range(1,1001))
for i in sayilar:
    if mukemmelSayi(i):
        print("{} sayisi mukemmeldir.".format(i))