import pygame as pg  # renomeei o pygame para pg

print('inicio do programa')
pg.init()
janela = pg.display.set_mode(size=(700, 500))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

