# Elimizde bir dikd�rtgenin kenarlar�n� ifade eden say� �iftlerinin bulundu�u bir liste olsun
#[(3,4),(10,3),(5,6),(1,9)]
#�imdi kenar uzunluklar�na g�re dikd�rtgenin alan�n� hesaplayan bir fonksiyon yaz�n ve bu listenin her bir eleman�na
# bu fonksiyonu uygulayarak ekrana ��yle bir liste yazd�r�n.
#[12,30,30,9]
from itertools import starmap
def diktorgen_Alan_Hesapla(x,y):
    return x*y

Alan = list(map(lambda t: diktorgen_Alan_Hesapla(t[0], t[1]), [(3, 4), (10, 3), (5, 6), (1, 9)]))
print(Alan)  # ��kt�: [12, 30, 30, 9]


Alan = list(starmap(diktorgen_Alan_Hesapla, [(3, 4), (10, 3), (5, 6), (1, 9)]))
print(Alan)  # ��kt�: [12, 30, 30, 9]

Alan=list(map(lambda x: x[0]*x[1], [(3,4),(10,3),(5,6),(1,9)]))
print(Alan)