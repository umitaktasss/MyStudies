#Burada yapaca��m�z i�lem i�in basit bir fonksiyonu ele alal�m.

from email import iterators


def kareleri_al():
    kareler=[]
    for i in range(1,6):
        kareler.append(i**2)
        
    return kareler

print(kareleri_al())

#Yukar�da g�rd���m�z durum i�in az say�da say�lar�n karesini al�p bir listede saklamak mant�kl� g�r�nebilir ama �ok y�ksek say�larda say�lar i�in bunu yapmak mant�kl� de�il.
#O y�zden generatorlere bi g�z atal�m.
#De�erlerimiz hen�z �retilmedi.
def kareleri_al2():
    for i in range(1,6):
        yield i**2
#Fonksiyon �a��rlmas�na ra�men �retilmedi.        
generator=kareleri_al2()
print(generator)
#DE�ERE ULA�MAK �STED���M�ZDE �RET�LECEK!
iterator=iter(generator)
#De�er �retildi ve serbest b�rak�ld�!
print(next(iterator))
print(next(iterator))
#List comph generatore �evirme

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