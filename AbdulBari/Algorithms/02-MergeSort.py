def merge(arr, l, mid, h):
    # �lk ve ikinci alt listeler olu�turuluyor
    left = arr[l:mid+1]
    right = arr[mid+1:h+1]

    i = j = 0
    k = l

    # �ki alt listeyi birle�tirme
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Kalan elemanlar� ekleme
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, l, h):
    if l < h:
        mid = (l + h) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, h)
        merge(arr, l, mid, h)

# �rnek Kullan�m
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr)-1)
print("Siralanmis liste:", arr)
