class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._adicionar_recursivo(self.raiz, valor)

    def _adicionar_recursivo(self, nodo_atual, valor):
        if valor < nodo_atual.valor:
            if nodo_atual.esq is None:
                nodo_atual.esq = Nodo(valor)
            else:
                self._adicionar_recursivo(nodo_atual.esq, valor)
        else:
            if nodo_atual.dir is None:
                nodo_atual.dir = Nodo(valor)
            else:
                self._adicionar_recursivo(nodo_atual.dir, valor)

    def procurar(self, valor):
        return self._procurar_recursivo(self.raiz, valor)

    def _procurar_recursivo(self, nodo_atual, valor):
        if nodo_atual is None or nodo_atual.valor == valor:
            return nodo_atual

        if valor < nodo_atual.valor:
            return self._procurar_recursivo(nodo_atual.esq, valor)
        return self._procurar_recursivo(nodo_atual.dir, valor)



arvore = ArvoreBuscaBinaria()
valores = [100, 50, 150, 30, 70, 130, 170]

print("Adicionando os valores:", valores)
for valor in valores:
    arvore.adicionar(valor)


valor_busca = 70
resultado = arvore.procurar(valor_busca)
print(f"\nProcurando o valor R$ {valor_busca}:")
if resultado:
    print(f"Valor R$ {valor_busca} encontrado na árvore!")
else:
    print(f"Valor R$ {valor_busca} não encontrado na árvore.")
