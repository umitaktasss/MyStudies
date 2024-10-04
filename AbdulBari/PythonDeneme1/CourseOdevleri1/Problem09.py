#Kullanýcýnýn girdiði vize1,vize2,final notlarýna notlarýna göre harf notunu hesaplayýn.

#    Vize1 toplam notun %30'una etki edecek.

#    Vize2 toplam notun %30'una etki edecek.

#    Final toplam notun %40'ýna etki edecek.

vize1=int(input("Birinci Vize notunuzu giriniz:"))
vize2=int(input("Ikinci Vize notunuzu giriniz:"))
final=int(input("Final notunuzu giriniz:"))

GenelNot = vize1*0.3+vize2*0.3+final*0.4
HarfNotu=("AA","AB","BB","BC","CC","CD","DD","FF")
if vize1>=0 and vize2>=0 and final>=0 and vize1<=100 and vize2<=100 and final<=100:
    if GenelNot >= 90 and GenelNot <=100:
        print("Genel Notunuz {} ve Harf Notunuz {}".format(GenelNot,HarfNotu[0]))
    elif GenelNot >= 80 and GenelNot <90:
        print("Genel Notunuz {} ve Harf Notunuz {}".format(GenelNot,HarfNotu[1]))
    elif GenelNot >= 70 and GenelNot <80:
        print("Genel Notunuz {} ve Harf Notunuz {}".format(GenelNot,HarfNotu[2]))
    elif GenelNot >= 60 and GenelNot <70:
        print("Genel Notunuz {} ve Harf Notunuz {}".format(GenelNot,HarfNotu[3]))
    elif GenelNot >= 50 and GenelNot <60:
        print("Genel Notunuz {} ve Harf Notunuz {}".format(GenelNot,HarfNotu[4]))
    elif    GenelNot >= 55 and GenelNot <60:
        print("Genel Notunuz {} ve Harf Notunuz {}".format(GenelNot,HarfNotu[5]))
    elif GenelNot >= 50 and GenelNot <55:
        print("Genel Notunuz {} ve Harf Notunuz {}".format(GenelNot,HarfNotu[6]))
    else:
        print("Genel Notunuz {} ve Harf Notunuz {}\nKaldiniz!".format(GenelNot,HarfNotu[7]))
         
else:
    print("Yanlis vize veya final girdisi!")


