import pygame as pg
from pacote.Entity import Entity
from pacote.PlayerTiro import PlayerTiro
from pacote.constante import ENTIDADE_SPEED, ENTIDADE_TIRO_DELAY, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP, WIN_HEIGHT, WIN_WIDTH


class Player(Entity):
    def __init__(self, nome: str, posicao: tuple):
        super().__init__(nome, posicao)
        self.tiro_delay = ENTIDADE_TIRO_DELAY[self.nome]
    
    def mover(self):
        pressed_key = pg.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.nome]] and self.rect.top > 0:
            self.rect.centery -= ENTIDADE_SPEED[self.nome]
        if pressed_key[PLAYER_KEY_DOWN[self.nome]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTIDADE_SPEED[self.nome]
        if pressed_key[PLAYER_KEY_LEFT[self.nome]] and self.rect.left > 0:
            self.rect.centerx -= ENTIDADE_SPEED[self.nome]
        if pressed_key[PLAYER_KEY_RIGHT[self.nome]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTIDADE_SPEED[self.nome]
        pass

    def atirar(self):
        self.tiro_delay -= 1
        if self.tiro_delay == 0:
            self.tiro_delay = ENTIDADE_TIRO_DELAY[self.nome]
            pressed_key = pg.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.nome]]:
                return PlayerTiro(nome=f'{self.nome}tiro', posicao=(self.rect.centerx, self.rect.centery))
            