file=open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","r")
for i in file:
    print(i,end='')
file.close()
file=open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","r")
iceri=file.read()
print("\n",iceri)
iceri2=file.read()
#Bo� olmas�n�n sebebi ilk iceri k�sm�nda dosya imleci sona geldi, bundan sonras�nda herhangi bir i�erik olmad���ndan okuma i�lemi ger�ekle�tirilmedi
print(iceri2)
file.close()
try:
    file=open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler2.txt","r")

except FileNotFoundError:
    print("Dosya Bulunamadi")
file=open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","r")
print(file.readline())
file.close()