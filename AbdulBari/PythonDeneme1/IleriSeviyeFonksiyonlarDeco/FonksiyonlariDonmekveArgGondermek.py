#Fonksiyonlarý return ile dönmek

def anafonksiyon(islem_adi):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam
    
    def carpim(*args):
        carpim=1
        for i in args:
            carpim*=i 
        return carpim
    
    if islem_adi == "toplama":
        return toplama
    else:
        return carpim
    

fonk = anafonksiyon("toplama")

print(fonk)

print(fonk(1,2,3,4,5,6,7))
fonk2=anafonksiyon("carpim")

print(fonk2(1,2,3,4,5,6,7))

def toplama1(a,b):
    return a+b
def cikarma1(a,b):
    return a-b
def carpma1(a,b):
    return a*b
def bolme(a,b):
    return a / b

def anafonksiyon(func1, func2, func3, func4, islem_adi):
    if (islem_adi=="toplama"):
        print(func1(10,5))
    elif(islem_adi=="cikarma"):
        print(func2(6,3))
    elif(islem_adi=="carpma"):
        print(func3(8,3))
    elif(islem_adi=="bolme"):
        print(func4(8,2))
    else:
        print("Hatali islem!")
        

anafonksiyon(toplama1,cikarma1,carpma1,bolme,"cikarma")
anafonksiyon(toplama1,cikarma1,carpma1,bolme,"bolme")