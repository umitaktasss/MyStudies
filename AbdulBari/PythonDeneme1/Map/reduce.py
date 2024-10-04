from functools import reduce

def toplama(x,y):
    return x+y
# 12 ve 18= 30 daha sonra 30+20=50 sonra 50+10=60
# yani kısacası fonksiyonda gerçekleşen olayları depolayarak sonraki fonksiyona uygular! kümülatif bir fonksiyon birike birike sonuç oluşturur
print(reduce(toplama,[12,18,20,10]))
def maksimum(x,y):
    if(x>y):
        return x
    else:
        return y

print(reduce(maksimum,[-2,3,1,4]))