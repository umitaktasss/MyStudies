import random
import string

def generate_random_name(length=7):
    return ''.join(random.choices(string.ascii_lowercase, k=length)).capitalize()
names = [generate_random_name() for _ in range(5500)]

with open('isimler.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')

print("Isimler basariyla 'isimler.txt' dosyasina kaydedildi.")


