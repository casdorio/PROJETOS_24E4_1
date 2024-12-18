def mochila(capacidade_maxima, pesos_item, valores_item):
    num_itens = len(valores_item)
    tabela_valores = [[0 for _ in range(capacidade_maxima + 1)] for _ in range(num_itens + 1)]

    for i in range(1, num_itens + 1):
        for capacidade in range(1, capacidade_maxima + 1):
            if pesos_item[i-1] <= capacidade:
                tabela_valores[i][capacidade] = max(valores_item[i-1] + tabela_valores[i-1][capacidade-pesos_item[i-1]], tabela_valores[i-1][capacidade])
            else:
                tabela_valores[i][capacidade] = tabela_valores[i-1][capacidade]

    return tabela_valores[num_itens][capacidade_maxima]

capacidade_maxima = 50
pesos_item = [10, 20, 30]
valores_item = [60, 100, 120]

valor_maximo_obtido = mochila(capacidade_maxima, pesos_item, valores_item)
print(f"Valor máximo que pode ser carregado: {valor_maximo_obtido}")
