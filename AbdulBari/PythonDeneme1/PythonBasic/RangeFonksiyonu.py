#Pythonda bu haz�r fonksiyon bizim verdi�imiz degerlere g�re range isimli bir yap� olu�turur ve bu yap� listelere olduk�a benzer. Bu yap� ba�lang�� biti� ve opsiyonel olarak art�rma degeri alarak listelere benzeyen bir say� dizisi olu�turur.
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
#Break ifadesi sadeve ve sadece i�indeki bulundu�u d�ng�y� sonlard�r�r e�er i� i�e d�ng�ler bulunuyorsa ve en i�teki d�ng�de break kullan�lm��sa sadece i�teki d�ng� sonra erer.
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

    