def selection_sort(jogadores):
    n = len(jogadores)
    
    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if jogadores[j]['pontuacao'] < jogadores[menor_indice]['pontuacao']:
                menor_indice = j
        
        jogadores[i], jogadores[menor_indice] = jogadores[menor_indice], jogadores[i]

jogadores = [
    {'nome': 'Jogador 1', 'pontuacao': 120},
    {'nome': 'Jogador 2', 'pontuacao': 250},
    {'nome': 'Jogador 3', 'pontuacao': 180},
    {'nome': 'Jogador 4', 'pontuacao': 300},
]

print("Antes da ordenação:")
for jogador in jogadores:
    print(f"{jogador['nome']}: {jogador['pontuacao']}")

selection_sort(jogadores)

print("\nApós a ordenação:")
for jogador in jogadores:
    print(f"{jogador['nome']}: {jogador['pontuacao']}")
