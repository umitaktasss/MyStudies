#Kullanýcýdan alýnan boy ve kilo deðerlerine göre beden kitle indeksini hesaplayýn ve þu kurallara göre ekrana þu yazýlarý yazdýrýn.
#BKÝ 18.5'un altýndaysa -------> Zayýf

#BKÝ 18.5 ile 25 arasýndaysa ------> Normal

#BKÝ 25 ile 30 arasýndaysa --------> Fazla Kilolu

#BKÝ 30'un üstündeyse -------------> Obez
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