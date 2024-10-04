#Ekrana yazdýrma komutu print
a="I'm on the spot!"
b=4
b=float(b)
print(a)
#\n \t karakterleri
print(a,"\n", a,"\t", a,"\t", a)
#type() içine gönderilen deðerin veri tipini gösterir.
print(type(a))
print(type(b))
#sep parametresi
print(3,4,5,6,7,8,9, sep="*")
#malesef print(a*3,sep="\n") ifadesinde olmuyor
print(a,a,a,sep="\n")
print(*a,sep="/")
#formatlama ve biçimlendirme
deger1=3
deger2=4
print("{} + {} 'nin toplami {}' dir".format(deger1,deger2,deger1+deger2))
print("{1} + {2} 'nin toplami {0} degildir".format(deger1,deger2,deger1+deger2))
print("{:.2f}".format(3.14762))