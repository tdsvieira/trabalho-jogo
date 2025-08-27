from pacote.InimigoTiro import InimigoTiro
from pacote.Entity import Entity
from pacote.Inimigo import Inimigo
from pacote.PlayerTiro import PlayerTiro
from pacote.constante import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verificar_colisao_janela(ent: Entity):
        if isinstance(ent, Inimigo):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerTiro):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, InimigoTiro):
            if ent.rect.right <= 0:
                ent.health = 0
   
    @staticmethod
    def verificar_colisao(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verificar_colisao_janela(test_entity)

    @staticmethod
    def verificar_health(entity_list: list[Entity]): 
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
