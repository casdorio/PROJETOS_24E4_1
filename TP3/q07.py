import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(left) - len(right) 
    
    if len(left) <= k < len(left) + pivot_count:
        return pivot
    elif k < len(left):
        return quickselect(left, k)
    else:
        return quickselect(right, k - len(left) - pivot_count)


arr = [10, 7, 8, 9, 1, 5]
k = 3
print(f"O {k+1}-ésimo menor elemento é:", quickselect(arr, k))
