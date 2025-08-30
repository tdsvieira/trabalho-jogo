import pygame as pg

# C
C_BLUE = (46, 119, 153)
C_WHITE = (255, 255, 255)
C_GREEN = (76, 216, 49)
C_YELLOW = (221, 242, 33)
C_PURPLE = (178, 39, 237)
# E
EVENTO_TIMEOUT = pg.USEREVENT + 2

EVENTO_INIMIGO = pg.USEREVENT + 1

ENTIDADE_SPEED = {'imageml1bg0': 0, 'imageml1bg1': 1, 'imageml1bg2': 2,
                  'imageml1bg3': 3, 'imageml2bg0': 0, 'imageml2bg1': 1,
                  'imageml2bg2': 2, 'imageml2bg3': 3, 'player1': 5, 
                  'player1tiro': 9, 'player2': 5, 'player2tiro': 9, 
                  'inimigo1': 3, 'inimigo2': 2, 'inimigo1tiro': 5, 
                  'inimigo2tiro': 4
                  }
ENTIDADE_HEALTH = {
    'imageml1bg0': 999,
    'imageml1bg1': 999,
    'imageml1bg2': 999,
    'imageml1bg3': 999,
    'imageml2bg0': 999,
    'imageml2bg1': 999,
    'imageml2bg2': 999,
    'imageml2bg3': 999,
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
    'imageml1bg0': 0,
    'imageml1bg1': 0,
    'imageml1bg2': 0,
    'imageml1bg3': 0,
    'imageml2bg0': 0,
    'imageml2bg1': 0,
    'imageml2bg2': 0,
    'imageml2bg3': 0,
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
    'player1': 10,
    'player2': 10,
    'inimigo1': 70,
    'inimigo2': 80,
}
ENTIDADE_DANO = {
    'imageml1bg0': 0,
    'imageml1bg1': 0,
    'imageml1bg2': 0,
    'imageml1bg3': 0,
    'imageml2bg0': 0,
    'imageml2bg1': 0,
    'imageml2bg2': 0,
    'imageml2bg3': 0,
    'player1': 1,
    'player1tiro': 25,
    'player2': 1,
    'player2tiro': 20,
    'inimigo1': 1,
    'inimigo1tiro': 20,
    'inimigo2': 1,
    'inimigo2tiro': 15,

}
# M
MENU_OPCOES = ('NOVO JOGO 1P', 'NOVO JOGO 2P - COOPERATIVO',
               'NOVO JOGO 2P - COMPETITIVO', 'PONTUAÇÃO', 'SAIR')

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
                    'player2': pg.K_LCTRL,
                    }

# S
SPAWN_INIMIGO = 1000
# T
TIMEOUT_NIVEL = 20000  # 20s
TIMEOUT_STEP = 100  # 100 ms
# W
WIN_WIDTH = 512
WIN_HEIGHT = 512
# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }