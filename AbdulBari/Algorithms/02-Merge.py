
def merge(list_a, list_b, lenght_a, lenght_b):
    i = 0
    j = 0
    merged_list = []
    
    while (i < lenght_a and j < lenght_b):
        if list_a[i] < list_b[j]:
            merged_list.append(list_a[i])
            i += 1
        else:
            merged_list.append(list_b[j])
            j += 1
    
    if i < lenght_a: 
        merged_list.extend(list_a[i:])
    elif j < lenght_b:
        merged_list.extend(list_b[j:])
        
    return merged_list

list_a = list(range(1, 6))#1,2,3,4,5
list_b = list(range(2, 9, 3))#2,5,8
le_a = len(list_a)
le_b = len(list_b)

merged_list = merge(list_a, list_b, le_a, le_b)

for i in merged_list:
    print("Elemanlar {}".format(i))

