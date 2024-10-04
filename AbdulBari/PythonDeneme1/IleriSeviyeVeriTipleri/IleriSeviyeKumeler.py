#K�meler (Sets) 
#K�meler, matematikte oldu�u gibi bir elemandan sadece bir adet tutan bir veritipidir.
#Bu a��dan kullan�ld�klar� yerlerde �ok �nemli bir veritipi olmaktad�rlar.
#isterseniz hemen bir k�me olu�tural�m

#Benzersiz Elemanlar�n Tutulmas�
#Tekrarlayan Eleman varsa Bu eleman Bir defa yaz�l�r

isimler =["Ali","Ayse","Ali","Mehmet","Mehmet"]

benzersiz_isimler=set(isimler)
#��kt� Ali Ayse Mehmet olacakt�r
print(benzersiz_isimler)

yasakli_kelimeler = {"spam", "reklam", "yasak"}

kullanici_Girisi = input("Lutfen Girdi Giriniz: ").lower()

for kelime in yasakli_kelimeler:
     if kelime in kullanici_Girisi:
        print(f"Bu kelime yasakli! : {kelime}")
        break
    

#K�me operosyanlar�
#E�er iki veya daha fazla veri k�mesi �zerinde kesi�im, birle�im, fark gibi i�lemler
#Yapmak istiyorsan�z, k�meler bu i�lemler i�in do�al bir se�imdir.

set1={1,2,3,4}
set2={3,4,5,6}

# Kesi�im (intersection)
print(set1 & set2)

# Birle�im (union)
print(set1 | set2)

# Fark (difference)
print(set1-set2)

#Veri filtreleme ve temizleme

#Bir veri k�mesini h�zl�ca filtrelemek ve temizlemek istiyorsan�z k�meler kullan��l�d�r.

numaralar = [1,2,3,2,4,3,5]

temiz_numaralar=list(set(numaralar))

print(temiz_numaralar)

#Performans gerektiren durumlar
# B�y�k veri k�melerinde s�k�a �yelik kontrol� yap�lacaksa, listeler yerine k�meler kullanmak performans� ciddi �ekilde art�rabilir.

buyuk_kume = set(range(1000000))
print(999999 in buyuk_kume)  # �ok h�zl� �al���