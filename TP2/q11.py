class FilaAtendimento:
    def __init__(self):
        self.fila = []
    
    def adicionar_cliente(self, nome):
        self.fila.append(nome)
    
    def atender_cliente(self):
        if self.fila:
            cliente = self.fila.pop(0)
            print(f"Atendendo cliente: {cliente}")
        else:
            print("Não há clientes na fila.")
    
    def tamanho_fila(self):
        return len(self.fila)
    
    def __str__(self):
        return str(self.fila)
    
fila = FilaAtendimento()
fila.adicionar_cliente("Alice")
fila.adicionar_cliente("João")
fila.adicionar_cliente("Carlos")
fila.adicionar_cliente("David")
print(fila)
fila.atender_cliente()
print(fila)
print(f"Tamanho da fila: {fila.tamanho_fila()}")
fila.atender_cliente()
print(fila)
print(f"Tamanho da fila: {fila.tamanho_fila()}")
fila.atender_cliente()
print(fila)
print(f"Tamanho da fila: {fila.tamanho_fila()}")
fila.atender_cliente()
