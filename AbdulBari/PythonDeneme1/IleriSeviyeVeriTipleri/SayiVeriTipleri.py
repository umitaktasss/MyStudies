#Bazen proglamada sayýlarýmýzý 10'luk taban haricinde 2'lik (binary) ve 16'lýk (hexadeciaml) tabanda göstermek ve kullanmak isteyebiliriz
a=bin(23)
print(a) # 
print(hex(20)) # 0*14 yani 16^0*4+16^1*1=20
print(hex(512))
#abs fonksiyonu
#bir sayýnýn mutlak degerini almamizi saðlar
print(abs(-65.31))
#round fonksiyonu
#sayýlarý alta veya üste yuvarlar
print(round(5.3),round(2.9))
print(round(3.2266,3))
#max min
print(max(3,4,5,6,7,-2,22))
print(min(3,4,5,6,7,-2,22))
#sum fonksiyonu verilen degerleri toplayarak döndürür. Deðerlerin liste,demet vb. þeklinde verilmesi lazým

print(sum([3,4,5,6,7,8]))
print(sum((3,4)))
#pow üs alma iþlemlerinde kullanýlýr
print(pow(5,3))
