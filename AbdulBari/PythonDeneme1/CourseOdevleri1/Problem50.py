#Program 1
#"Kareler" isminde bir tane s�n�f tan�mlay�n ve bu s�n�f� iterable bir s�n�f yapmaya �al���n. 
#Bu s�n�f�n init fonksiyonu maksimum isimli bir tane parametre als�n ve 
#her next i�leminde ekrana �zerinde bulundu�unuz say�n�n karesi yazd�r�ls�n. 
#StopIteration hatas� ekrana maksimum say�y� ge�ti�iniz zaman f�rlat�ls�n.

class Kareler():
    def __init__(self,sayi,max=0):
        self.max= max
        self.sayi=sayi
        self.kuvvet=2
       # self.current=sayi
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.sayi<=self.max):
            sonuc = self.sayi ** self.kuvvet
            self.sayi +=1
            return sonuc
        else:
            #self.sayi=self.current
            
            raise StopIteration
        
sayi1=Kareler(10,30)
iteration=iter(sayi1)
for i in iteration:
    print(i)
    
