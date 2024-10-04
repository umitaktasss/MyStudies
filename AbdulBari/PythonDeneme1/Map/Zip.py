#Zip fonksiyonunu görmeden önce 
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]
liste_str=["C++","Php","Python","Java","Html"]
#sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalýþalým


i=0
sonuc=list()

while(i<len(liste1) and i <len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i+=1
print(sonuc)
#Yukaridaki iþlemi daha rahat þekilde böyle yapabiliriz.
liste3=list(zip(liste1,liste2,liste_str))
print(liste3)

for i,j in zip(liste1,liste_str):
    print(i,j)