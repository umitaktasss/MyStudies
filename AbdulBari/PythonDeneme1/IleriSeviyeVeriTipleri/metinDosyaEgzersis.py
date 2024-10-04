
#Dosya sýnýfý oluþturuldu.
class Dosya():
    #Dosya sýnýfýnýn özellikleri belirlendi.
    def __init__(self):
        #Ulaþýlmak istenen metine ulaþýldý ve metinin yapýsý okuntu.
        with open(r"C:\Users\Tulpar\Desktop\Algorithm\PythonDeneme1\PythonDeneme1\IleriSeviyeVeriTipleri\metin.txt", "r", encoding="utf-8") as file:
            dosya_icerigi = file.read()
            #Her boþlukta string ifadeler bölündü.
            kelimeler=dosya_icerigi.split()
            #Boþ bir sade_kelimeler listesi oluþturuldu.
            self.sade_kelimeler= list()
            #Kelimeleri daha sadece hale getirip sade kelimeler listesine ekleyeceðiz.
            for i in kelimeler:
                #Alt satýra inmiþse
                i =i.strip("\n")
                #Boþluk varsa
                i=i.strip(" ")
                #Nokta varsa
                i=i.strip(".")
                #Virgül varsa
                i=i.strip(",")
                #Daha sonra bu stringi sade_kelimelere aktar.
                self.sade_kelimeler.append(i)
            
    def tum_kelimeler(self):
        #Kelime kümesi oluþturuldu.
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