class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
    
    def inserir(self, chave, valor):
        posicao = hash(chave) % self.tamanho
        self.tabela[posicao].append((chave, valor))
    
    def buscar(self, chave):
        posicao = hash(chave) % self.tamanho
        
        for item in self.tabela[posicao]:
            if item[0] == chave:
                return item[1]
        
        return None
    
    def remover(self, chave):
        posicao = hash(chave) % self.tamanho
        
        for i, item in enumerate(self.tabela[posicao]):
            if item[0] == chave:
                del self.tabela[posicao][i]
                return True
        
        return False
    
    def __str__(self):
        return str(self.tabela)
    
tabela = TabelaHash(10)

tabela.inserir("Alice", 25)
tabela.inserir("João", 30)
tabela.inserir("Carlos", 35)
tabela.inserir("David", 40)
print(tabela)
print(tabela.buscar("Alice"))
print(tabela.buscar("João"))
print(tabela.buscar("Carlos"))
print(tabela.buscar("David"))
print(tabela.buscar("Maria"))
print(tabela.remover("Carlos"))
print(tabela)
print(tabela.remover("Maria"))
print(tabela)
print(tabela.remover("Alice"))
print(tabela)
print(tabela.remover("David"))
print(tabela)
