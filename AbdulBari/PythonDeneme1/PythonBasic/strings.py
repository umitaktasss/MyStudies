#3 farlk� �ekilde olu�turulabilir tek t�rnak �ift t�rnak veya 3 t�rnak ile
a="Feeling in love"  #Ya�anabilecek yaz�m yanl��l�klar�n� gidermek i�in kullan�l�r!
print(a,"A'nin 10. elemani", a[10])
# ve geriye do�ru indeks yazabiliriz
print(a[-1])
#String par�alama a[ba�lama:biti�:atlama]
print(a[4:12])
print(a[4:])
print(a[:5])
print(a[:-1])
print(a[::2])
print(a[::-1])
#String �zellkleri
#String uzunlugunu buma leng
string="Greetings Folks! "
print(len(string))
#bir stringi direkt olarak de�i�tiemezsin ! string[3]='t' error

#Stringleri toplayabilirsin
string2="Have you been tried yet? "
string3="If you have, Get your cold fresh drinks in the trunk"
print(string+string2+string3)
print(string*4)
#Error!!! print(string/2) you can't divide
#bir stringi b�yle de�i�tirebiliriz
string= string+"You got the same smell right?"
print(string)
