import random
import sys
import pygame as pg
from pygame import Surface
from pygame.font import Font
from pacote.EntityMediator import EntityMediator
from pacote.Entity import Entity
from pacote.EntityFactory import EntityFactory
from pacote.Inimigo import Inimigo
from pacote.Player import Player
from pacote.constante import C_PURPLE, C_WHITE, C_YELLOW, EVENTO_INIMIGO, EVENTO_TIMEOUT, MENU_OPCOES, SPAWN_INIMIGO, TIMEOUT_NIVEL, TIMEOUT_STEP, WIN_HEIGHT


class Nivel:
    def __init__(self, janela: Surface, nome: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_NIVEL
        self.janela = janela
        self.nome = nome
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.nome + 'bg'))
        player = (EntityFactory.get_entity('player1'))
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPCOES[1], MENU_OPCOES[2]]:
            player = (EntityFactory.get_entity('player2'))
            player.score = player_score[1]
            self.entity_list.append(player)
        pg.time.set_timer(EVENTO_INIMIGO, SPAWN_INIMIGO)
        pg.time.set_timer(EVENTO_TIMEOUT, TIMEOUT_STEP)

    def run(self,  player_score: list[int]):
        pg.mixer_music.load('./arquivo/musicanivel1.wav')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()

        while True:
            clock.tick(45)
            for ent in self.entity_list:
                self.janela.blit(source=ent.surf, dest=ent.rect)
                ent.mover()
                if isinstance(ent, (Player, Inimigo)):
                    tiro = ent.atirar()
                    if tiro is not None:
                        self.entity_list.append(tiro)
                if ent.nome == 'player1':
                    self.level_texto(
                        14, f'player1 - Vida:{ent.health} | Pontuação: {ent.score}', C_YELLOW, (10, 20))
                if ent.nome == 'player2':
                    self.level_texto(
                        14, f'player2 - Vida:{ent.health} | Pontuação: {ent.score}', C_PURPLE, (10, 30))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENTO_INIMIGO:
                    choice = random.choice(('inimigo1', 'inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENTO_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.nome == 'player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.nome == 'player2':
                                player_score[1] = ent.score
                        return True
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False
            self.level_texto(
                14, f'Nivel: {self.nome} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_texto(
                14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_texto(
                14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pg.display.flip()
            # colisões
            EntityMediator.verificar_colisao(entity_list=self.entity_list)
            EntityMediator.verificar_health(entity_list=self.entity_list)

    def level_texto(self, tamanho: int, texto: str, text_color: tuple, posicao: tuple):
        text_font: Font = pg.font.SysFont(
            name='Lucida Sans Typewriter', size=tamanho)
        text_surface: pg.Surface = text_font.render(
            texto, True, text_color).convert_alpha()
        text_rect: pg.Rect = text_surface.get_rect(
            left=posicao[0], top=posicao[1])
        self.janela.blit(source=text_surface, dest=text_rect)
