class Casa:
    
    #Funções de cada subclasse de casa implementadas através de polimorfismo
    def __init__(self, id, distanceToNext, name):
        self.id = id
        self.distanceToNext = distanceToNext
        self.name = name

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        jogador.suprimentos = jogador.suprimentos - 200
        return
    
    def drawCasa(self, coord, fonte, fonteFortaleza, screen): #deve ser implementado na casa
        return
       