import random

cartas_espadas = list(range(1, 14))
random.shuffle(cartas_espadas)

primeira_mao = []

while cartas_espadas:
    carta_atual = cartas_espadas.pop(0)

    posicao = 0
    while posicao < len(primeira_mao) and primeira_mao[posicao] < carta_atual:
        posicao += 1

    primeira_mao.insert(posicao, carta_atual)

print("Cartas de espadas ordenadas:", primeira_mao)
