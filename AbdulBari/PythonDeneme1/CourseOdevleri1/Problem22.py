def tamBolen(sayi):
    tam_bolenler=[]
    
    for i in range(2,(sayi//2)+1):
        if sayi % i ==0:
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi=input("Lutfen sayinizi girin: ")
    if sayi=='*':
        print("Programdan cikis yapiliyor...")
        break
    else:
        sayi=int(sayi)
       
        print("Tam bolenler: ", tamBolen(sayi))
    