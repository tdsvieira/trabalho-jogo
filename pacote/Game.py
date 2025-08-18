import pygame as pg  # renomeei o pygame para pg


from pacote.Menu import Menu


class Game:
    def __init__(self):

        pg.init()
        self.janela = pg.display.set_mode(size=(700, 500))

    def run(self,):
        while True:
            menu = Menu(self.janela)
            menu.run
            pass

            # for event in pg.event.get():
            #   if event.type == pg.QUIT:
            #        pg.quit()
            #       quit()
