#The sum of squares of the first ten natural number is,
#1^2+2^2+....+10^2=385
#(1+2+3+4...+10)^2=55^2=3025
#3025-385=2640


def power_of_sum_list(list):
    suma =0
    for i in list:
        suma +=i
    suma = suma ** 2
    return suma

def power_of_elements_list(list):
    suma =0
    for i in list:
        suma = (i**2)+suma
    return suma    

liste_100=range(1,101)

fark = power_of_sum_list(liste_100)-power_of_elements_list(liste_100)
print(fark)