#Program 1
#"Kareler" isminde bir tane sýnýf tanýmlayýn ve bu sýnýfý iterable bir sýnýf yapmaya çalýþýn. 
#Bu sýnýfýn init fonksiyonu maksimum isimli bir tane parametre alsýn ve 
#her next iþleminde ekrana üzerinde bulunduðunuz sayýnýn karesi yazdýrýlsýn. 
#StopIteration hatasý ekrana maksimum sayýyý geçtiðiniz zaman fýrlatýlsýn.

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
    
