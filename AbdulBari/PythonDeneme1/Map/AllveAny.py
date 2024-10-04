def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

listea= [True,False,True,False,True]

print(hepsi(listea))
def herhangi(liste):
    for i in liste:
        if  i:
            return True
    return False
listeb= [False,False,True,False,True]
print(herhangi(listeb))
liste_c=[1,1,1,1,1,1,0]
print(all(liste_c))
print(any(liste_c))