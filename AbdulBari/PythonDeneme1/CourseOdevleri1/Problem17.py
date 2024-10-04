#Problem
#1'den 10'kadar olan sayýlarla ekrana çarpým tablosu bastýrmaya çalýþýn.
#Ýpucu: Ýç içe 2 tane for döngüsü kullanýn. Ayný zamanda sayýlarý range() fonksiyonunu kullanarak elde edin.

for i in range(1, 11):
    for j in range(1, 11):
        print("i: {} j: {} i*j: {}".format(i, j, i*j))
    print("\n")