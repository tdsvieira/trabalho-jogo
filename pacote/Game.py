import pygame as pg  # renomeei o pygame para pg


from pacote.Menu import Menu
from pacote.Nivel import Nivel
from pacote.constante import MENU_OPCOES, WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):

        pg.init()
        self.janela = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pg.display.set_caption('Combate Espacial')

    def run(self,):
        while True:
            menu = Menu(self.janela)
            menu_retorno = menu.run()
            if menu_retorno in [MENU_OPCOES[0], MENU_OPCOES[1], MENU_OPCOES[2]]:
                nivel = Nivel(self.janela, 'Nivel1', menu_retorno)
                nivel_retorno = nivel.run()
            elif menu_retorno == MENU_OPCOES[4]:
                pg.quit()
                quit()
            else:
                pass 
