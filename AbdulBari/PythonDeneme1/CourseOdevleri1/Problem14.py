#Fibbonaci Serisi
print("""*******************     
Fibbonaci Dizisinin Terimlerini Bulma
Cikmak icin negatif bir deger giriniz.      
*******************    """)

while True:
    fibborange=int(input("Lutfen Dizinin Kacinci Elemanini Bulmak Istediginizi Giriniz:"))
    if fibborange <0:
        print("Negatif bir deger girdiniz. Cikis yapiliyor...")
        break
    fibbo=[]
    if fibborange==0 or fibborange==1:
        print("Sonuc: 1")
    fibbo.append(1)
    fibbo.append(1)
    for i in range(2,fibborange):
        fibbo.append(fibbo[i-1]+fibbo[i-2])
    print("Sonuc: ", fibbo[-1])
# baþka bir sonuc 
# a = 1
# b = 1
# fibonacci = [a, b]

# for i in range(20):
 #   a, b = b, a + b
 #   fibonacci.append(b)

# print(fibonacci)

