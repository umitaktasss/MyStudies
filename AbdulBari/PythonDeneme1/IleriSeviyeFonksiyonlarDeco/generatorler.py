#Burada yapacaðýmýz iþlem için basit bir fonksiyonu ele alalým.

from email import iterators


def kareleri_al():
    kareler=[]
    for i in range(1,6):
        kareler.append(i**2)
        
    return kareler

print(kareleri_al())

#Yukarýda gördüðümüz durum için az sayýda sayýlarýn karesini alýp bir listede saklamak mantýklý görünebilir ama çok yüksek sayýlarda sayýlar için bunu yapmak mantýklý deðil.
#O yüzden generatorlere bi göz atalým.
#Deðerlerimiz henüz üretilmedi.
def kareleri_al2():
    for i in range(1,6):
        yield i**2
#Fonksiyon çaðýrlmasýna raðmen üretilmedi.        
generator=kareleri_al2()
print(generator)
#DEÐERE ULAÞMAK ÝSTEDÝÐÝMÝZDE ÜRETÝLECEK!
iterator=iter(generator)
#Deðer üretildi ve serbest býrakýldý!
print(next(iterator))
print(next(iterator))
#List comph generatore çevirme

listeA= [i*3 for i in range(5)]

generator2= (i*3 for i in range(5))

iterator2=iter(generator2)

print(next(iterator2))

def carpim_tablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield f"{i} x {j} = {i*j}"
            
for i in carpim_tablosu():
    print(i)