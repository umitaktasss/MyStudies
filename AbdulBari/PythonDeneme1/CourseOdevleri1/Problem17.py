#Problem
#1'den 10'kadar olan say�larla ekrana �arp�m tablosu bast�rmaya �al���n.
#�pucu: �� i�e 2 tane for d�ng�s� kullan�n. Ayn� zamanda say�lar� range() fonksiyonunu kullanarak elde edin.

for i in range(1, 11):
    for j in range(1, 11):
        print("i: {} j: {} i*j: {}".format(i, j, i*j))
    print("\n")