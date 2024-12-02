def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]

        return quicksort(left) + [pivot] + quicksort(right)

arr = [10, 7, 8, 9, 1, 5]
print("Array original:", arr)
sorted_arr = quicksort(arr)
print("Array ordenado:", sorted_arr)
