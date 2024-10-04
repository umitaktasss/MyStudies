#arg ifadesiyle istedigimiz kadar argüman gönderebiliriz.
#Demet halinde for döngüsü içinde gezinebiliriz.
#Dinamik arguman
def fonksiyon(*args):
    for i in args:
        print(i)

#Istedigimiz sayida arguman gönderebiliriz.
fonksiyon(1,2,3,4,5)

fonksiyon(1,2,3,'b',31,33,3)

def fonksiyon2(isim,*args):
    print("\nIsim: ", isim)
    print("-------------")
    for i in args:
        print(i)


fonksiyon2("Murat",1,2,3,4,5,6,8)

#**kwargs ifadesi bir dic görevi görür.
#Bir fonksiyona esnek sayýda anahtar-deðer çifti göndermeye yarar.

def bilgiler(**kwargs):
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")
        
bilgiler(isim="Ahmet", yas=25, sehir="Istanbul")

def fonksiyon3(*args,**kwargs):
    for i in args:
        print(i)
        
    print("----------------")
    
    for anahtar, deger in kwargs.items():
        print(f"{anahtar} {deger}")


fonksiyon3(33,35,98,66,isim="Umit",soy_isim="Aktas",numara=2111504057)