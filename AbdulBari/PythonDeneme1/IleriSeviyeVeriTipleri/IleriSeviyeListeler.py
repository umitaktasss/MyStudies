#Listelerde en �ok kullan�lan metodlar

liste = [1,23,34,44]
#Eleman ekleme
liste.append(31)

liste_2=[0,10,20,30]

#Liste_2yi liste ile birle�tirir. (geni�letir)
liste.extend(liste_2)

#�nsert methoduyla indeksleme yap�labilir

liste.insert(2,"Piton")

#Pop metoduyla eleman ��kartabiliriz. (en son eleman)

liste.pop()
#2. indeksteki eleman ��kar�l�cak
liste.pop(2)

#remove komutuyla girilen de�er at�l�r
liste.remove("Piton")

#Index() index methodu verilen bir de�erin ba�tan ba�layarak hangi indekste oldu�unu bulur.
#De�er listede yoksa hata d�ner.
#E�er ekstra index de�eri belirtilirse index metodu() de�eri by indeksten itibaren aramaya �al���r.

liste3=[1,2,3,4,5,6,7,8,9,10,3]
#indeks 2 d�ner
liste3.index(3)

liste3.index(3,3)

#Count metodu
#Verilen bir de�erin listede ka� defa ge�ti�ini sayar.

liste3.count(3)

#Sort methodu
#Sort metodu bir listenin elemanlar�n� say�s� k���kten b�y��e, string ise alfabetik olarak s�ralar. E�er �zellik i�ine reverse=true de�eri verilirse elemanlar� b�y�kten k����e s�ralar

