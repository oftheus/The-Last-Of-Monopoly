from stateJogador import *
class SobreviventeState(JogadorState):
    def __init__(self):
        return

    def atualizarSuprimentos(self,jogador, s):
        jogador.suprimentos += s
        return s