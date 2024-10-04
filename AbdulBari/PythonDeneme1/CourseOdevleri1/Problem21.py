#Asal sayilari bulma fonksiyonu
#def asalSayi(a):
#    sayac=0
#    if a==1 or a<0:
#            print("Girdiginiz Sayi Asal Sayi belirtmez!")
#    else:
#        for i in range(1,(a//2)+1):
        
        
#            if a % i ==0:
#                sayac+=1
#                if sayac >1:
#                    print("Sayi Asal degildir!")
#                else:
#                    print("Sayi Asaldir!")


#asalSayi(3)
#asalSayi(2)
#asalSayi(1)
#asalSayi(-1)
#asalSayi(5)
#asalSayi(4)
#asalSayi(6)
#asalSayi(97)
def asalSayi_mi(sayi):
    if sayi==1:
         return False
    elif sayi==2:
        return True
    else:
        for i in range(2,int((sayi//2))+1):
            if sayi % i == 0:
               return False
        return True

print("Cikis icin * basiniz")
while True:
    girdi=input("Lutfen sayiyi giriniz:")
    
    if girdi=='*':
        break
    else:
        if asalSayi_mi(int(girdi)):
            print(girdi," sayisi asaldir")
        else:
            print(girdi," Bu sayi asal degildir!")