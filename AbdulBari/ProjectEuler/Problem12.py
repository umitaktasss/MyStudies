# Triangle numbers
# The first number : 1
# The second number: 1+2 = 3
# The third number : 1+2+3=6
# The fourth number : 1+2+3+4=10
#And so on

import math

def count_divisors(number):
    count = 1
    exponent = 0
    while number % 2 == 0:
        exponent += 1
        number //= 2
    count *= (exponent + 1)
    
    p = 3
    while p * p <= number:
        exponent = 0
        while number % p == 0:
            exponent += 1
            number //= p
        count *= (exponent + 1)
        p += 2
    
    if number > 1:
        count *= 2
        
    return count

def find_triangle_number_with_divisors(min_divisors):
    n = 1
    triangle_number = 1
    while count_divisors(triangle_number) <= min_divisors:
        n += 1
        triangle_number += n
    return triangle_number

# �al��ma s�resini �l�mek i�in time mod�l� kullan�m�
import time
start_time = time.time()

# 5000'den fazla b�leni olan ilk ��gen say�y� bulal�m
result = find_triangle_number_with_divisors(500)

end_time = time.time()

# Sonu�lar� ve ge�en s�reyi yazd�rma
print("500'den fazla boleni olan ilk ucgen sayi:", result)
print("Gecen sure: {:.2f} saniye".format(end_time - start_time))

           
    




