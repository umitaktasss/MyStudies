#Elinizden her bir elemaný 3'lü bir demet olan bir liste olsun.

#     [(3,4,5),(6,8,10),(3,10,7)]

#Þimdi kenar uzunluklarýna göre bu kenarlarýn bir üçgen olup olmadýðýný dönen bir fonksiyon yazýn ve sadece üçgen belirten kenarlarý bulunduran listeyi ekrana yazdýrýn.

#     [(3, 4, 5), (6, 8, 10)]

#*** Not: filter() fonksiyonunu kullanmaya çalýþýn. ***

def IsTriangle(x,y,z):
    if x+y>z and x+z>y and z+y>x:
        return True
    else:
        return False

Ucgenler=[(3,4,5),(6,8,10),(3,10,7)]

gecerli_ucgenler = list(filter(lambda t: IsTriangle(t[0], t[1], t[2]), Ucgenler))

print(gecerli_ucgenler)