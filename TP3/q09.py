class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None

def percurso_em_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    
    if no:
        percurso_em_ordem(no.esquerdo, resultado)        
        resultado.append(no.valor)        
        percurso_em_ordem(no.direito, resultado)
    
    return resultado

raiz = No(10)
raiz.esquerdo = No(5)
raiz.direito = No(15)
raiz.esquerdo.esquerdo = No(3)
raiz.esquerdo.direito = No(7)
raiz.direito.esquerdo = No(12)
raiz.direito.direito = No(17)

valores_em_ordem = percurso_em_ordem(raiz)
print("Valores da árvore em ordem:", valores_em_ordem)
