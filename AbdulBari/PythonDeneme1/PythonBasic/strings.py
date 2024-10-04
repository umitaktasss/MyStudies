#3 farlký þekilde oluþturulabilir tek týrnak çift týrnak veya 3 týrnak ile
a="Feeling in love"  #Yaþanabilecek yazým yanlýþlýklarýný gidermek için kullanýlýr!
print(a,"A'nin 10. elemani", a[10])
# ve geriye doðru indeks yazabiliriz
print(a[-1])
#String parçalama a[baþlama:bitiþ:atlama]
print(a[4:12])
print(a[4:])
print(a[:5])
print(a[:-1])
print(a[::2])
print(a[::-1])
#String Özellkleri
#String uzunlugunu buma leng
string="Greetings Folks! "
print(len(string))
#bir stringi direkt olarak deðiþtiemezsin ! string[3]='t' error

#Stringleri toplayabilirsin
string2="Have you been tried yet? "
string3="If you have, Get your cold fresh drinks in the trunk"
print(string+string2+string3)
print(string*4)
#Error!!! print(string/2) you can't divide
#bir stringi böyle deðiþtirebiliriz
string= string+"You got the same smell right?"
print(string)
