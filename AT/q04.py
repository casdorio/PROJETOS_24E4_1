import random
import time

def busca_binaria(lista, isbn_procurado):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio]["isbn"] == isbn_procurado:
            return lista[meio], iteracoes
        elif lista[meio]["isbn"] < isbn_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None, iteracoes

def busca_linear(lista, isbn_procurado):
    iteracoes = 0
    for livro in lista:
        iteracoes += 1
        if livro["isbn"] == isbn_procurado:
            return livro, iteracoes

    return None, iteracoes

random.seed(42)
num_livros = 100_000
livros = [{"titulo": f"Livro {i}", "isbn": i} for i in range(1, num_livros + 1)]

isbn_procurado = random.randint(1, num_livros)

inicio_binaria = time.time()
livro_encontrado_bin, iteracoes_binaria = busca_binaria(livros, isbn_procurado)
fim_binaria = time.time()

inicio_linear = time.time()
livro_encontrado_lin, iteracoes_linear = busca_linear(livros, isbn_procurado)
fim_linear = time.time()

print(f"ISBN Procurado: {isbn_procurado}")
print("Busca Binária:")
print(f"  Livro encontrado: {livro_encontrado_bin}")
print(f"  Iterações: {iteracoes_binaria}")
print(f"  Tempo: {(fim_binaria - inicio_binaria):.6f} segundos\n")

print("Busca Linear:")
print(f"  Livro encontrado: {livro_encontrado_lin}")
print(f"  Iterações: {iteracoes_linear}")
print(f"  Tempo: {(fim_linear - inicio_linear):.6f} segundos")
