#Problem 5
#1'den 100'e kadar olan sayýlardan sadece 3'e bölünen sayýlarý ekrana bastýrýn. Bu iþlemi *continue* ile yapmaya çalýþýn.

for i in range(1,101):
    if i % 3 != 0:
        continue
    else:
        print(i)