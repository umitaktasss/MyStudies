#Atm programý
print("""*********************
Atm Makinesine Hosgeldiniz.
Islemler;
1. Bakiye Sorgulama
2. Para Yatirma
3. Para cekme    
Programdan cikmak icin  '*' tusuna basin.
******************      """)
Bakiye_a=1550.0
while True:
    islem=0
    secim_in=input("Lutfen Seciminizi Yapin: ")
    if secim_in=="1":
        print("Suanki Guncel Bakiyeniz: {}".format(Bakiye_a))
    elif secim_in=="2":
        islem=float(input("Yatirmak istediginiz tutari giriniz: "))
        Bakiye_a+=islem
        print("Guncel Bakiyeniz: {} TL'dir".format(Bakiye_a))
    elif secim_in=="3":
        islem=float(input("Cekmek istediginiz tutari giriniz: "))
        if islem>Bakiye_a and islem >= 0:
            print("Cekmek istediginiz Tutar Guncel Bakiyenizden buyuk olamaz!")
        else:
            Bakiye_a-=islem
        print("Guncel Bakiyeniz: {} TL'dir".format(Bakiye_a))
    elif secim_in=="*":
        print("Cikis isleminiz gerceklestiriliyor... \n Iyi gunler dileriz...")
        break
    else:
        print("Yanlis islem sectiniz...")
            
    
        
