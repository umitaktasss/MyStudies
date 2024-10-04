#Kullanýcýdan bir dik üçgenin dik olan iki kenarýný(a,b) alýn ve hipotenüs uzunluðunu bulmaya çalýþýn.

#Hipotenüs Formülü: a^2 + b^2 = c^2
print("\t****Dik Ucgenin Hipotenusunu Bulma****")
a=float(input("Lutfen Ucgenin dik kenarlarindan birini giriniz:"))
b=float(input("Lutfen Ucgenin diger dik kenarini giriniz:"))
hip=(a ** 2 + b ** 2) ** 0.5
print("Hipotenus {}".format(hip))