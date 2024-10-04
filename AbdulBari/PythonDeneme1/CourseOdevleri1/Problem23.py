
#1'den 1000'e kadar olan say�lardan m�kemmel say� olanlar� ekrana yazd�r�n. 
#Bunun i�in bir say�n�n m�kemmel olup olmad���n� d�nen bir tane fonksiyon yaz�n.

#Bir say�n�n b�lenlerinin toplam� kendine e�itse bu say� m�kemmel bir say�d�r. 
#�rnek olarak 6 m�kemmel bir say�d�r (1 + 2 + 3 = 6).

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