#Problem 5
#1'den 100'e kadar olan say�lardan sadece 3'e b�l�nen say�lar� ekrana bast�r�n. Bu i�lemi *continue* ile yapmaya �al���n.

for i in range(1,101):
    if i % 3 != 0:
        continue
    else:
        print(i)