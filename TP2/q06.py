def pedidos_impares(pilha_de_pedidos):
    count = 0
    for pedido in pilha_de_pedidos:
        if pedido % 2 != 0:
            count += 1
    return count

pilha_de_pedidos = [1, 2, 3, 4, 5]
print(pedidos_impares(pilha_de_pedidos)) 

