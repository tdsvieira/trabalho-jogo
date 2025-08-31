from pygame.font import Font
from pygame import Surface
from pygame import Rect
import pygame as pg

from pacote.constante import (
    C_BLUE,
    C_GREEN,
    C_WHITE,
    MENU_OPCOES,
    WIN_WIDTH
)


class Menu():
    def __init__(self, janela):
        # desenhei as imagens
        self.janela = janela
        self.surf = pg.image.load('./arquivo/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_opcoes = 0
        pg.mixer_music.load('./arquivo/musica_menu.wav')
        pg.mixer_music.play(-1)
        while True:
            self.janela.blit(source=self.surf, dest=self.rect)
            self.menu_texto(80, 'Combate', C_BLUE, ((WIN_WIDTH / 2), 40))
            self.menu_texto(50, 'Espacial', C_BLUE, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPCOES)):
                if i == menu_opcoes:
                    self.menu_texto(
                            30,
                            MENU_OPCOES[i],
                            C_GREEN,
                            ((WIN_WIDTH / 2), 280 + 40 * i)
                        )
                else:
                    self.menu_texto(
                            30,
                            MENU_OPCOES[i],
                            C_WHITE,
                            ((WIN_WIDTH / 2), 280 + 40 * i)
                        )

            # o titulo de cima
            self.menu_texto(30, 'TIAGO VIEIRA', C_WHITE,
                            ((WIN_WIDTH / 1.2), 450))
            self.menu_texto(30, 'RU:2822630', C_WHITE,
                            ((WIN_WIDTH / 1.2), 480))
            
            pg.display.flip()

            # checa os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if (
                        event.key
                        == pg.K_DOWN  # verifica se é a tecla para baixo
                    ):
                        if menu_opcoes < len(MENU_OPCOES) - 1:
                            menu_opcoes += 1
                        else:
                            menu_opcoes = 0
                    if event.key == pg.K_UP:  # verifica se é a tecla para cima
                        if menu_opcoes > 0:
                            menu_opcoes -= 1
                        else:
                            menu_opcoes = len(MENU_OPCOES) - 1
                    if event.key == pg.K_RETURN:  # entrar
                        return MENU_OPCOES[menu_opcoes]

    def menu_texto(
        self,
        text_size: int,
        text: str,
        text_color: tuple,
        text_center_pos: tuple
    ):
        text_font: Font = pg.font.SysFont(
            name='Lucida sans Typewhiter', size=text_size)
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.janela.blit(source=text_surf, dest=text_rect)
