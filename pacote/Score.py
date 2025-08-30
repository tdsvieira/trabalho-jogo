from datetime import datetime
import sys
import pygame as pg
from pygame import K_BACKSPACE, K_ESCAPE, K_RETURN, Surface, Rect, KEYDOWN
from pygame.font import Font
from pacote.DBproxy import DBproxy
from pacote.constante import C_WHITE, C_YELLOW, MENU_OPCOES, SCORE_POS


class Score:
    def __init__(self, janela: Surface):
        self.janela = janela
        self.surf = pg.image.load('./arquivo/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pg.mixer_music.load('./arquivo/score.wav')
        pg.mixer_music.play(-1)
        db_proxy = DBproxy('DBScore')
        nome = ''
        while True:
            self.janela.blit(source=self.surf, dest=self.rect)
            self.score_texto(48, 'VOCE GANHOU!!', C_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPCOES[0]:
                score = player_score[0] 
                texto = 'Jogador 1 Digite seu nome:(4 digitos):'
            if game_mode == MENU_OPCOES[1]:
                score = (player_score[0] + player_score[1]) / 2
                texto = 'Digite o nome do time:(4 digitos):'
            if game_mode == MENU_OPCOES[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    texto = 'Digite o nome do jogador 1(4 digitos):'
                else:
                    score = player_score[1]
                    texto = 'Digite o nome do jogador 2(4 digitos):'
            self.score_texto(20, texto, C_WHITE, SCORE_POS['EnterName'])
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(nome) == 4:
                        db_proxy.save({'name': nome, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        nome = nome[:-1]
                    else:
                        if len(nome) < 4:
                            nome += event.unicode
            self.score_texto(20, nome, C_WHITE, SCORE_POS['Name'])
            pg.display.flip()
            pass

    def show(self):
        pg.mixer_music.load('./arquivo/score.wav')
        pg.mixer_music.play(-1)
        self.janela.blit(source=self.surf, dest=self.rect)
        self.score_texto(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_texto(20, 'NAME     SCORE           DATE      ', C_WHITE, SCORE_POS['Label'])
        db_proxy = DBproxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()
        for  player_score in list_score:
            id_, name, score, date = player_score
            self.score_texto(20, f'{name}     {score:05d}     {date}', C_WHITE,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pg.display.flip()
            
    def score_texto(self, tamanho: int, texto: str, text_color: tuple, posicao: tuple):
        text_font: Font = pg.font.SysFont(
            name='Lucida Sans Typewriter', size=tamanho)
        text_surface: Surface = text_font.render(
            texto, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(
            center=posicao)
        self.janela.blit(source=text_surface, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"