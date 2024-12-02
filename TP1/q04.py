def busca_binaria(array, numero):
    passos = 0
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        passos += 1
        meio = (inicio + fim) // 2

        if array[meio] == numero:
            return passos
        elif array[meio] < numero:
            inicio = meio + 1
        else:
            fim = meio - 1

    return passos

array = [2, 4, 6, 8, 10, 12, 13]
numero = 8

resultado = busca_binaria(array, numero)
print(f"Número {numero} encontrado em {resultado} passos.")
