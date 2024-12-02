def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

def encontrar_duplicados_com_conjunto(lista):
    elementos_vistos = set()
    duplicados_encontrados = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            duplicados_encontrados.add(elemento)
        else:
            elementos_vistos.add(elemento)
    return list(duplicados_encontrados)

numeros = [5, 3, 2, 4, 6, 3, 7, 8, 5, 9, 10, 6, 1]

print("Duplicados (Força Bruta):", encontrar_duplicados_forca_bruta(numeros))
print("Duplicados (Usando Conjunto):", encontrar_duplicados_com_conjunto(numeros))
