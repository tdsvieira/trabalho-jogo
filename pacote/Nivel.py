import random
import sys
from pygame.font import Font
from pacote.Entity import Entity
from pacote.EntityFactory import EntityFactory
import pygame as pg

from pacote.constante import COLOR_WHITE, EVENTO_INIMIGO, MENU_OPCOES, SPAWN_INIMIGO, WIN_HEIGHT


class Nivel:
    def __init__(self, janela, nome, game_mode):
        self.timeout = 20000  # 20 segundos
        self.janela = janela
        self.nome = nome
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('imagem'))
        self.entity_list.append(EntityFactory.get_entity('player1'))
        if game_mode in [MENU_OPCOES[1], MENU_OPCOES[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2'))
        pg.time.set_timer(EVENTO_INIMIGO, SPAWN_INIMIGO)

    def run(self, ):
        pg.mixer_music.load('./arquivo/musicanivel1.wav')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()

        while True:
            clock.tick(45)
            for ent in self.entity_list:
                self.janela.blit(source=ent.surf, dest=ent.rect)
                ent.mover()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENTO_INIMIGO:
                    choice = random.choice(('inimigo1', 'inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_texto(
                14, f'Nivel: {self.nome}- Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_texto(
                14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_texto(
                14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pg.display.flip()
        pass

    def level_texto(self, tamanho: int, texto: str, text_color: tuple, posicao: tuple):
        text_font: Font = pg.font.SysFont(
            name='Lucida Sans Typewriter', size=tamanho)
        text_surface: pg.Surface = text_font.render(
            texto, True, text_color).convert_alpha()
        text_rect: pg.Rect = text_surface.get_rect(
            left=posicao[0], top=posicao[1])
        self.janela.blit(source=text_surface, dest=text_rect)
