liste = ["345","sadas","324a","14","kemal"]

for eleman in liste:
    
    try: 
        eleman = int(eleman) # E�er hata ile kar��la��rsak buras� hata verecek ve print �al��mayacak.
        print(eleman)
    except:
        pass 