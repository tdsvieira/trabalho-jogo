import random
from pacote.Inimigo import Inimigo
from pacote.Player import Player
from pacote.Background import Background
from pacote.constante import WIN_HEIGHT, WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_nome: str, posicao=(0, 0)):
        match entity_nome:
            case 'imagem':
                lista_nu = []
                for i in range(4):
                    lista_nu.append(Background(f'imagem{i}', (0, 0)))
                    lista_nu.append(Background(f'imagem{i}', (WIN_WIDTH, 0)))
                return lista_nu
            case 'player1':
                return Player('player1', (10, WIN_HEIGHT / 2 - 30))
            case 'player2':
                return Player('player2', (10, WIN_HEIGHT / 2 + 30))
            case 'inimigo1':
                return Inimigo('inimigo1', (WIN_WIDTH + 10, random.randint(10, WIN_HEIGHT - 10)))
            case 'inimigo2':
                return Inimigo('inimigo2', (WIN_WIDTH + 10, random.randint(10, WIN_HEIGHT - 10)))
