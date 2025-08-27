from abc import ABC, abstractmethod
import pygame as pg

from pacote.constante import ENTIDADE_DANO, ENTIDADE_HEALTH, ENTIDADE_SCORE


class Entity(ABC):
    def __init__(self, nome: str, posicao: tuple):
        self.nome = nome
        self.surf = pg.image.load('./arquivo/' + nome + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=posicao[0], top=posicao[1])
        self.speed = 0
        self.health = ENTIDADE_HEALTH[self.nome]
        self.dano = ENTIDADE_DANO[self.nome]
        self.score = ENTIDADE_SCORE[self.nome]
        self.lest_dmg = 'None'

    @abstractmethod
    def mover(self, ):
        pass
