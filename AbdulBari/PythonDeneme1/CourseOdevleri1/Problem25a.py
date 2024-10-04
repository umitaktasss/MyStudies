def okunus2basamak(sayi):
    a=sayi // 10  #96 / 10 = 9, onlar basamagi 
    b=sayi % 10   # 96 %10 =6 birler basamagi
    Okunus=[a,b]
    if Okunus[0]==9:
        print("Doksan ",end='')
    elif Okunus[0]==8:
        print("Seksen ",end='')
    elif Okunus[0]==7:
        print("Yetmis ",end='')
    elif Okunus[0]==6:
        print("Altmis ",end='')
    elif Okunus[0]==5:
        print("Elli ",end='')
    elif Okunus[0]==4:
        print("Kirk ",end='')
    elif Okunus[0]==3:
        print("Otuz ",end='')
    elif Okunus[0]==2:
        print("Yirmi ",end='')
    elif Okunus[0]==1:
        print("On ",end='')
    else:
        print("Bu sayi ikis basamakli degildir!")
    if Okunus[1]==9:
        print("Dokuz")
    elif Okunus[1]==8:
        print("Sekiz")
    elif Okunus[1]==7:
        print("Yedi")
    elif Okunus[1]==6:
        print("Alti")
    elif Okunus[1]==5:
        print("Bes")
    elif Okunus[1]==4:
        print("Dort")
    elif Okunus[1]==3:
        print("Uc")
    elif Okunus[1]==2:
        print("Iki")
    elif Okunus[1]==1:
        print("Bir")
    elif Okunus[1]==0:
        print()
    else:
        print("Bu sayi ikis basamakli degildir!")