#�imdi bir generator �zelli�i ile u�ra�aca��z.
 

def fibonacci():
    a=1
    b=1
    yield a
    yield b
    while True:
        a,b=b,b+a
        yield b
        
for sayi in fibonacci():
    
    if (sayi >100000):
        break
    print(sayi)