import pygame as pg

# C
C_BLUE = (46, 119, 153)
C_WHITE = (255, 255, 255)
C_GREEN = (76, 216, 49)
C_YELLOW = (221, 242, 33)
C_PURPLE = (178, 39, 237)
# E
EVENTO_INIMIGO = pg.USEREVENT + 1
ENTIDADE_SPEED = {'imagem0': 0, 'imagem1': 1, 'imagem2': 2,
                  'imagem3': 3, 'player1': 5, 'player1tiro': 8,
                  'player2': 5, 'player2tiro': 9, 'inimigo1': 3,
                  'inimigo2': 2, 'inimigo1tiro': 5, 'inimigo2tiro': 2
                  }
ENTIDADE_HEALTH = {
    'imagem0': 999,
    'imagem1': 999,
    'imagem2': 999,
    'imagem3': 999,
    'player1': 300,
    'player1tiro': 1,
    'player2': 300,
    'player2tiro': 1,
    'inimigo1': 50,
    'inimigo1tiro': 1,
    'inimigo2': 60,
    'inimigo2tiro': 1,
}
ENTIDADE_SCORE = {
    'imagem0': 0,
    'imagem1': 0,
    'imagem2': 0,
    'imagem3': 0,
    'player1': 0,
    'player1tiro': 0,
    'player2': 0,
    'player2tiro': 0,
    'inimigo1': 100,
    'inimigo1tiro': 0,
    'inimigo2': 125,
    'inimigo2tiro': 0,


}

ENTIDADE_TIRO_DELAY = {
    'player1': 30,
    'player2': 10,
    'inimigo1': 70,
    'inimigo2': 90,
}
ENTIDADE_DANO = {
    'imagem0': 0,
    'imagem1': 0,
    'imagem2': 0,
    'imagem3': 0,
    'player1': 1,
    'player1tiro': 25,
    'player2': 1,
    'player2tiro': 20,
    'inimigo1': 1,
    'inimigo1tiro': 20,
    'inimigo2': 1,
    'inimigo2tiro': 15,

}
# P
PLAYER_KEY_UP = {'player1': pg.K_UP,
                 'player2': pg.K_w}
PLAYER_KEY_DOWN = {'player1': pg.K_DOWN,
                   'player2': pg.K_s}
PLAYER_KEY_LEFT = {'player1': pg.K_LEFT,
                   'player2': pg.K_a}
PLAYER_KEY_RIGHT = {'player1': pg.K_RIGHT,
                    'player2': pg.K_d}
PLAYER_KEY_SHOOT = {'player1': pg.K_RCTRL,
                    'player2': pg.K_LCTRL}

# M
MENU_OPCOES = ('NOVO JOGO 1P', 'NOVO JOGO 2P - COOPERATIVO',
               'NOVO JOGO 2P - COMPETITIVO', 'PONTUAÇÃO', 'SAIR')
# S
SPAWN_INIMIGO = 2500
# W
WIN_WIDTH = 512
WIN_HEIGHT = 512
