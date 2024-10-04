#Basit Hesap Makinesi
print("***Hos geldiniz***")
a=float(input("Lutfen Bir Sayi Giriniz:"))
b=float(input("Lutfen Bir Sayi Giriniz:"))
islem=("*","/","-","+")
kislem=input("Yapmak istediginiz islemi seciniz {} {} {} {} :".format(islem[0],islem[1],islem[2],islem[3]))


if kislem==islem[0]:
    carpim=a*b
    print("{} * {} = {}".format(a,b,carpim))
elif kislem==islem[1]:
    bolum=a/b
    print("{} / {} = {}".format(a,b,bolum))
elif kislem==islem[2]:
    fark=a-b
    print("{} - {} = {}".format(a,b,fark))
elif kislem==islem[3]:
    toplam=a+b
    print("{} + {} = {}".format(a,b,toplam))
else:
    print("Yanlis girdi!")    