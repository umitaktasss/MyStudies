# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#2520 % 2
#2520 % 3
#2520 % 4
#2520 % 20
# 1'den 20'ye kadar olan say�lar�n EKOK'unu bulan fonksiyon
import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_for_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

# 1'den 20'ye kadar olan say�lar i�in EKOK
print(lcm_for_range(20))



