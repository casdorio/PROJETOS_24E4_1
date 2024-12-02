import random

def contar_impares(ids_livros):
    total_impares = 0
    for id_livro in ids_livros:
        if id_livro % 2 != 0:
            total_impares += 1

    return total_impares

livros_ids = [random.randint(10000, 99999) for _ in range(15)]

print('Identificações dos livros: ', livros_ids)
print('Total de identificações ímpares: ', contar_impares(livros_ids))