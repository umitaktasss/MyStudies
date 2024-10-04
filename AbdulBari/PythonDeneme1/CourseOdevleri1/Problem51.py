#Program 2
# 1'den 1000'e kadar olan sayýlardan asal sayýlarý üreten generator bir fonksiyon yazýn.

def asal_mi(sayi):
    i =  2
    
    while i < sayi:
        if (sayi % i == 0):
            return False
        i += 1
    return True

def asal_generator():
    i =  2
    while True:
        if (asal_mi(i)):
            yield i
        i += 1
        

for sayi in asal_generator():
    if (sayi > 1000):
        break
    print(sayi)