#Kullan�c�dan bir dik ��genin dik olan iki kenar�n�(a,b) al�n ve hipoten�s uzunlu�unu bulmaya �al���n.

#Hipoten�s Form�l�: a^2 + b^2 = c^2
print("\t****Dik Ucgenin Hipotenusunu Bulma****")
a=float(input("Lutfen Ucgenin dik kenarlarindan birini giriniz:"))
b=float(input("Lutfen Ucgenin diger dik kenarini giriniz:"))
hip=(a ** 2 + b ** 2) ** 0.5
print("Hipotenus {}".format(hip))