def �ift_mi(say�):
    
    if (say� % 2 == 0):
        return say�
    else:
        raise ValueError
liste = [34,2,1,3,33,100,61,1800]

for i in liste:
    try:
        print(�ift_mi(i))
    except ValueError:
        pass