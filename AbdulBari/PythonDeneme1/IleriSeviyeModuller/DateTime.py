from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")

zaman=datetime.now()

#Date time modülü ile bulunduðumuz zamanýn gerçek zamanlý olarak bilgisini alabiliriz
#Ayný þekilde zaman.year, zaman.month, zaman.hour, zaman.milisecond gibi özel methodlarla ayrý ayrý vakit bilgisi alabiliriz.
print(zaman)
#Buradaki ctime ile günüde öðrenebiliriz.
print(datetime.ctime(zaman))
print(datetime.strftime(zaman,"%Y %B %A %X %D"))
#Ýki tarih arasýndaki gün farkýný bulma
tarih1=datetime(2018,4,26)
tarih2=datetime.now()
fark=tarih2-tarih1
print(fark)