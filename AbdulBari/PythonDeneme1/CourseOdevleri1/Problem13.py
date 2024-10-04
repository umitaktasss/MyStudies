#Bir Sayinin Faktoriyelini Bulma 5*4*3*2*1> sayilarin çarpýmý
print("*********\nBasit Faktoriyel Alma Islemine Hos geldiniz.\nCikis Yapmak Icin negatif bir deger giriniz\n\n*********")
while True:
   
    faktoriyel_in=int(input("Lutfen Faktoriyeli Alinmasi Istediginiz Sayiyi Giriniz:"))
    if(faktoriyel_in==0 or faktoriyel_in==1):
        print("Sonucunuz: 1")
        continue
    elif(faktoriyel_in<0):
        print("Cikis isleminiz gerceklestiriliyor...")
        break
    i=1
    faktoriyelhesap=1
    for i in range(1,faktoriyel_in+1):
     faktoriyelhesap*=i
    print("{} ! = {}".format(faktoriyel_in,faktoriyelhesap))
   
   