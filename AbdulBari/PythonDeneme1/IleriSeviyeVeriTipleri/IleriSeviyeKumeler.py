#Kümeler (Sets) 
#Kümeler, matematikte olduðu gibi bir elemandan sadece bir adet tutan bir veritipidir.
#Bu açýdan kullanýldýklarý yerlerde çok önemli bir veritipi olmaktadýrlar.
#isterseniz hemen bir küme oluþturalým

#Benzersiz Elemanlarýn Tutulmasý
#Tekrarlayan Eleman varsa Bu eleman Bir defa yazýlýr

isimler =["Ali","Ayse","Ali","Mehmet","Mehmet"]

benzersiz_isimler=set(isimler)
#Çýktý Ali Ayse Mehmet olacaktýr
print(benzersiz_isimler)

yasakli_kelimeler = {"spam", "reklam", "yasak"}

kullanici_Girisi = input("Lutfen Girdi Giriniz: ").lower()

for kelime in yasakli_kelimeler:
     if kelime in kullanici_Girisi:
        print(f"Bu kelime yasakli! : {kelime}")
        break
    

#Küme operosyanlarý
#Eðer iki veya daha fazla veri kümesi üzerinde kesiþim, birleþim, fark gibi iþlemler
#Yapmak istiyorsanýz, kümeler bu iþlemler için doðal bir seçimdir.

set1={1,2,3,4}
set2={3,4,5,6}

# Kesiþim (intersection)
print(set1 & set2)

# Birleþim (union)
print(set1 | set2)

# Fark (difference)
print(set1-set2)

#Veri filtreleme ve temizleme

#Bir veri kümesini hýzlýca filtrelemek ve temizlemek istiyorsanýz kümeler kullanýþlýdýr.

numaralar = [1,2,3,2,4,3,5]

temiz_numaralar=list(set(numaralar))

print(temiz_numaralar)

#Performans gerektiren durumlar
# Büyük veri kümelerinde sýkça üyelik kontrolü yapýlacaksa, listeler yerine kümeler kullanmak performansý ciddi þekilde artýrabilir.

buyuk_kume = set(range(1000000))
print(999999 in buyuk_kume)  # Çok hýzlý çalýþý