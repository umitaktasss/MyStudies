#Kullan�c�dan 3 tane say� al�n ve en b�y�k say�y� ekrana yazd�r�n.
a=int(input("Lutfen bir tam sayi degeri giriniz:"))
b=int(input("Lutfen bir tam sayi degeri giriniz:"))
c=int(input("Lutfen bir tam sayi degeri giriniz:"))
liste=[a,b,c]
liste.sort()
print("Girdiginiz En Buyuk sayi {}".format(liste[-1]))