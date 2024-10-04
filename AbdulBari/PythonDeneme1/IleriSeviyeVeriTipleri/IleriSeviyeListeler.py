#Listelerde en çok kullanýlan metodlar

liste = [1,23,34,44]
#Eleman ekleme
liste.append(31)

liste_2=[0,10,20,30]

#Liste_2yi liste ile birleþtirir. (geniþletir)
liste.extend(liste_2)

#Ýnsert methoduyla indeksleme yapýlabilir

liste.insert(2,"Piton")

#Pop metoduyla eleman çýkartabiliriz. (en son eleman)

liste.pop()
#2. indeksteki eleman çýkarýlýcak
liste.pop(2)

#remove komutuyla girilen deðer atýlýr
liste.remove("Piton")

#Index() index methodu verilen bir deðerin baþtan baþlayarak hangi indekste olduðunu bulur.
#Deðer listede yoksa hata döner.
#Eðer ekstra index deðeri belirtilirse index metodu() deðeri by indeksten itibaren aramaya çalýþýr.

liste3=[1,2,3,4,5,6,7,8,9,10,3]
#indeks 2 döner
liste3.index(3)

liste3.index(3,3)

#Count metodu
#Verilen bir deðerin listede kaç defa geçtiðini sayar.

liste3.count(3)

#Sort methodu
#Sort metodu bir listenin elemanlarýný sayýsý küçükten büyüðe, string ise alfabetik olarak sýralar. Eðer özellik içine reverse=true deðeri verilirse elemanlarý büyükten küçüðe sýralar

