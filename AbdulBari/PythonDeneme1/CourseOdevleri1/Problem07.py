#Kullan�c�dan al�nan boy ve kilo de�erlerine g�re beden kitle indeksini hesaplay�n ve �u kurallara g�re ekrana �u yaz�lar� yazd�r�n.
#BK� 18.5'un alt�ndaysa -------> Zay�f

#BK� 18.5 ile 25 aras�ndaysa ------> Normal

#BK� 25 ile 30 aras�ndaysa --------> Fazla Kilolu

#BK� 30'un �st�ndeyse -------------> Obez
kilo=float(input("Lutfen kilogram cinsinden kilonuzu giriniz:"))
boy=float(input("Lutfen boyunuzu metre cinsinden giriniz:"))
indeks=kilo/(boy**2)
List1=("Zayif","Normal","Fazla Kilolu", "Obez")


if kilo>0 and boy>0 and boy<2.55:
    if indeks<18.5:
        print("Kilo: {}\nBoy: {}\nIndeks: {}\nDurum: {}".format(kilo,boy,indeks,List1[0]))
    elif indeks>=18.5 and indeks<25:
        print("Kilo: {}\nBoy: {}\nIndeks: {}\nDurum: {}".format(kilo,boy,indeks,List1[1]))
    elif indeks>=25 and indeks<30:
        print("Kilo: {}\nBoy: {}\nIndeks: {}\nDurum: {}".format(kilo,boy,indeks,List1[2]))
    elif indeks>=30:
        print("Kilo: {}\nBoy: {}\nIndeks: {}\nDurum: {}".format(kilo,boy,indeks,List1[3]))
else:
    print("Yanlis boy veya kilo girdisi!")