# Elimizde bir dikdörtgenin kenarlarýný ifade eden sayý çiftlerinin bulunduðu bir liste olsun
#[(3,4),(10,3),(5,6),(1,9)]
#Þimdi kenar uzunluklarýna göre dikdörtgenin alanýný hesaplayan bir fonksiyon yazýn ve bu listenin her bir elemanýna
# bu fonksiyonu uygulayarak ekrana þöyle bir liste yazdýrýn.
#[12,30,30,9]
from itertools import starmap
def diktorgen_Alan_Hesapla(x,y):
    return x*y

Alan = list(map(lambda t: diktorgen_Alan_Hesapla(t[0], t[1]), [(3, 4), (10, 3), (5, 6), (1, 9)]))
print(Alan)  # Çýktý: [12, 30, 30, 9]


Alan = list(starmap(diktorgen_Alan_Hesapla, [(3, 4), (10, 3), (5, 6), (1, 9)]))
print(Alan)  # Çýktý: [12, 30, 30, 9]

Alan=list(map(lambda x: x[0]*x[1], [(3,4),(10,3),(5,6),(1,9)]))
print(Alan)