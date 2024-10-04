#Problem 4
#Kullanýcýdan 2 basamaklý bir sayý alýn ve bu sayýnýn okunuþunu bulan bir fonksiyon yazýn.

#Örnek: 97 ---------> Doksan Yedi
birler=["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
def okunus(sayi):
    a=sayi // 10 # onlar basamagi
    b=sayi % 10 #birler basamagi
    return onlar[a] + " " + birler[b]

sayi = int(input("Sayi:"))
print(okunus(sayi))


    