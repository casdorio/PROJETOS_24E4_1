def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def display(arr):
    print(arr)

test_cases = [
    [54, 24, 25, 12, 22, 30, 50],
    [5, 3, 8, 6, 7, 2],
    [1, 2, 3, 4, 5],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [],
    [10],
]

for test_case in test_cases:
    print("Lista original:")
    display(test_case)
    bubble_sort(test_case)
    print("Lista ordenada:")
    display(test_case)
    print("-" * 30)
