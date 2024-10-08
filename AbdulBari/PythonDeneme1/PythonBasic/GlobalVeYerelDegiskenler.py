# yerel ve global degiskenler
# yerel degiskenler fonksiyonlar icerisinde bulunur ve tan�mlan�p daha sonra bellekten silinir.
def sayi():
    a=10            #yerel degisken 
    print(a) 
sayi() #yerel degisken kullan�ld� ve at�ld�
#print(a) #Boyle bir degisken yok, yerel degisken yok oldu!
#Global degiskenler en kapsamli degiskenler olarak adland�r�l�r tan�mland�ktan sonra her yerden eri�ebiliriz.
b=5 #global degisken
def fonksiyon():
    print(b)   # fonksiyon icerisinde kullanabilirim.
    
fonksiyon()
#b=5 olsaydi hata!
#degiskenler fonksiyon cagrisi yapilmadan �nce atanmalidir!!
def fonksiyon1():
    b=3
    print(b)

fonksiyon1() # 3 fonksiyon icerisinde yerel olarak 3 tan�mland� ve daha sonra deger yok oldu
print(b) # global deger 5 olarak ekranda g�r�nt�lenecek

def fonksiyon2():
    global b   #b degerimiz art�k global olarak ayarlandi yani sonraki alinacak degerde yok olup at�lmayacak,degisken olarak kaydedilecek
    b=2
    print(b)

fonksiyon2()
print(b)


