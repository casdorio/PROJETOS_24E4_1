def buscar_contato(lista, nome_procurado):
    for indice in range(len(lista)):
        if lista[indice]["nome"] == nome_procurado:
            return lista[indice]

    return None

agenda = [
    {"nome": "Ana", "contato": "1234-5678"},
    {"nome": "Bruno", "contato": "9876-5432"},
    {"nome": "Clara", "contato": "4567-8901"}
]

resultado = buscar_contato(agenda, "Bruno")
print(resultado)
