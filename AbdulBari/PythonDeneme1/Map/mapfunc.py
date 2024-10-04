def double(x):
    return x*2

# Map objesi  elemanlarımızı fonksiyon içerisinde teker teker uygulayacak.
print(list(map(double,[1,2,3,4,5,6,7])))

print(list(map(lambda x: x**2,(1,2,3,4,5,6,7,8,9,10))))

liste1=[1,2,3,4]
liste2=[5,6,7,8]
liste3=[9,10,11,12,13]

liste4=list(map(lambda x,y:x*y,liste1,liste2))
print(liste4)
