from pacote.InimigoTiro import InimigoTiro
from pacote.Entity import Entity
from pacote.Inimigo import Inimigo
from pacote.Player import Player
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
    def __verificar_colisao_entity(ent1, ent2):
        validar_interacao = False
        if isinstance(ent1, Inimigo) and isinstance(ent2, PlayerTiro):
            validar_interacao = True
        elif isinstance(ent1, PlayerTiro) and isinstance(ent2, Inimigo):
            validar_interacao = True
        elif isinstance(ent1, Player) and isinstance(ent2, InimigoTiro):
            validar_interacao = True
        elif isinstance(ent1, InimigoTiro) and isinstance(ent2, Player):
            validar_interacao = True

        if validar_interacao:
            if (ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.dano
                ent2.health -= ent1.dano
                ent1.lest_dmg = ent2.nome
                ent2.lest_dmg = ent1.nome

    @staticmethod
    def __give_score(enemy: Inimigo, entity_list: list[Entity]):
        if enemy.lest_dmg == 'player1tiro':
            for ent in entity_list:
                if ent.nome == 'player1':
                    ent.score += enemy.score
        elif enemy.lest_dmg == 'player2tiro':
            for ent in entity_list:
                if ent.nome == 'player2':
                    ent.score += enemy.score

    @staticmethod
    def verificar_colisao(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verificar_colisao_janela(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verificar_colisao_entity(entity1, entity2)

    @staticmethod
    def verificar_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Inimigo):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
