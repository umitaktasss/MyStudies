#denklem ax^2+bx+c   
#Delta= b**2-4*a*c
#(-b-delta**0.5)/(2*a) (-b+delta**0.5)/(2*a)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
delta=b**2-4*a*c
if(delta<0):
 print("Kok yoktur!")
x_1=(-b-delta**0.5)/(2*a)
x_2=(-b+delta**0.5)/(2*a)
print("Birinci Kok {}\nIkinci Kok: {}\n".format(x_1,x_2))
