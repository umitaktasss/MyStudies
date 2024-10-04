#The Prime factors of 13195 are 5,7,13,29
#What is the largest prime factor of the number 600851475143

#Algorithm:
#Start with 2 and check if it divides the given number.
#If it divides evenly, update the prime_factor to this value and divide the number by this factor.
#Repeat this process until no factors are left that are smaller than the square root of the number.
#If, after all, the number is still greater than 1, it means the remaining number is a prime number and it is the largest prime factor.



def largest_prime_factor(number):
    prime_factor = 1
    i = 2
    # Rule: Checks for prime factors up to the square root of the number
    while i * i <= number:
        if number % i == 0:
            prime_factor = i
            number //= i
        else:
            i += 1

    if number > 1:
        prime_factor = number

    return prime_factor   

print(largest_prime_factor(600851475143))