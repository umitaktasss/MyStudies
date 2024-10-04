#Problem 4
#Elinizde isimlerin ve soyisimlerin bulunduðu iki tane liste olsun.

#        isimler -----> ["Kerim","Tarýk","Ezgi","Kemal","Ýlkay","Þükran","Merve"]

#        soyisimler -----> ["Yýlmaz","Öztürk","Daðdeviren","Atatürk","Dikmen","Kaya","Polat"]

#Bu isimleri ve soyisimleri sýrasýyla eþleþtirin ve ekrana alt alta isimleri ve soyisimleri yazdýrýn.

isimler=["Kerim","Tarik","Ezgi","Kemal","Ilkay","Sukran","Merve"]
soyisimler = ["Yilmaz","Ozturk","Dagdeviren","Ataturk","Dikmen","Kaya","Polat"]
print(list(zip(isimler,soyisimler)))
for i,j in zip(isimler,soyisimler):
    print(i,j)