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
        
        case "Claw Strike":

            move_function = claw_strike
        
        case "Fire Breath":

            move_function = fire_breath

        case "Devour":

            move_function = devour

    return move_function

# ---------------------------- Moves ----------------------------

def basic_attack(user: Entity, target: Entity):

    # Min Damage : 80% of user strength. 
    # Max Damage : 120% of user strength.

    damage: int = int(user.get_strength() * 0.8 + (user.get_strength() * random.random() * 0.4)) 
    target.take_damage(damage)

    return damage

def steal(user: Entity, target: Entity):

    # Min Damage : 40% of user strength. 
    # Max Damage : 80% of user strength.
    # Healing    : 10% of target current health (before damage is applied).

    healing: int = int(target.get_current_health() * 0.1)
    user.heal_health(healing)

    damage: int = int(user.get_strength() * 0.4 + (user.get_strength() * random.random()) * 0.4)
    target.take_damage(damage)

    if user.get_type() == "Player":

        print(f'You stole from {target.get_name()} and healed {healing} hp.\n\n')

    elif target.get_type() == "Player":

        print(f'{user.get_name()} stole from you and healed {healing} hp.\n\n')
    
    else:

        print(f'{user.get_name()} stole from {target.get_name()} and healed {healing} hp.\n\n')

    return damage

def claw_strike(user: Entity, target: Entity):

    # Damage : 100% of user's strength.

    damage: int = int(user.get_strength())
    target.take_damage(damage)

    return damage

def fire_breath(user: Entity, target: Entity):

    # Min Damage: 40% of user's current health.
    # Max Damage: 60% of user's current health.

    damage: int = int(user.get_current_health() * 0.4 + (user.get_current_health() * random.random() * 0.2))
    target.take_damage(damage)

    if target.get_type() == "Player":

        print(f'You are consumed by dragon fire.\n\n')
    
    else:

        print(f'{target.get_name()} is consumed by dragon fire.\n\n')

    return damage

def devour(user: Entity, target: Entity):

    # Damage: 25% of target's max health.

    damage: int = int(target.get_max_health() * 0.25)
    target.take_damage(damage)

    if user.get_type() == "Player":

        print(f'{target.get_name()} is being devoured by you.\n\n')

    elif target.get_type() == "Player":

        print(f'You are being devoured by {user.get_name()}.\n\n')
    
    else:

        print(f'{target.get_name()} is being devoured by {user.get_name()}.\n\n')

    return damage