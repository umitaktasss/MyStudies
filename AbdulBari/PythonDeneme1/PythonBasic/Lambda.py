liste=[1,2,3,4,5]
liste_a=[i*2 for i in liste]
print(liste_a)
#aynen bu �ekilde lambda ifadeleri olu�turulabilir
#etiket=lambda parametre1,paratmetre2,....: i�lem, k���k fonksiyonlarda kullanmak pratik ve kullan��l� b�y�k fonksiyonlarda tavsiye edilmez.
def ikiylecarp(x):
    return x*2
print(ikiylecarp(3))
ikiylecarp2=lambda x: x*2  #yukardaki fonksiyonla ayni �zellikte olan lambda ifadesi tanimlandi.
print(ikiylecarp2(3))
def toplama(x,y,z):
    return x+y+z
print(toplama(1,2,3))
toplama2=lambda x,y,z: x+y+z
print(toplama2(1,2,3))

def terscevir(s):
    return s[::-1]
print(terscevir("Timu Satka"))
terscevir2=lambda s : s[::-1]
print(terscevir2("Timu Satka"))