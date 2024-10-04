#�imdi de geometrik �ekil hesaplama i�lemi yapal�m. �lk olarak kullan�c�dan ��genin mi d�rtgenin mi tipini bulmak istedi�ini sorun
#E�er kullan�c� "D�rtgen" cevab�n� verirse , 4 tane kenar isteyip bu d�rtgenin kare mi , dikd�rtgen mi yoksa s�radan bir d�rtgen mi oldu�unu bulmaya �al���n.
#E�er kullan�c� "��gen" cevab�n� verirse , 3 tane kenar isteyip bu ��genin ikizkenar m� , e�kenar m� yoksa s�radan bir ��gen mi oldu�unu bulmaya �al���n.
#E�er verilen kenarlar bir ��gen belirtmiyorsa, ekrana "��gen belirtmiyor" �eklinde bir yaz� yaz�n
print("*************\n1-Dortgenin Cesidini Bulma\n2-Ucgenin Cesidini Bulma\n*************")
islem=(1,2)
secim=int(input("Isleminizi Secin {} {}: ".format(islem[0],islem[1])))
if secim==islem[0]:
    print("Dortgenin Kenarlarini Sirasiyla Giriniz")
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))
    d=float(input("d:"))
    #Girilen kenarlar� listeleme
    kenarlar=[a,b,c,d]
    #Girilen kenarlar� sortlama k���kten b�y��e
    kenarlar.sort()
    if a<0 or b<0 or c<0 or d<0:
        print("Negatif deger girdiniz!")
    elif kenarlar[0]==kenarlar[1] and kenarlar[2]==kenarlar[3] and kenarlar[0]==kenarlar[2]:
        print("Bu Bir Kare!")
    elif kenarlar[0]==kenarlar[1] and kenarlar[2]==kenarlar[3]:
        print("Bu Bir Dikdortgen")
    else:
        print("Bu Bir Normal Dortgen")
elif secim==islem[1]:
    print("Ucgenin Kenarlarini Sirasiyla Giriniz")
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))
    kenarlar=[a,b,c]
    kenarlar.sort()
    if a<0 or b<0 or c<0:
        print("Negatif deger girdiniz!")
    elif kenarlar[0]<kenarlar[1]+kenarlar[2] and kenarlar[1]<kenarlar[0]+kenarlar[2] and kenarlar[2]<kenarlar[0]+kenarlar[1]:
        if kenarlar[0]==kenarlar[1]==kenarlar[2]:
            print("Bu bir EskenarUcgen!")
        elif kenarlar[0]==kenarlar[1] or kenarlar[1]==kenarlar[2]:
            print("Bu bir IkizKenar!")
        else:
            print("Bu bir Cesitkenar!")
    else:
        print("Girdiginiz degerler bir ucgen belirtmez!!")
else:
    print("Yanlis Islem Girdiniz")