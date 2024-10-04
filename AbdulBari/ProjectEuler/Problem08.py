# Verilen sayý string formatýnda düz bir þekilde saklanmalý
number_string = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

# Sayýyý listeye çevirme
number_list = [int(digit) for digit in number_string]

#Þimdi bu liste içerisinde bitiþik 13 sayýnýn en büyük olmasýný istiyorum.
#ilk sayýdan baþlar sonra o sayýyý sonraki 12 sayi ile çarparým. 
#elde ettiðim sonucu tutarým.
#sonra ikinci sayýyý alýrým, ondan sonraki 12 sayi için çarparým.
#elde ettiðim sonuc önceki sonuçtan büyükse bu sonucu alýrým.
def find_adjacent_13(liste):
    max_product = 0  # Maksimum çarpýmý tutmak için deðiþken
    max_sequence = []  # Maksimum çarpýmýn hangi sayýlarýn çarpýmý olduðunu tutmak için deðiþken

    for i in range(len(liste) - 12):  # Listeyi dolaþ ve 13 elemanlý alt listeler oluþtur
        product = 1  # Çarpým için baþlangýç deðeri
        for j in range(i, i + 13):
            product *= liste[j]  # Her bir sayý için çarpým iþlemi yap

        if product > max_product:  # Bulunan çarpým maksimumdan büyükse güncelle
            max_product = product
            max_sequence = liste[i:i + 13]  # En büyük çarpým için olan sayýlarý tut

    return max_product, max_sequence  # En büyük çarpýmý ve hangi sayýlardan oluþtuðunu döndür

liste=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print(find_adjacent_13(number_list))


def find_adjacent_number(list):
    listea=[]
    max_product = 0
    # son 4 sayý dahil deðil.
    for i in range(len(list)-4):
        product = 1
        for j in range(i,i+5):
            product *= list[j]
        if product > max_product:
            max_product = product
            listea=list[i:i+5]
    return max_product, listea

print(find_adjacent_number(liste))
        
