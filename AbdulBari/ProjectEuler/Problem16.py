# 2^1000 say�s�n� hesapla
number = 2**1000

# Say�y� string'e �evir
number_str = str(number)

# Basamaklar�n toplam�n� hesapla
digit_sum = sum(int(digit) for digit in number_str)

# Sonucu yazd�r
print(digit_sum)
