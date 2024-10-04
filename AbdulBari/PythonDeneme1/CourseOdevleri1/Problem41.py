#Problem 3
#Elinizde þöyle bir liste bulunsun.

#    [1,2,3,4,5,6,7,8,9,10]

#Bu listenin içindeki çift sayýlarýn toplamýný ekrana yazdýran bir fonksiyon yazýn.

#*Not: Ýlk önce filter() fonksiyonu ile çift sayýlarý ayýklayýn. Daha sonra reduce() fonksiyonunu kullanýn.*
from functools import reduce
def topla(x,y):
    return x+y
liste_A=[1,2,3,4,5,6,7,8,9,10]
liste_B=list(filter(lambda x: x % 2 ==0,liste_A ))
toplam=reduce(topla,liste_B)
print(liste_B,toplam,sep="/")
