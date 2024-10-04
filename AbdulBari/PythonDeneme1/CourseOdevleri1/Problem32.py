liste = ["345","sadas","324a","14","kemal"]

for eleman in liste:
    
    try: 
        eleman = int(eleman) # Eðer hata ile karþýlaþýrsak burasý hata verecek ve print çalýþmayacak.
        print(eleman)
    except:
        pass 