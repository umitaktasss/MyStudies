#Upper() ve lower()
#upper() metodu stringin t�m karakterlerini b�y�k harfe �evirir
#lower() metodu strining t�m karakterlerini k���k harfe �evirir
print("python".upper())
print("python".lower())
#replace(x,y)  stringteki x de�erlerini y ile de�i�tirir
print("Herkes ana baci gardas".replace("a","o"))
print("Abijim herkez yanlis bilioo".replace("kez","kes"))
#startswith() ve endswith()
#startswith: string x ile ba�l�yorsa true, ba�lam�yorsa false
#endswith: string x ile bitiyorsa true, bitmiyorsa false
print("Python".startswith("py")) #false
print("Python".startswith("Py")) #True
print("python".endswith("on"))#True
#split()
#split(a) verilen bir a de�erine g�re string par�alar�na ayr�larak her bir par�a listeye at�l�r
liste="Python Programlama Dili".split(" ")
print(liste)
#strip(x) stringin ba��nda ve sonunda bulunan x de�erlerini siler
#lstrip(x) stringin sadece ba��nda bulunan x de�erlerini siler
#rstrip(x) stringin sadece sonunda bulunan x de�erlerini siler
print("                       Heheheeyyyyt         ".strip())#De�er g�ndermezsek vars�yalan olarak bo�luk karakteri
print("<<<<<<<<<<<<<<<<<<<<<<Umidoo<<<<<<<<Zibaboo<<<<<<<<".strip("<"))
print("<<<<<<<<<<<<<<<<<<<<<<Umidoo<<<<<<<<Zibaboo<<<<<<<<".lstrip("<"))
print("<<<<<<<<<<<<<<<<<<<<<<Umidoo<<<<<<<<Zibaboo<<<<<<<<".rstrip("<"))
#join listenin elemanlar�n� bir string de�eriyle birle�tirmemizi sa�lar
liste=["21","02","2014"]
print("/".join(liste))
print(".".join(liste))
#count(x) string i�indkei x de�erlerini sayar
#count(x,index) stringin i�indeki x de�erlerini verilen index de�erinden ba�layarak saymaya bailar
print("ada kapisi yandan carkli".count("a"))
print("ada kapisi yandan carkli".count(" "))
print("ada kapisi yandan carkli".count("a",2))
#find() ve rfind()
#x de�erlerini ba�tan itibaren string i�inde arar ve bulursa ilk buldu�u indeksi d�nd�r�r. Bulamazsa "-1" de�erini verir
#x de�erini sondan itibaren string i�inde arar ve bulursa ilk buldu�u indeksi d�nd�r�r. Bulamazsa "-1" de�erini verir.
print("araba".find("a"))
print("araba".find("s"))
print("araba".rfind("a"))
print("araba".rfind("s"))