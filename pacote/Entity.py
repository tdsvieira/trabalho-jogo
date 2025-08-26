from abc import ABC, abstractmethod
import pygame as pg


class Entity(ABC):
    def __init__(self, nome: str, posicao: tuple):
        self.nome = nome
        self.surf = pg.image.load('./arquivo/' + nome + '.png')
        self.rect = self.surf.get_rect(left=posicao[0], top=posicao[1])
        self.speed = 0

    @abstractmethod
    def mover(self, ):
        pass
