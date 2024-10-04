#Kullanicidan alinan boy ve kilo degerlerine göre kullanicinin beden kitle indeksini bulma beden kitle indeksi: Kilo/Boy(m)
kilo=float(input("Lutfen kilogram cinsinden kilonuzu giriniz:"))
boy=float(input("Lutfen boyunuzu metre cinsinden giriniz:"))
indeks=kilo/(boy**2)

print("Boy kilo endeksiniz: {}".format(indeks))