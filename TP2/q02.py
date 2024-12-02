def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

import random
import time

arr = random.sample(range(1, 5000001), 5000000)

start_time = time.time()

sorted_arr = merge_sort(arr)

end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.4f} segundos")


