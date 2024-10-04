def merge_sort(flowers, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(flowers, left, middle)
        merge_sort(flowers, middle + 1, right)
        merge(flowers, left, middle, right)


def merge(flowers, left, middle, right):
    n1 = middle - left + 1  # Size of the first subarray
    n2 = right - middle  # Size of the second subarray

    # Create temporary arrays
    leftArray = [0] * n1
    rightArray = [0] * n2

    # Copy data to temp arrays leftArray and rightArray
    for i in range(n1):
        leftArray[i] = flowers[left + i]
    for j in range(n2):
        rightArray[j] = flowers[middle + 1 + j]

    # Initial indexes of the first and second subarrays
    i = 0  # Initial index of leftArray
    j = 0  # Initial index of rightArray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back into flowers[left..right]
    while i < n1 and j < n2:
        if compare(leftArray[i], rightArray[j]) <= 0:
            flowers[k] = leftArray[i]
            i += 1
        else:
            flowers[k] = rightArray[j]
            j += 1
        k += 1

    # Copy any remaining elements of leftArray
    while i < n1:
        flowers[k] = leftArray[i]
        i += 1
        k += 1

    # Copy any remaining elements of rightArray
    while j < n2:
        flowers[k] = rightArray[j]
        j += 1
        k += 1


def compare(flower1, flower2):
    # Define the order of the colors
    order = {"black": 0, "white": 1, "purple": 2}
    return order[flower1] - order[flower2]


# Example usage
flowers = ["purple", "black", "white", "purple", "black", "white"]
merge_sort(flowers, 0, len(flowers) - 1)
print("Sorted flowers:", flowers)