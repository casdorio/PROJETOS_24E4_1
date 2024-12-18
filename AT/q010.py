class NavegadorWeb:
    def __init__(self):
        self.pagina_atual = None
        self.pagina_passada = []
        self.pagina_futura = []

    def visitar(self, url):
        if self.pagina_atual:
            self.pagina_passada.append(self.pagina_atual)
        self.pagina_atual = url
        self.pagina_futura.clear()
        print(f"Visitando: {self.pagina_atual}")

    def retroceder(self):
        if self.pagina_passada:
            self.pagina_futura.append(self.pagina_atual)
            self.pagina_atual = self.pagina_passada.pop()
            print(f"Página atual: {self.pagina_atual}")
        else:
            print("Nenhuma página anterior para voltar.")

    def avançar(self):
        if self.pagina_futura:
            self.pagina_passada.append(self.pagina_atual)
            self.pagina_atual = self.pagina_futura.pop()
            print(f"Página atual: {self.pagina_atual}")
        else:
            print("Nenhuma página futura para avançar.")

navegador = NavegadorWeb()
navegador.visitar("exemplo.com")
navegador.visitar("exemplo2.com")
navegador.retroceder()
navegador.avançar()
