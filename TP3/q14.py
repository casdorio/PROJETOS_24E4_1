def soma_lista(lista):
    if not lista:
        return 0
    
    return lista[0] + soma_lista(lista[1:])

lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30]
lista3 = []

print(f"Soma da lista {lista1}: {soma_lista(lista1)}")
print(f"Soma da lista {lista2}: {soma_lista(lista2)}")
print(f"Soma da lista {lista3}: {soma_lista(lista3)}")
