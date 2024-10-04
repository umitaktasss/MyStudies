def selamla():
    print("Hadi hadi python temeli bitecek daha ogrenmen gereken daha coook sey var")
    print("Helal len sanaaa")





selamla()
def selamla1(name):
    print("{} bu isi yapiyor".format(name))



selamla1("Umit")
def faktoriyel(sayi):
    faktoriyel=1
    if (sayi==0 or sayi ==1):
        print("Faktoriyel: 1")
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi-=1
    print("Faktoriyel", faktoriyel)


faktoriyel(5)
faktoriyel(7)
faktoriyel(12)