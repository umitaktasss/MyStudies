#Problem 4
#Her bir while d�ng�s�nde kullan�c�dan bir say� al�n ve kullan�c�n�n girdi�i say�lar� "toplam" isimli bir de�i�kene ekleyin. Kullan�c� "q" tu�una bast��� zaman d�ng�y� sonland�r�n ve ekrana "toplam de�i�kenini" bast�r�n.

#�pucu : while d�ng�s�n� sonsuz ko�ulla ba�lat�n ve kullan�c� q'ya basarsa d�ng�y� break ile sonland�r�n.*
#rint("""******************
#TOPLAMA PROGRAMI
#PROGRAMI SONLANDIRMAK ICIN '=' basiniz   
#******************      """)
#toplam=0
#print("Lutfen toplanmasini istediginiz sayilari sirasiyla giriniz:")
#i=1
#while True:
#    in_top=input("{}. sayi:".format(i))
#    if in_top=='=':
#        break
#    toplam+=int(in_top)
#    i+=1
#print("Girdiginiz Sayilarin Toplami: ",toplam)
print("""******************
TOPLAMA PROGRAMI
PROGRAMI SONLANDIRMAK ICIN '=' basiniz   
******************""")

sayilar = []

print("Lutfen toplanmasini istediginiz sayilari sirasiyla giriniz:")
while True:
    in_top = input("Sayi girin ('=' icin bitirin): ")
    if in_top == '=':
        break
    sayilar.append(int(in_top))

toplam = sum(sayilar)
print("Girdiginiz sayilar:", sayilar)
print("Toplam:", toplam)
    
        
    
    