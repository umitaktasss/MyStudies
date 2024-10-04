# return ifadesi fonksiyonlarda elde ettiðimiz deðeri bir deðiþkende depolayabilir ve bu deðiþkeni farklý yerlerde kullanabiliriz.
def toplama(a,b,c):
    return a+b+c
def ikiylecarp(a): 
    return a*2

toplam=toplama(3,5,7)
print(ikiylecarp(toplam))
def selamla(ad="Isimsiz"):
    print("Selamlar: ", ad)
    

selamla()
def bilgilerigoster (ad="null",soyad="null",numara="null"):
    print("Ad: {} \nSoyad: {} \nNumara: {}".format(ad, soyad, numara))


bilgilerigoster('Ahmet','Ali',211554001)
bilgilerigoster()
#esnek sayida degerler
#def toplam(a,b,c):
#    print(a+b+c)

#toplam(5,7,8)
# error! toplam(5,7,8,11)
def toplam(*a):
    toplam=0
    print(a)
    for i in a:
        toplam+=i
     
    print(toplam)
        
#tupplelar içerisinde tutuldu
toplam(3,4,5,6,8)
toplam(1,2,3)


