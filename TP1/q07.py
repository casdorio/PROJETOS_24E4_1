def selectAStrings(array):
    newArray = []
    
    for i in range(len(array)):
        if array[i].startswith("a"):
            newArray.append(array[i])
    
    return newArray


array = ["abacaxi", "banana", "amora", "cereja", "damasco", "figo", "laranja", "manga", "melancia", "melao", "morango", "pera", "pessego", "uva", "maca"]
print(selectAStrings(array))

# Resposta:
# A complexidade do algoritmo é O(n), onde n é o tamanho do array. Isso porque o algoritmo percorre o array uma única vez, verificando se cada string começa com a letra "a".