#Buradaki problemin ��z�m�n� derslerimizde �zellikle ��renmedik. 
#Burada mant�k y�r�terek ve list comprehension kullanarak 1'den 100'e kadar olan say�lardan sadece �ift say�lar� bir listeye atmay� yapmay� �al���n.
cift_sayilar = [x for x in range(1, 101) if x % 2 == 0]
print(cift_sayilar)