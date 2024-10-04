#Hata yakalamyý öðrenmeden önce hatalari taniyalim
#print(a) Tanýmli deðil Name Error!
#int("sdsds3432") # Value Error
#2/0 ZeroDivisionError
#print("Musttfo'sdsdsds) Syntax Error
#Try,except,Finally


# Try:
#  Hata Çikarabilecek kodlar buraya yaziliyor
# Eðer hata çýkarsa program uygun olan except bloðuna girecek
# Hata oluþursa try bloðunun geri kalanýndaki iþlemler çalýþmayacak
# except Hata1:
#   Hata 1 oluþtugunda burasý çalýsacak
# except Hata2:
#   Hata 2 oluþtuðunda burasý çalýþacak
# finally:
# Mutlaka çalýþmasý gereken kodlar bu bloða yazýlýr
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


    