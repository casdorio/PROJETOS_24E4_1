class HashtableSimples:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def armazenar(self, chave, valor):
        indice = self._hash(chave)
        self.tabela[indice] = valor

    def recuperar(self, chave):
        indice = self._hash(chave)
        return self.tabela[indice]

perfil1 = {"nome_usuario": "casdorio", "nome_completo": "Carlos Adriano", "email": "casdorio@gmail.com"}
perfil2 = {"nome_usuario": "casdorio2", "nome_completo": "Carlos Adriano 2", "email": "casdorio2@gmail.com"}

hashtable = HashtableSimples()

# Armazenando perfis
hashtable.armazenar("casdorio", perfil1)
hashtable.armazenar("casdorio2", perfil2)

# Recuperando perfis
perfil_recuperado = hashtable.recuperar("casdorio")
if perfil_recuperado:
    print(f"Nome completo: {perfil_recuperado['nome_completo']}, Email: {perfil_recuperado['email']}")
else:
    print("Usuário não encontrado.")
