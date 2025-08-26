from pacote.Entity import Entity
from pacote.Inimigo import Inimigo


class EntityMediator:

    @staticmethod
    def __verificar_colisao_janela(ent: Entity):
        if isinstance(ent, Inimigo):
            if ent.rect.right < 0:
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
