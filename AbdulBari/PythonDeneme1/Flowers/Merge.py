def merge_sort(flowers):
    # Base case: if the list is empty or contains a single element, it is already sorted.
    if len(flowers) <= 1:
        return flowers

    # Find the middle point to divide the array into two halves.
    mid = len(flowers) // 2

    # Recursively sort the first half and the second half.
    left_half = merge_sort(flowers[:mid])
    right_half = merge_sort(flowers[mid:])

    # Merge the sorted halves.
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    # Traverse both arrays and append the smaller element to the sorted array.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append the remaining elements in the left half, if any.
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Append the remaining elements in the right half, if any.
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Test the merge_sort function with an example list of flowers.
# 0: Black, 1: White, 2: Purple
flowers = [2, 0, 1, 2, 0, 1, 2, 1, 0]

# Sort the flowers using the merge_sort function.
sorted_flowers = merge_sort(flowers)

# Print the sorted list of flowers.
print("Sorted flowers:", sorted_flowers)
