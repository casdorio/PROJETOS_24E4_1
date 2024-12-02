def swap_elements(array, idx1, idx2):
    array[idx1], array[idx2] = array[idx2], array[idx1]

def biDirectionalSort(array):
    left = 0
    right = len(array) - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(left, right):
            if array[i] > array[i + 1]:
                swap_elements(array, i, i + 1)
                swapped = True

        right -= 1 
        if not swapped:
            break 

        swapped = False

        for i in range(right, left, -1):
            if array[i] < array[i - 1]:
                swap_elements(array, i, i - 1)
                swapped = True

        left += 1

def display(array):
    print(array)


numbers = [54, 24, 25, 12, 22, 30, 50]

print("Array original:")
display(numbers)

biDirectionalSort(numbers)

print("Array ordenado:")
display(numbers)
