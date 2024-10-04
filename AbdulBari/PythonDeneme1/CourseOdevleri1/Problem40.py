#Elinizden her bir eleman� 3'l� bir demet olan bir liste olsun.

#     [(3,4,5),(6,8,10),(3,10,7)]

#�imdi kenar uzunluklar�na g�re bu kenarlar�n bir ��gen olup olmad���n� d�nen bir fonksiyon yaz�n ve sadece ��gen belirten kenarlar� bulunduran listeyi ekrana yazd�r�n.

#     [(3, 4, 5), (6, 8, 10)]

#*** Not: filter() fonksiyonunu kullanmaya �al���n. ***

def IsTriangle(x,y,z):
    if x+y>z and x+z>y and z+y>x:
        return True
    else:
        return False

Ucgenler=[(3,4,5),(6,8,10),(3,10,7)]

gecerli_ucgenler = list(filter(lambda t: IsTriangle(t[0], t[1], t[2]), Ucgenler))

print(gecerli_ucgenler)