#Upper() ve lower()
#upper() metodu stringin tüm karakterlerini büyük harfe çevirir
#lower() metodu strining tüm karakterlerini küçük harfe çevirir
print("python".upper())
print("python".lower())
#replace(x,y)  stringteki x deðerlerini y ile deðiþtirir
print("Herkes ana baci gardas".replace("a","o"))
print("Abijim herkez yanlis bilioo".replace("kez","kes"))
#startswith() ve endswith()
#startswith: string x ile baþlýyorsa true, baþlamýyorsa false
#endswith: string x ile bitiyorsa true, bitmiyorsa false
print("Python".startswith("py")) #false
print("Python".startswith("Py")) #True
print("python".endswith("on"))#True
#split()
#split(a) verilen bir a deðerine göre string parçalarýna ayrýlarak her bir parça listeye atýlýr
liste="Python Programlama Dili".split(" ")
print(liste)
#strip(x) stringin baþýnda ve sonunda bulunan x deðerlerini siler
#lstrip(x) stringin sadece baþýnda bulunan x deðerlerini siler
#rstrip(x) stringin sadece sonunda bulunan x deðerlerini siler
print("                       Heheheeyyyyt         ".strip())#Deðer göndermezsek varsýyalan olarak boþluk karakteri
print("<<<<<<<<<<<<<<<<<<<<<<Umidoo<<<<<<<<Zibaboo<<<<<<<<".strip("<"))
print("<<<<<<<<<<<<<<<<<<<<<<Umidoo<<<<<<<<Zibaboo<<<<<<<<".lstrip("<"))
print("<<<<<<<<<<<<<<<<<<<<<<Umidoo<<<<<<<<Zibaboo<<<<<<<<".rstrip("<"))
#join listenin elemanlarýný bir string deðeriyle birleþtirmemizi saðlar
liste=["21","02","2014"]
print("/".join(liste))
print(".".join(liste))
#count(x) string içindkei x deðerlerini sayar
#count(x,index) stringin içindeki x deðerlerini verilen index deðerinden baþlayarak saymaya bailar
print("ada kapisi yandan carkli".count("a"))
print("ada kapisi yandan carkli".count(" "))
print("ada kapisi yandan carkli".count("a",2))
#find() ve rfind()
#x deðerlerini baþtan itibaren string içinde arar ve bulursa ilk bulduðu indeksi döndürür. Bulamazsa "-1" deðerini verir
#x deðerini sondan itibaren string içinde arar ve bulursa ilk bulduðu indeksi döndürür. Bulamazsa "-1" deðerini verir.
print("araba".find("a"))
print("araba".find("s"))
print("araba".rfind("a"))
print("araba".rfind("s"))