liste_a=[1,2,3,4,5,6,7,8,9,10]
liste_b=list(filter(lambda x: x % 2 !=0 and x %3 ==0,liste_a))
print(liste_b)
def asal_mi(x):
    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        while(i<x):
            if(x % i==0):
                return False
            i+=1
        return True

print(list(filter(asal_mi,liste_a)))

liste_c=list(filter(lambda x: x % 2 !=0 and x>0, [-10, -3, 0, 1, 4, 5, 7, -2, -1, 9]))
print(liste_c)