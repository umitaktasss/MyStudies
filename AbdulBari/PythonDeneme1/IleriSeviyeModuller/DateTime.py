from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")

zaman=datetime.now()

#Date time mod�l� ile bulundu�umuz zaman�n ger�ek zamanl� olarak bilgisini alabiliriz
#Ayn� �ekilde zaman.year, zaman.month, zaman.hour, zaman.milisecond gibi �zel methodlarla ayr� ayr� vakit bilgisi alabiliriz.
print(zaman)
#Buradaki ctime ile g�n�de ��renebiliriz.
print(datetime.ctime(zaman))
print(datetime.strftime(zaman,"%Y %B %A %X %D"))
#�ki tarih aras�ndaki g�n fark�n� bulma
tarih1=datetime(2018,4,26)
tarih2=datetime.now()
fark=tarih2-tarih1
print(fark)