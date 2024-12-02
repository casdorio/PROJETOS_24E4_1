def greatestUniqueNumber(array):
    greatest = float('-inf')
    
    for i in array:
        if i > greatest:
            greatest = i
    
    return greatest

array = [3, 5, 7, 2, 8, 8, 7, 1]
print(greatestUniqueNumber(array))