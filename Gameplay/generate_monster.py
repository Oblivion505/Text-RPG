import random

import GameData.monster_data as Monster_Data

from Entities.entity import Entity
from Entities.player import Player

def initialise_monster(new_entity: Entity, monster_name: str, average_level: int) -> None:

    monster_data: dict = Monster_Data.get_data(monster_name)

    new_entity.set_name(monster_data["name"])
    new_entity.set_exp_value(monster_data["exp_drop"])
    new_entity.set_moves(monster_data["moves"])

    monster_level: int = monster_data["min_level"]

    if average_level > monster_data["min_level"]:

        monster_level += random.randint(0, 5)
    
    if monster_level > monster_data["max_level"]:

        monster_level = monster_data["max_level"]

    new_entity.set_level(monster_level)
    new_entity.set_max_health(monster_data["base_health"] + 10 * monster_level)
    new_entity.set_current_health(new_entity.get_max_health())
    new_entity.set_strength(monster_data["base_strength"] + 5 * monster_level)

def adventure(player: Player) -> Entity:

    new_entity: Entity = Entity()

    rand_num: float = random.randrange(0, 100)

    monster_name: str = ""

    if rand_num < 50:

        monster_name = "Skeleton"

        initialise_monster(new_entity, monster_name, player.get_level())

    elif rand_num < 99:

        monster_name = "Goblin"

        initialise_monster(new_entity, monster_name, player.get_level())

    else:

        monster_name = "Gold Skeleton"

        initialise_monster(new_entity, monster_name, player.get_level())

    return new_entity