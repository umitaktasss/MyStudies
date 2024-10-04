
#Dosya s�n�f� olu�turuldu.
class Dosya():
    #Dosya s�n�f�n�n �zellikleri belirlendi.
    def __init__(self):
        #Ula��lmak istenen metine ula��ld� ve metinin yap�s� okuntu.
        with open(r"C:\Users\Tulpar\Desktop\Algorithm\PythonDeneme1\PythonDeneme1\IleriSeviyeVeriTipleri\metin.txt", "r", encoding="utf-8") as file:
            dosya_icerigi = file.read()
            #Her bo�lukta string ifadeler b�l�nd�.
            kelimeler=dosya_icerigi.split()
            #Bo� bir sade_kelimeler listesi olu�turuldu.
            self.sade_kelimeler= list()
            #Kelimeleri daha sadece hale getirip sade kelimeler listesine ekleyece�iz.
            for i in kelimeler:
                #Alt sat�ra inmi�se
                i =i.strip("\n")
                #Bo�luk varsa
                i=i.strip(" ")
                #Nokta varsa
                i=i.strip(".")
                #Virg�l varsa
                i=i.strip(",")
                #Daha sonra bu stringi sade_kelimelere aktar.
                self.sade_kelimeler.append(i)
            
    def tum_kelimeler(self):
        #Kelime k�mesi olu�turuldu.
        kelimeler_kumesi= set()
        
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
            
        print("Tum kelimeler.........")
        
        for i in kelimeler_kumesi:
            print(i)
            
            print("***************************")
        

    def kelime_frekansi(self):
        
        kelime_sozluk=dict()
        
        for i in self.sade_kelimeler:
            
            if(i in kelime_sozluk):
                kelime_sozluk[i]+=1
            else:
                 kelime_sozluk[i]=1
                 
        for kelime, sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geciyor!!!".format(kelime,sayi))
            print("----------------------------")
dosya=Dosya()

dosya.tum_kelimeler()
dosya.kelime_frekansi()