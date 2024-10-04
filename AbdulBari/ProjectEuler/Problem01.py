#If we list all the natural numbers below 10 that are multiples of 3 or 5
#we get 3,5,6,9 the sum of these multiples is 23

#Find the sum of all the multiples 3 or 5 bellow 1000.

#If the number get divided by 3 or 5 add in sum.
# Has been solved!
#The answer is 233168 

def sum_of_3_5(Liste):
    sum = 0
    for i in Liste:
        if (i % 3 == 0) or (i % 5 ==0):
            sum+=i
            
    return sum
    

Liste_1000=range(1,1000)

print(sum_of_3_5(Liste_1000))