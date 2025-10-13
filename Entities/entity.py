from types import FunctionType
from typing import Any
import random

import Gameplay.moves as Moves

# ---------------------------- Entity Class ----------------------------

class Entity():

    # ---------------------------- Attributes ----------------------------

    _type: str

    _name: str
    _level: int
    _max_health: int
    _current_health: int
    _strength: int
    _moves: list
    _cooldown: int
    _exp_value: int
    _defeated: bool

    # ---------------------------- Constructor ----------------------------

    def __init__(self) -> None:

        self._type = "Entity"

        self._name = "entity"

        self._level = 0

        self._max_health = 1
        self._current_health = 1

        self._strength = 1

        self._moves = []
        self._cooldown = 0

        self._exp_value = 0

        self._defeated = False
    
    # ---------------------------- Set Methods ----------------------------
    
    def set_name(self, new_name: str) -> None:

        self._name = new_name

    def set_level(self, new_level: int) -> None:

        self._level = new_level
    
    def set_max_health(self, new_max_health: int) -> None:

        self._max_health = new_max_health

    def set_current_health(self, new_current_health: int) -> None:

        if new_current_health < self._max_health:

            self._current_health = new_current_health
        
        else:

            self._current_health = self._max_health
    
    def set_strength(self, new_strength: int) -> None:

        self._strength = new_strength

    def set_moves(self, new_moves: list) -> None:

        self._moves = new_moves
    
    def set_cooldown(self, new_cooldown: int) -> None:

        self._cooldown = new_cooldown

    def set_exp_value(self, new_exp_value: int) -> None:

        self._exp_value = new_exp_value

    def set_defeated(self, currently_defeated: bool) -> None:

        self._defeated = currently_defeated

    # ---------------------------- Get Methods ----------------------------

    def get_type(self) -> str:

        return self._type

    def get_name(self) -> str:

        return self._name

    def get_level(self) -> int:

        return self._level

    def get_max_health(self) -> int:

        return self._max_health
    
    def get_current_health(self) -> int:

        return self._current_health

    def get_strength(self) -> int:

        return self._strength

    def get_moves(self) -> list:

        return self._moves
    
    def get_cooldown(self) -> int:

        return self._cooldown
    
    def get_exp_value(self) -> int:

        return self._exp_value
    
    def is_defeated(self)-> bool:

        return self._defeated

    # ---------------------------- Instance Methods ----------------------------

    def __str__(self) -> str:

        return f"""
                [====================================]

                    Name: {self._name}

                    Level: {str(self._level)}

                    Max Health: {str(self._max_health)}

                    Current Health: {str(self._current_health)}

                    Strength: {str(self._strength)}

                [====================================]

                
                """

    def short_profile(self) -> str:

        return f"""

                    {self._name} : {self._current_health} / {self._max_health}

                """
    
    def add_move(self, new_move: str) -> None:

        self._moves.append(new_move)
    
    def increment_cooldown(self, new_cooldown: int) -> None:

        self._cooldown += new_cooldown
    
    def pass_turn(self) -> None:

        if self._cooldown > 0:

            self._cooldown -= 1

    def random_move(self) -> str:

        move_choice: str = ""

        if len(self._moves) > 0:

            move_index = random.randint(0, len(self._moves) - 1)

            move_choice = self._moves[move_index]

        return move_choice

    def take_turn(self, opponent: 'Entity', move_name: str) -> Any:

        move: FunctionType = Moves.get_move(move_name)

        return move(self, opponent)

    def take_damage(self, damage: int) -> None:

        if self._current_health > damage:

            self._current_health -= damage
        
        else:

            self._current_health = 0
            self._defeated = True
    
    def heal_health(self, healing: int) -> None:

        if (self._current_health + healing) < self._max_health:

            self._current_health += healing
        
        else:

            self._current_health = self._max_health
