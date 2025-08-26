import pygame as pg

# C
COLOR_BLUE = (46, 119, 153)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (76, 216, 49)
# E
EVENTO_INIMIGO = pg.USEREVENT + 1
ENTIDADE_SPEED = {'imagem0': 0, 'imagem1': 1, 'imagem2': 2, 'imagem3': 3, 'player1': 5, 'player2': 5,'inimigo1': 3, 'inimigo2': 2}

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
