import random

def ordenar_lista(valores):
    tamanho = len(valores)
    
    for i in range(tamanho):
        indice_minimo = i
        
        for j in range(i + 1, tamanho):
            if valores[indice_minimo] > valores[j]:
                indice_minimo = j
        
        valores[indice_minimo], valores[i] = valores[i], valores[indice_minimo]

numeros = [random.randint(1, 100) for _ in range(20)]

print('Lista antes de ordenar:', numeros)
ordenar_lista(numeros)
print('Lista ordenada:', numeros)