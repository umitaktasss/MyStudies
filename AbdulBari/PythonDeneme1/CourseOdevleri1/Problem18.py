#Problem 4
#Her bir while döngüsünde kullanýcýdan bir sayý alýn ve kullanýcýnýn girdiði sayýlarý "toplam" isimli bir deðiþkene ekleyin. Kullanýcý "q" tuþuna bastýðý zaman döngüyü sonlandýrýn ve ekrana "toplam deðiþkenini" bastýrýn.

#Ýpucu : while döngüsünü sonsuz koþulla baþlatýn ve kullanýcý q'ya basarsa döngüyü break ile sonlandýrýn.*
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
    
        
    
    