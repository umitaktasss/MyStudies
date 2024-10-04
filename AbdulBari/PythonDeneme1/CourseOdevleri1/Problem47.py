#1'den 1000'e kadar olan asal say�lar� ekrana yazd�ran bir program yaz�n. Daha sonra bir tane decorator fonksiyon kullanarak 
#bu fonksiyona 1'den 1000'e kadar olan m�kemmel say�lar� yazd�rma �zelli�i ekleyin.

def perfect_number_dec(func):
    def wrapper(numbers):
        # Check for perfect numbers
        for number in numbers:
            if perfect_number(number):
                print(f"{number} is a perfect number.")
        
        # Then perform prime number check
        return func(numbers)
    
    return wrapper

def perfect_number(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total == number

@perfect_number_dec
def prime_numbers(numbers):
    prime_nums = [] 
    
    for i in numbers:
        if i > 1:  # Prime numbers must be greater than 1
            for j in range(2, i):  # Check divisibility by numbers smaller than itself
                if i % j == 0:  # If divisible, it's not prime
                    break
            else:
                prime_nums.append(i)  # If no division occurred, it's prime

    return prime_nums

numbers = range(1000)

print(prime_numbers(numbers))
