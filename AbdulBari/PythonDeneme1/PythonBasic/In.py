#In operatörü in operatörüyle bir elemanýn baþka bir listede demetle veya stringte bulunup bulunmadýðý kontrol edilir
print("a" in "merhaba")
print(1 in [1,2,3,4])
#for dongüsü
#for eleman in veri_yapýsý(liste,demet,vs):
#yapýlacak iþlemler
liste=[1,2,3,4,5,6,7,34,54,63,78]
for eleman in liste:
    print(eleman)
toplam=0
for eleman in liste:
    toplam=toplam+eleman
    print("Toplam: {} Eleman: {}".format(toplam,eleman))
for eleman in liste:
    if eleman % 2 == 0:
     print(eleman)

#String
s="Python"
for i in s:
   print(i*3)
#demetler içerisinde gezinme
demet=(1,2,3,4,5)
for a in demet:
   print(a)
liste1=[(1,2),(3,4),(5,6),(7,8)]
for eleman in liste1:
   print(eleman)
for (i,j) in liste1:
   print("i: {} j: {}".format(i,j))
#Sozlukler üzerinde gezinmek
sozluk={"bir":1,"iki":2,"uc":3,"dort":4}
print("\n",sozluk.keys(),"\n",sozluk.values(),"\n",sozluk.items())
for eleman in sozluk.values():
   print(eleman)
for i,j in sozluk.items():
   print("Anahtar:",i,"Deger:",j)