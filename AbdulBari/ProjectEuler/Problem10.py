#Sum of all prime numbers bellow two million
#Find all prime numbers that bellow two million and put in a list then sum
#To find sum
import time


def sum_total(list):
    total=0
    for i in list:
        total +=i
    
    return total

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_prime_below_2million(numbers):
    prime_numbers = []
    last_element = 2000000
    i = 0
    while i < len(numbers) and numbers[i] <= last_element:
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
        i += 1
    return prime_numbers


start_time = time.time()
liste_A = list(range(1, 2000000))
liste_B = find_prime_below_2million(liste_A)
liste_C= sum_total(liste_B)
end_time = time.time()
execution_time = end_time - start_time
print(liste_C)
print(execution_time)


#65 saniye çalýþma süresi kötü algoritma , farklý algoritmalar bul!

