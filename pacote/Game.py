import pygame as pg  # renomeei o pygame para pg


from pacote.Menu import Menu
from pacote.constante import WIN_HEIGTH, WIN_WIDTH


class Game:
    def __init__(self):

        pg.init()
        self.janela = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))
        pg.display.set_caption('Combate Espacial')

    def run(self,):
        while True:
            menu = Menu(self.janela)
            menu.run()
            pass
