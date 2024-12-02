def soma_elementos(lista):
    if not lista:
        return 0

    return lista[0] + soma_elementos(lista[1:])

lista = [111, 223, 5, 8, 18, 20]
print("A soma dos elementos é:", soma_elementos(lista))