from pacote.Entity import Entity
from pacote.constante import ENTIDADE_SPEED


class InimigoTiro(Entity):
    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)

    def mover(self):
        self.rect.centerx -= ENTIDADE_SPEED[self.nome]
        