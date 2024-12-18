import sys
sys.stdout.reconfigure(encoding='utf-8')

class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        if self.raiz is None:
            self.raiz = No(dado)
        else:
            self._inserir_no(self.raiz, dado)

    def _inserir_no(self, atual, dado):
        if dado < atual.dado:
            if atual.esquerda is None:
                atual.esquerda = No(dado)
            else:
                self._inserir_no(atual.esquerda, dado)
        else:
            if atual.direita is None:
                atual.direita = No(dado)
            else:
                self._inserir_no(atual.direita, dado)

    def excluir(self, dado):
        self.raiz = self._excluir_no(self.raiz, dado)

    def buscar(self, dado):
        return self._buscar_no(self.raiz, dado)

    def _buscar_no(self, atual, dado):
        if atual is None:
            return False
        if atual.dado == dado:
            return True
        if dado < atual.dado:
            return self._buscar_no(atual.esquerda, dado)
        else:
            return self._buscar_no(atual.direita, dado)

    def _menor_no(self, atual):
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _excluir_no(self, atual, dado):
        if atual is None:
            return atual

        if dado < atual.dado:
            atual.esquerda = self._excluir_no(atual.esquerda, dado)
        elif dado > atual.dado:
            atual.direita = self._excluir_no(atual.direita, dado)
        else:
            if atual.esquerda is None and atual.direita is None:
                return None
            if atual.esquerda is None:
                return atual.direita
            if atual.direita is None:
                return atual.esquerda
            menor_no_maior_subarvore = self._menor_no(atual.direita)
            atual.dado = menor_no_maior_subarvore.dado
            atual.direita = self._excluir_no(atual.direita, menor_no_maior_subarvore.dado)
        return atual

    def em_ordem(self):
        resultado = []
        self._percorre_em_ordem(self.raiz, resultado)
        return resultado

    def _percorre_em_ordem(self, atual, resultado):
        if atual is not None:
            self._percorre_em_ordem(atual.esquerda, resultado)
            resultado.append(atual.dado)
            self._percorre_em_ordem(atual.direita, resultado)


arvore = ArvoreBinaria()

for valor in [45, 25, 65, 20, 30, 60, 70]:
    arvore.inserir(valor)

print(f"Antes das exclusões: {arvore.em_ordem()}")
arvore.excluir(20)
print(f"Após a exclusão do 20: {arvore.em_ordem()}")
arvore.excluir(25)
print(f"Após a exclusão do 25: {arvore.em_ordem()}")
arvore.excluir(45)
print(f"Após a exclusão do 45: {arvore.em_ordem()}")
