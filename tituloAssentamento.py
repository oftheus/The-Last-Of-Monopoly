from grupoAssentamento import *

class Titulo:
    def __init__(self, valor):
        self.custo = valor
        self.casa = None
        self.jogador = None
        self.comprado = False
        self.grupo = None

    def atribuirAJogador(self, jogador):
        self.jogador = jogador
        self.comprado = True
