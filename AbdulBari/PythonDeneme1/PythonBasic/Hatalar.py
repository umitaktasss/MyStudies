#Hata yakalamy� ��renmeden �nce hatalari taniyalim
#print(a) Tan�mli de�il Name Error!
#int("sdsds3432") # Value Error
#2/0 ZeroDivisionError
#print("Musttfo'sdsdsds) Syntax Error
#Try,except,Finally


# Try:
#  Hata �ikarabilecek kodlar buraya yaziliyor
# E�er hata ��karsa program uygun olan except blo�una girecek
# Hata olu�ursa try blo�unun geri kalan�ndaki i�lemler �al��mayacak
# except Hata1:
#   Hata 1 olu�tugunda buras� �al�sacak
# except Hata2:
#   Hata 2 olu�tu�unda buras� �al��acak
# finally:
# Mutlaka �al��mas� gereken kodlar bu blo�a yaz�l�r
from typing import final


try:
    a= int("323243")
    print("Program Burada")
except :
    print("Bir hata olustu")
print("Bloklar bitti")
try:
    b= int("sdsdsdsds23243")
    print("Program Burada")
except ValueError:
    print("Bir hata olustu")
print("Bloklar bitti")



try:
    sayi=int(input("Sayi1:"))
    sayi2=int(input("Sayi2:"))
    bolme=sayi/sayi2
    print(bolme)
except ZeroDivisionError:
    print("Bir Sayi Sifira Bolunemez!")
except ValueError:
    print("Gecerli Bir Sayi Giriniz!")
finally:
    print("Burasi Calisti")
print("Bloklar Bitti")

#Hata Firlatmak
#Kendi Hatalarimizi yazma
def tercevir(s):
        if(type(s)!=str):
            raise ValueError("Lutfen bir string Deger Giriniz!")
        else:
            return s[::-1]

print(tercevir("Python"))
try:
    print(tercevir(11))
except ValueError:
    print("Fonksiyon Hata Verdri!")


    