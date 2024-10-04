#1 den 20000 e Liste oluþtur.
#Yeni bir liste oluþtur bu liste içerisinde prime sayýlarý ekle. 
#10001e ulaþýnca dur

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_nth_prime(n):
    count=0
    number=2
    while count<n:
        if is_prime(number):
            count+=1
            if count == n:
                return number
        number +=1    
              

prime_10001=find_nth_prime(10001)

print("10001th Prime Number is: {}".format(prime_10001))