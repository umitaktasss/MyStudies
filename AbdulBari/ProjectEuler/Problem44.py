#Hangi pentagon say�lar�n�n toplam� ve fark� pentagon say�d�r?
#Ra+Rb=Rc ve |Ra-Rb|=Rd               
#Pentagon number formula n(3n-1)//2
import math

def find_pentagons_sum_and_difference(limit):
    # Pentagonal numbers are generated using n(3n-1)//2
    pentagon_numbers = set()
    
    i = 1
    while True:
        pentagon_number_a = i * (3 * i - 1) // 2
        pentagon_numbers.add(pentagon_number_a)
        
        for j in range(1, i):
            pentagon_number_b = j * (3 * j - 1) // 2
            
            sum_pentagons = pentagon_number_a + pentagon_number_b
            diff_pentagons = pentagon_number_a - pentagon_number_b
            
            if is_pentagon(sum_pentagons) and is_pentagon(diff_pentagons):
                print(f"Found: P({i}) = {pentagon_number_a}, P({j}) = {pentagon_number_b}")
                print(f"Sum: {sum_pentagons}, Difference: {diff_pentagons}")
                return pentagon_number_a, pentagon_number_b, sum_pentagons, diff_pentagons
        
        if i >= limit:
            break
        
        i += 1

def is_pentagon(number):
    discriminant = 1 + 24 * number
    sqrt_discriminant = math.isqrt(discriminant)
    
    if sqrt_discriminant ** 2 == discriminant:
        k = (1 + sqrt_discriminant) / 6
        return k.is_integer()
    return False


# Example usage with a limit
limit = 10000  # You can set this higher if needed
find_pentagons_sum_and_difference(limit)

#Zaman Kompleksi O(n^2)