#Problem 4
#Kullan�c�dan 2 basamakl� bir say� al�n ve bu say�n�n okunu�unu bulan bir fonksiyon yaz�n.

#�rnek: 97 ---------> Doksan Yedi
birler=["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
def okunus(sayi):
    a=sayi // 10 # onlar basamagi
    b=sayi % 10 #birler basamagi
    return onlar[a] + " " + birler[b]

sayi = int(input("Sayi:"))
print(okunus(sayi))


    