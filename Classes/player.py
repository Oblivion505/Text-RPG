from typing import Any

from Classes.entity import Entity

# ---------------------------- Player Class ----------------------------

class Player(Entity):

    # ---------------------------- Attributes ----------------------------

    _level: int
    _exp: int

    # ---------------------------- Constructor ----------------------------

    def __init__(self):

        super().__init__()

        self.set_max_health(100)
        self.set_current_health(100)

        self.set_strength(10)

        self._level = 1
        self._exp = 0

    # ---------------------------- Set Methods ----------------------------

    def set_level(self, new_level: str):

        self._level = new_level
    
    def set_exp(self, new_exp: str):

        self._exp = new_exp

    # ---------------------------- Get Methods ----------------------------

    def get_level(self):

        return self._level
    
    def get_exp(self):

        return self._exp

    # ---------------------------- Class Methods ----------------------------

    def __str__(self):

        return f"""

                Name: {self._name}\n
                Level: {str(self._level)}\n
                Experience Points: {str(self._exp)}\n
                Max Health: {str(self._max_health)}\n
                Current Health: {str(self._current_health)}\n
                Strength: {str(self._strength)}\n
                Defeated: {str(self._defeated)}\n\n

                """
    
    def add_exp(self, exp_amount: int):

        self.set_exp(self._exp + exp_amount)

        if self._exp >= 100:

            levels: int = int(self._exp / 100)

            self.set_exp(self._exp - (100 * levels))

            self.level_up(levels)

    def level_up(self, levels: int):

        self.set_level(self._level + levels)

        health_increase: int = 10 * levels

        self.set_max_health(self._max_health + health_increase)
        self.set_current_health(self._current_health + health_increase)

        strength_increase: int = 5 * levels

        self.set_strength(self._strength + strength_increase)

