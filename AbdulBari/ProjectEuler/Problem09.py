#Rule 1: a<b<c
#Rule 2: a^2+b^2=c^2
#Rule 3: a+b+c=1000
#Find abc

sum_total=1000

for a in range(1,sum_total):
    for b in range (a+1,sum_total-a):
        c = sum_total - a - b
        if a**2 + b**2 == c**2:
            print(f"a = {a}, b = {b}, c = {c}")
            print(f"abc = {a * b * c}")
            break
    
                