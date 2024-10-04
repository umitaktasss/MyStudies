#List Comprehension
#liste üretmek ve oluşturma da pratik kolaylık sağlayan list comp:
liste1=[1,2,3,4,5]
liste2=[i for i in liste1]
print(liste2)
liste3=[i*2 for i in liste1]
print(liste3)
liste4=[(1,2),(3,4),(5,6)]
liste5= [i*j for i,j in liste4]
print(liste5)
listea=[[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
listeb=[x for i in listea for x in i]
print(listeb)