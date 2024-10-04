#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
a=int(input("Lutfen bir tam sayi degeri giriniz:"))
b=int(input("Lutfen bir tam sayi degeri giriniz:"))
c=int(input("Lutfen bir tam sayi degeri giriniz:"))
liste=[a,b,c]
liste.sort()
print("Girdiginiz En Buyuk sayi {}".format(liste[-1]))