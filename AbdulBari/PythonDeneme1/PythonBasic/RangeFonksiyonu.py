#Pythonda bu hazýr fonksiyon bizim verdiðimiz degerlere göre range isimli bir yapý oluþturur ve bu yapý listelere oldukça benzer. Bu yapý baþlangýç bitiþ ve opsiyonel olarak artýrma degeri alarak listelere benzeyen bir sayý dizisi oluþturur.
print(*range(0,20))
print(*range(1,20))
print(*range(15))
print(*range(1,100,2))
print(*range(5,100,3))
print(*range(20,0,-1))
for i in range(1,101):
    print(i)
for i in range(1,10):
    print("*"*i)
#Break ve continue
#Break ifadesi sadeve ve sadece içindeki bulunduðu döngüyü sonlardýrýr eðer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanýlmýþsa sadece içteki döngü sonra erer.
i=0
while(i<10):
    if(i==5):
        break
    print("i:",i)
    
    i+=1
    
#Continue 
liste=(list(range(11)))
for i in liste:
    if i==5 or i==3:
        continue
    print("i:",i)

    