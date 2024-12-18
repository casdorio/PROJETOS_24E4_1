import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def testar_bubble_sort(tamanho_lista):
    lista_precos = [random.uniform(1, 1000) for _ in range(tamanho_lista)]
    inicio = time.time()
    bubble_sort(lista_precos)
    fim = time.time()

    return fim - inicio

tempo_1k = testar_bubble_sort(1000)
tempo_10k = testar_bubble_sort(10000)

print(f"Tempo para ordenar 1.000 elementos: {tempo_1k:.6f} segundos")
print(f"Tempo para ordenar 10.000 elementos: {tempo_10k:.6f} segundos")
