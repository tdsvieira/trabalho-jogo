from pygame.font import Font
from pygame import Surface
from pygame import Rect
import pygame as pg

from pacote.constante import COLOR_BLUE, COLOR_WHITE, MENU_OPCOES, WIN_WIDTH


class Menu():
    def __init__(self, janela):
        self.janela = janela
        self.surf = pg.image.load('./arquivo/menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pg.mixer_music.load('./arquivo/musica_menu.wav')
        pg.mixer_music.play(-1)
        while True:
            self.janela.blit(source=self.surf, dest=self.rect)
            self.menu_texto(100, 'Combate', COLOR_BLUE, ((WIN_WIDTH / 2), 40))
            self.menu_texto(80, 'Espacial', COLOR_BLUE, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPCOES)):
                self.menu_texto(
                    30, MENU_OPCOES[i], COLOR_WHITE, ((WIN_WIDTH / 2), 500 + 40 * i))

            self.menu_texto(30, 'TIAGO VIEIRA', COLOR_WHITE,
                            ((WIN_WIDTH / 1.2), 720))
            self.menu_texto(30, 'RU:2822630', COLOR_WHITE, ((WIN_WIDTH / 1.2), 745))
            
            pg.display.flip()
            # checa os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

    def menu_texto(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(
            name='Lucida sans Typewhiter', size=text_size)
        text_surf: Surface = text_font.render(
            text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.janela.blit(source=text_surf, dest=text_rect)
