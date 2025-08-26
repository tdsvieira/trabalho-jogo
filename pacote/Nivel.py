from pacote.Entity import Entity
from pacote.EntityFactory import EntityFactory
import pygame as pg


class Nivel:
    def __init__(self, janela, nome, game_mode):
        self.janela = janela
        self.nome = nome
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('imagem'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.janela.blit(source=ent.surf, dest=ent.rect)
                ent.mover()
            pg.display.flip()
        pass
