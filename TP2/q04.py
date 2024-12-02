def ordenar_menores_para_maiores(pilha_notas):
    pilha_temporal = []
    
    while pilha_notas:
        elemento = pilha_notas.pop()
        
        while pilha_temporal and pilha_temporal[-1] > elemento:
            pilha_notas.append(pilha_temporal.pop())
        
        pilha_temporal.append(elemento)
    
    while pilha_temporal:
        pilha_notas.append(pilha_temporal.pop())

notas_alunos = [8, 5, 7, 10, 3, 9]
print("Pilha original:", notas_alunos)

ordenar_menores_para_maiores(notas_alunos)
print("Pilha ordenada:", notas_alunos)
