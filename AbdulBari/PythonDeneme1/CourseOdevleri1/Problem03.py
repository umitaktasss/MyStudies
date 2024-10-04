#Bir aracýn kilometrede ne kadar yaktýðý ve kaç kilometre yol yaptýðý bilgilerini alýn, sürücünün toplam ne kadar ödemesi gerektiðini hesaplayýn.
yakilan=float(input("Araciniz Kilometrede ne kadar yakiyor? "))
km=float(input("Kac kilometre gittiniz? "))
odeme=yakilan*km
print("Odemeniz gereken {} Tl'dir.".format(odeme))