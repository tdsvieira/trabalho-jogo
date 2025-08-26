from pacote.Background import Background
from pacote.constante import WIN_WIDTH


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
