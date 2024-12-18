class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        self.raiz = self._adicionar_recursivo(self.raiz, valor)

    def _adicionar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.esq = self._adicionar_recursivo(nodo.esq, valor)
        else:
            nodo.dir = self._adicionar_recursivo(nodo.dir, valor)
        return nodo

    def obter_minimo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esq:
            atual = atual.esq
        return atual.valor

    def obter_maximo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.dir:
            atual = atual.dir
        return atual.valor

valores = [85, 70, 95, 60, 75, 90, 100]
arvore = ArvoreBinaria()
for valor in valores:
    arvore.adicionar(valor)

valor_minimo = arvore.obter_minimo()
valor_maximo = arvore.obter_maximo()

print(f"O menor valor encontrado foi: {valor_minimo}")
print(f"O maior valor encontrado foi: {valor_maximo}")
