#Sys.exit
#Bu fonksiyon �al��an 
#python program�n� sonland�r�r.

import sys

#a = int(input("a: "))
#b= int(input("b: "))

#sys.exit()
#Buradaki komut �al��mayacakt�r.
#c= int(input("c: "))

#stderr stdout
#Bilgisayarlar i�lemlerimiz i�in �al��t��� zaman ��kt� vermek ve girdi almak i�in �u dosyalar� kullan�r.
#stdin: i�lemimizin kullan�c�dan input almas�n� sa�lar.
#stdout i�lemimizin ��kt� vermesini sa�lar
#stderr bu standart dosya, i�lemimizin hata mesajlar�n� ��kt� olarak vermek i�in kullan�l�r.
#print() fonksiyonu kulland���m�zda asl�nda standart stdout kullan�lmaktad�r.

sys.stderr.write("Bu bir hata mesajidir.\n")

sys.stderr.flush()

sys.stdout.write("Bu normal bir yazidir.\n")

for i in sys.argv:
    print(i)