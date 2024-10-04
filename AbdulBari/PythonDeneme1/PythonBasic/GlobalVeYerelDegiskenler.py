# yerel ve global degiskenler
# yerel degiskenler fonksiyonlar icerisinde bulunur ve tanımlanıp daha sonra bellekten silinir.
def sayi():
    a=10            #yerel degisken 
    print(a) 
sayi() #yerel degisken kullanıldı ve atıldı
#print(a) #Boyle bir degisken yok, yerel degisken yok oldu!
#Global degiskenler en kapsamli degiskenler olarak adlandırılır tanımlandıktan sonra her yerden erişebiliriz.
b=5 #global degisken
def fonksiyon():
    print(b)   # fonksiyon icerisinde kullanabilirim.
    
fonksiyon()
#b=5 olsaydi hata!
#degiskenler fonksiyon cagrisi yapilmadan önce atanmalidir!!
def fonksiyon1():
    b=3
    print(b)

fonksiyon1() # 3 fonksiyon icerisinde yerel olarak 3 tanımlandı ve daha sonra deger yok oldu
print(b) # global deger 5 olarak ekranda görüntülenecek

def fonksiyon2():
    global b   #b degerimiz artık global olarak ayarlandi yani sonraki alinacak degerde yok olup atılmayacak,degisken olarak kaydedilecek
    b=2
    print(b)

fonksiyon2()
print(b)


