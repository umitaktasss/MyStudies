#Problem 3
#Elinizde ��yle bir liste bulunsun.

#    [1,2,3,4,5,6,7,8,9,10]

#Bu listenin i�indeki �ift say�lar�n toplam�n� ekrana yazd�ran bir fonksiyon yaz�n.

#*Not: �lk �nce filter() fonksiyonu ile �ift say�lar� ay�klay�n. Daha sonra reduce() fonksiyonunu kullan�n.*
from functools import reduce
def topla(x,y):
    return x+y
liste_A=[1,2,3,4,5,6,7,8,9,10]
liste_B=list(filter(lambda x: x % 2 ==0,liste_A ))
toplam=reduce(topla,liste_B)
print(liste_B,toplam,sep="/")
