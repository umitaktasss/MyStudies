#Kullan�c�dan 2 tane say� alarak bu say�lar�n 
#ebob
#iki say�n�n en yak�n bulu�tuklar� nokta

def ebob(a,b):
    ebob = 1
    for i in range(2, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            ebob = i
    print("ebob: ", ebob)
    return ebob
def ekok(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            ekok = max_num
            break
        max_num += 1
    print("ekok:", ekok)
    return ekok
        

ebob(19,6)
ekok(19,6)


