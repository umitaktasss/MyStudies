#Kullanýcý giriþi giriþ hakký 3 veya çýkmak istediðinde çýkacak veya doðru girdiðince döngü bitecek
kullanici_Adi="Umit123a"
sifre="Admin123"
i=3
while True:
    print("****Hos Geldiniz**** Cikmak icin * basiniz.")
    kullanici_Adi_In=input("Lutfen Kullanici Adinizi Giriniz:")
    if kullanici_Adi_In=='*':
        print("Cikis isleminiz gerceklestiriliyor ....")
        break

    sifre_In=input("Lutfen Sifrenizi Giriniz:")
    
    if(kullanici_Adi_In!=kullanici_Adi or sifre_In!=sifre):
        i-=1
        print("Kullanici adiniz veya sifreniz yanlis! Giris icin {} hakkiniz kaldi!".format(i))
        if i==0:
            break
    else:
        print("Hos geldiniz.")
        break