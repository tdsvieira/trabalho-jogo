from pacote.Entity import Entity
from pacote.InimigoTiro import InimigoTiro
from pacote.constante import ENTIDADE_SPEED, ENTIDADE_TIRO_DELAY


class Inimigo(Entity):
    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)
        self.tiro_delay = ENTIDADE_TIRO_DELAY[self.nome]

    def mover(self):
        self.rect.centerx -= ENTIDADE_SPEED[self.nome]
          
    def atirar(self):
        self.tiro_delay -= 1
        if self.tiro_delay == 0:
            self.tiro_delay = ENTIDADE_TIRO_DELAY[self.nome]
            return InimigoTiro(nome=f'{self.nome}tiro', posicao=(self.rect.centerx, self.rect.centery))