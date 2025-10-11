from __future__ import annotations

from types import FunctionType
import random

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from Entities.entity import Entity


# ---------------------------- Returns specific move function ----------------------------

def get_move(move_name: str) -> FunctionType: 

    move_function: FunctionType = lambda: False

    match move_name:

        case "Basic Attack":

            move_function = basic_attack 
        
        case "Steal":

            move_function = steal

    return move_function

# ---------------------------- Moves ----------------------------

def basic_attack(user: Entity, target: Entity):

    # Min Damage : 50% of user strength. 
    # Max Damage : 150% of user strength.

    damage: int = int(user.get_strength() * 0.5 + (user.get_strength() * random.random())) 
    target.take_damage(damage)

    return damage

def steal(user: Entity, target: Entity):

    # Min Damage : 40% of user strength. 
    # Max Damage : 100% of user strength.
    # Healing    : 10% of target current health (before damage is applied).

    healing: int = int(target.get_current_health() * 0.1)
    user.heal_health(healing)

    damage: int = int(user.get_strength() * 0.4 + (user.get_strength() * random.random()) * 0.6)
    target.take_damage(damage)

    if user.get_type() == "Player":

        print(f'You stole from {target.get_name()} and healed {healing} hp.\n\n')

    elif target.get_type() == "Player":

        print(f'{user.get_name()} stole from you and healed {healing} hp.\n\n')
    
    else:

        print(f'{user.get_name()} stole from {target.get_name()} and healed {healing} hp.\n\n')

    return damage