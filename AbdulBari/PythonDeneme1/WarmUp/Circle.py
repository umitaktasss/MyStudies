#daire �evresi = 2pir
#daire alan� pr^2
pi=3.14
pi = 3.14

while True:
    r = float(input("Enter the radius: "))
    if r < 0:
        print("Invalid value! Please enter a non-negative value.")
    else:
        circumference = 2 * pi * r
        area = pi * (r ** 2)
        print("Circumference of the circle:", circumference)
        print("Area of the circle:", area)
        break  # Ge�erli bir de�er girdi�inde d�ng�den ��k
    #swap
a=3
b=4
a,b=b,a
print(a,b)
b**=3
print(b)

