from re import T


liste=[1,2,3,4,5]
print(dir(liste)) #__iter__ methoduyla uðraþacaðýz
iterator=iter(liste)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#Kendi iterabile objelerimizi nasl yapabiliriz?
#Oluþturduðumuz sýnýflarda mutlaka __iter()__ __next()__ metodlarýnýn tanýmlanmasý gereklidir.

class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi=kanal_listesi
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if (self.index<len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index= -1
            raise StopIteration


kumanda=Kumanda(["ATV","TRT","KANAL7","FOX","KANAL D"])
for i in kumanda:
    print(i)



