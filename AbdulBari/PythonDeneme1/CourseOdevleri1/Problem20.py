#Buradaki problemin çözümünü derslerimizde özellikle öðrenmedik. 
#Burada mantýk yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayýlardan sadece çift sayýlarý bir listeye atmayý yapmayý çalýþýn.
cift_sayilar = [x for x in range(1, 101) if x % 2 == 0]
print(cift_sayilar)