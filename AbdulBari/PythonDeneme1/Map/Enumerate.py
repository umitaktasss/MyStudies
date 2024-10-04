#Enumerate fonksiyonunu anlamak için
liste=["Elma","Armut","Muz","Kiraz"]
#sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz
sonuc=list()
i=0
for a in liste:
    sonuc.append((i,a))
    i+=1
print(sonuc)
liste_a=list(enumerate(liste))
print(liste_a)
#indeks numarası çift olanları ekrana bastırma
for i,j in enumerate(liste):
    if(i%2==0):
        print(j)