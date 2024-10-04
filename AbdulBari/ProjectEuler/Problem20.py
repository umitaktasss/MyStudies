import math

sayi=100

faktoriyel = math.factorial(sayi)
faktoriyel=str(faktoriyel)

total_sum=sum(int(i) for i in faktoriyel)

print("Rakamlarin toplami: {}".format(total_sum))

      