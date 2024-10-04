#sözlükler anahtar(key), deðer(value) olarak tutulur. gerçek hayattaki sözlüklere benziyor.
sozluk={"bir":1,"iki":2,"uc":3,"dort":4}
print(sozluk,type(sozluk))
sozluk1={}
sozluk2=dict()
print(sozluk["bir"]+sozluk["dort"])
#Eleman ekleyebiliriz.
sozluk["Bes"]=5
print(sozluk)
a={"bir":[1,2,3,4,5],"iki":[[1,2],[3,4],[5,6]],"uc":15}
print(a["iki"][1])
sozluk["Bes"]=10 #yeni sozluk degeri Bes için 10
#ic ice sozlukler
b={"sayilar":{"bir":1,"iki":2,"uc":3},"meyveler":{"kiraz":"yaz","portakal":"kis","erik":"yaz"}}
print(b["sayilar"]["iki"],b["meyveler"]["kiraz"])
print(b.keys())
print(b.values())
print(b.items())
                                                             