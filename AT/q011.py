import sys
sys.stdout.reconfigure(encoding='utf-8')

class Fila:
    def __init__(self):
        self.elementos = []

    def adicionar_cliente(self, cliente):
        self.elementos.append(cliente)

    def atender_cliente(self):
        if not self.elementos:
            print("A fila está vazia.")
            return None
        return self.elementos.pop(0)

    def exibir_fila(self):
        if not self.elementos:
            print("A fila está vazia.")
        else:
            print(", ".join(self.elementos))

fila_de_atendimento = Fila()
fila_de_atendimento.adicionar_cliente("Lucas Oliveira")
fila_de_atendimento.adicionar_cliente("Ana Souza")

print('- Fila inicial:')
fila_de_atendimento.exibir_fila()
fila_de_atendimento.atender_cliente()
print('- Fila após Lucas Oliveira ser atendido:')
fila_de_atendimento.exibir_fila()
