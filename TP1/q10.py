def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def display(arr):
    print(arr)

test_cases = [
    ["banana", "maçã", "cereja", "data", "amora", "figo", "uva"],
    ["zebra", "macaco", "maçã", "banana"],
    ["gato", "cachorro", "morcego", "anta", "elefante"],
    [],
    ["laranja"],
    ["carro", "banana", "maçã", "cachorro", "elefante", "gato", "urso"],
]

for i, test_case in enumerate(test_cases, 1):
    print(f"Teste {i} - Lista original:")
    display(test_case)
    bubble_sort(test_case)
    print(f"Teste {i} - Lista ordenada:")
    display(test_case)
    print("-" * 30)
