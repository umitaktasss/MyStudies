#Problem 4
#Elinizde isimlerin ve soyisimlerin bulundu�u iki tane liste olsun.

#        isimler -----> ["Kerim","Tar�k","Ezgi","Kemal","�lkay","��kran","Merve"]

#        soyisimler -----> ["Y�lmaz","�zt�rk","Da�deviren","Atat�rk","Dikmen","Kaya","Polat"]

#Bu isimleri ve soyisimleri s�ras�yla e�le�tirin ve ekrana alt alta isimleri ve soyisimleri yazd�r�n.

isimler=["Kerim","Tarik","Ezgi","Kemal","Ilkay","Sukran","Merve"]
soyisimler = ["Yilmaz","Ozturk","Dagdeviren","Ataturk","Dikmen","Kaya","Polat"]
print(list(zip(isimler,soyisimler)))
for i,j in zip(isimler,soyisimler):
    print(i,j)