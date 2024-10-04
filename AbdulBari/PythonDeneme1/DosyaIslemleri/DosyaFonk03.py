from os import linesep


with open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","r") as file:
    print(file.tell()) #imlecin nerede oldugunu söyler
    file.seek(7)
    print(file.tell()) #imlecimiz artik 7. byteta
with open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","r+") as file:
    file.seek(5)
    icerik=file.read(10)
    icerik2=file.read(8)
    print(icerik)
    print(icerik2)
    print(file.tell())
    file.seek(10)
    file.write("Deneme") #10 karakterden sonra bu karakterlerin üzerine yazma iþlemi gerçekleþtirildi
    file.seek(0)
    file.write("Ahmet Acar\n")
    file.seek(0)
    print(file.read())
    
    
#with open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","a") as file:
#    file.write("Mert Erarslan\n")
#    file.seek(0)
    
with open("C:/Users/Tulpar/Desktop/Algorithm/PythonDeneme1/PythonDeneme1/DosyaIslemleri/bilgiler.txt","r+") as file:
    liste=file.readlines()
    print(liste)
    liste.insert(3,"Ahmet Baltaci\n")
    file.seek(0)
    file.writelines(liste)
    file.seek(0)
    print(file.read())



