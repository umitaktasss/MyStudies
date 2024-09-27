#Bu b�l�mde binary search algoritmas�n�n iterative halini g�rece�iz.
#Binary Searche ba�lamadan �nce �u sorular� soral�m.
#Binary Search temeli neye dayanmakta?
#Binary Search nedir?
#Hangi durumlarda kullan�l�r?
#Zaman Kompleksi Nedir?
#�ncellikle Binary Search�n temeli divie and conquer da yatmakta
#Peki Bu divide and conquer ne?
#Bir problemi ��zmek i�in kullan�lan �zel bir y�ntemdir.
#Bir problemde size(b�y�kl���n) verildi�ini varsayal�m,
#Ve problemin par�alara ayr�labilece�ini varsayal�m.
#Bu problemi k���k par�alara ay�raca��z. 
#B�ylelikle her problemin bir cevab� olacakt�r
#Sonra bu cevablar� birle�tirerek genel cevab� bulabiliriz.
#�unu unutmamak laz�m olu�an problemler ana problemin alt k�mesidir.
#Yani bu problemler ana problemle ayn� mant��� i�ermelidir (e�er bir s�ralama sorusuysa alt k�mede bulunan problemlerin cinside s�ralama problemi olmal�d�r!)
#E�er farkl� ana ba�l�klarda problemlere ayr�lm��sa bu ��z�m tekni�ine divide an conquer diyemeyiz.
#Bunun ��z�m� genellikle rek�rsif olur. 
#General Method:
#DAC(P)
#   if(small(P))
#       {
#           s(P);
#       
#       }
#    else{
#           divide P into P1,P2,P3,...,PK
#            Aplly DAC(P1), DAC(P2)
#            Combine(DAC(P1),DAC(P2)......) 
#       }

#Problems
#Binary Search
#Finding maximum and minimum
#MergeSort
#Quick Sort
#Strassem's matrix multiplication
#Rek�rsifin mant���n� ve zaman komplekslerini ��rendi�imize g�re
#Binary search�n iterative k�sm�n� ��renebiliriz.
#Tekrardan soral�m
#Binary Search nedir?
#Ad�ndan da anla��laca�� �zere bir arama alogirtmas�d�r.
#Belirli bir dizimiz olsun ve bu dizimizdeki elemanlar �nceden s�ralanm�� bir �ekilde dizi i�erisine yerle�tirilmi� olsun.
#�ki ba�lang�� noktam�z olacak birincisi dizimizin ba�� olacak ve di�eriyse dizimizin sonu.
#Ve arad���m�z bir de�er olacak bu de�erede anahtar diyelim.
#Peki bu anahtar de�erimizi nas�l bulaca��z?
#Bunun i�in ilk ba�lang�� noktam�z (l) ve ikinci ba�lang�� noktam�z (h) bunlarla birlikte ortanca noktam�z� belirleyece�iz (m=(l+h)/2).
#E�er m noktas�ndaki de�erimiz arad���m�z anahtar de�erden k���kse l noktam�z� m+1 olarak g�ncelleyece�iz.
#E�er m noktas�ndaki de�erimiz arad���m�z anahtar de�erden b�y�kse h noktas�n� m-1 olarak g�ncelleyece�iz.
#Bu algoritmadaki mant�kla bu i�lemi rek�rsif bir �ekilde ger�ekle�tirece�iz ve en sonunda 
#O(logn) zamanda arad���m�z anahtar de�eri bulmu� olaca��z.
#Evet bunun i�in �rnek bi C kodu yazaca��m sonra Python i�in yazaca��m
#Burada g�rd���n�z kod iterative kodtur.
#int BinSearch(Array,size,anahtar){
#
#   low=1, h=n,
#   while(l<=h){
#   mid=(l+h)/2                       
#   if(key==A[mid])                        
#      return mid;                    
#    if(key<A[mid])
#       h=mid-1
#    else
#       l=mid+1
#   }
#       return 0
# }
#�imdi kodu rek�rsif �ekilde yazaca��z.
#RBinSearch(l,h,key){
#          if (l==h)
#          {  if (A[l]==key)
#               return l;
#             else
#             return 0;              
#          }
#          else{
#               mid=(l+h)/2
#               if(key==A[mid])
#               return mid;
#               if(key<A[mid])
#               return RBinSearch(l,mid-1,key)           T(n/2)
#               } 
#               else
#                   return RBinSearch(mid+1,h,key)        T(n/2)      
#                                                         T(n)=T(n/2)+1                      
#                                                              O(logn)     
#
#
#}



def binary_Search_R(List,low,high,key):
    if low==high:
        if(List[low]==key):
            return low
        else:
            return 0
            
    else:
        mid=(low+high)//2
        if(key==List[mid]):
            return mid
        if(key < List[mid]):
            return binary_Search_R(List,low,mid-1,key)
        else:
            return binary_Search_R(List,mid+1,high,key)
        


liste_a=range(1,300,2)
aranan=66
indeks=binary_Search_R(liste_a,0,len(liste_a)-1,aranan)
if indeks:
    print(f"""Aranan sayi olan "{aranan}" sayimiz {indeks}. indekste bulunmustur.""")
    print(f"Listemizin {indeks} indeksinin degeri {aranan}") #Ba�ar�l�
else:
    print(f"""Aranan sayi olan "{aranan}" sayimiz  liste icerisinde bulunmamaktadir.""")
    
#{  Peki Pythonda Binary Search yapan bir method var m�? Evet var 
# import bisect
# sorted_list=[1,3,4,7,8,10]
# element= 7
# index= bisect.bisect_left(sorted_list,element)
#if index < len(sorted_list) and sorted_list[index] == element:
#   print(f"Element {element} found at index {index}.")    
#else:
#   print(f"Element {element} not found.")
#
#
#}


