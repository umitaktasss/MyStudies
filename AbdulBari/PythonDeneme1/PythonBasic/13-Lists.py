# 1-Liste Olu�turma
# 2-Indeksleme ve Par�alama
# 3-Temel Liste Metodlar� ve ��lemleri
# 4-�� i�e listeler
#Liste Olu�turma [] listeler b�yle olu�turulabilir.
from ast import List
import pprint


Liste=["Iki ekmek", "Aldim", "Eve gidiyorum", "Death Claw lutfen pesimi birak!", 30, 40]
Liste2=[]
Liste3=list()
print(len(Liste))
Liste4=list("Merhaba")
print(Liste4)
print(len(Liste4))
#Indeksleme ve parcalama
liste5=[3,4,5,6,7,8,9,10]
print(liste5[2])
print(liste5[-1])
print(liste5[len(liste5)-1])
#par�alama
print(liste5[4:])
print(liste5[:2])
print(liste5[::3])
print(liste5[::-1])
#Temel liste metodlar� Listeler birbirine toplama i�lemi ger�ekle�tirebilir.
Liste_A=[1,2,3,4,5]
Liste_B=[6,7,8,9,10]
Liste_C=Liste_A+Liste_B
print(Liste_C)
Liste_A*=3
print(Liste_A)
#Listeler direkt olarak degistirilebilir
Liste_D=[5,6,7,25,23]
Liste_D[2]=10
print(Liste_D)
Liste_D[0:2]=[12,11]
print(Liste_D)
#methodlar append ekleme
Liste_D.append("Python")
print(Liste_D)
#pop eleman ��karma
Liste_D.pop(1)
print(Liste_D)
Liste_D.pop(-1)
#sort methoduyla direkt listeyi s�ralayabiliriz
Liste_D.sort()
print(Liste_D)
Liste_E=["Python","C","Java","C++"]
Liste_E.sort()
print(Liste_E)
Liste_E.sort(reverse=True)
print(Liste_E)
#i� i�e listeler
Liste_nested= [[1,2],[3,4],[5,6]]
print(Liste_nested[0][1])
