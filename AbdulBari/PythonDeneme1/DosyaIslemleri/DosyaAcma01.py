
# dosya kapatma i�lemi e�er dosya kapat�lmazsa arka planda �al��maya devam eder ve gereksiz kaynak kullan�m�na sebep olur
file=open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","w",encoding="utf-8")
file.write("Bu benim kaderim abicim\n")
file.close()
# dosyayi tekrardan acarsak icerisindekiler silinir!!!
#file=open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","w",encoding="utf-8")
#file.close()
file=open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","a",encoding="utf-8")
file.write("Ben geri geldim abicim")
file.close()
