def busca_linear(array, numero):
    passos = 0
    
    for i, valor in enumerate(array):
        passos += 1 
        if valor == numero:
            return passos
    
    return passos

array = [2, 4, 6, 8, 10, 12, 13]
numero = 8

resultado = busca_linear(array, numero)
print(f"Número {numero} encontrado em {resultado} passos.")
