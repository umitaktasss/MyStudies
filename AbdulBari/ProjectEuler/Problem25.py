#1000 basamakl� ilk fibonacci dizisinin indeksi nedir?

import math

def basamak_sayisi(sayi):
    return math.floor(math.log10(sayi) + 1)

def fibonacci():
    fib = [1, 1]
    while basamak_sayisi(fib[-1]) < 1000:
        fib.append(fib[-1] + fib[-2])
    return fib

fib_listesi = fibonacci()
print(f"Fibonacci dizisinin {len(fib_listesi)}. terimi 1000 basamaklidir.")
