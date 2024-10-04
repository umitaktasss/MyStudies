#Bir sayi i�erisinde 1-n e kadar olmak �zere, n - basamak say�s� olmak �zere. Rakamlar� tekrar etmiyorsa bu say�n�n bu sayiya pandigital denir.
#�rnek: 1234 -> 1 den 4 e kadar ve say� 4 basamakl� say�n�n rakamlar� tekrar etmiyor ve 1 den 4 e kadar olan t�m say�lar� i�eriyor.
#Buna g�re en b�y�k prime pandigital say� ka�t�?
#�ncellikle 9 basamakl� 1 den 9 e olan say�lar�n perm�tasyonunu alarak say�lar� yerle�tirelim. Buradaki her sayi i�in asal olup olmad���na bakal�m.
#9 da ��kmazsa 8 e bak
#B�yle b�yle devam.


from ast import Num
import time
import itertools

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Ba�lang�� zaman�n� al
start_time = time.time()

# 9 basamakl� rakamlar�n perm�tasyonlar�n� olu�tur
digits = '7654321'
#9 basamakl� hi�bir pandigital say� asal ��kmad�
#8 e bak�yoruz.
#8 de de ayn�s�
#7 i�in bakt�m bulundu.
pandigital_numbers = itertools.permutations(digits, 7)

# Pandigital say�lar olu�turuluyor ve kontrol ediliyor
for perm in pandigital_numbers:
    number = int(''.join(perm))
    if isPrime(number):
        print(f"Sayi: {number}")
        break

# Biti� zaman�n� al ve ge�en s�reyi hesapla
end_time = time.time()
execution_time = end_time - start_time

print(f"Sure: {execution_time:.2f} saniye")
