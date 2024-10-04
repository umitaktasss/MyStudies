#Sys.exit
#Bu fonksiyon çalýþan 
#python programýný sonlandýrýr.

import sys

#a = int(input("a: "))
#b= int(input("b: "))

#sys.exit()
#Buradaki komut çalýþmayacaktýr.
#c= int(input("c: "))

#stderr stdout
#Bilgisayarlar iþlemlerimiz için çalýþtýðý zaman çýktý vermek ve girdi almak için þu dosyalarý kullanýr.
#stdin: iþlemimizin kullanýcýdan input almasýný saðlar.
#stdout iþlemimizin çýktý vermesini saðlar
#stderr bu standart dosya, iþlemimizin hata mesajlarýný çýktý olarak vermek için kullanýlýr.
#print() fonksiyonu kullandýðýmýzda aslýnda standart stdout kullanýlmaktadýr.

sys.stderr.write("Bu bir hata mesajidir.\n")

sys.stderr.flush()

sys.stdout.write("Bu normal bir yazidir.\n")

for i in sys.argv:
    print(i)