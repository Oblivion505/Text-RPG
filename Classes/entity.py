from typing import Any

# ---------------------------- Entity Class ----------------------------

class Entity():

    # ---------------------------- Attributes ----------------------------

    _name: str
    _max_health: int
    _current_health: int
    _strength: int
    _defeated: bool

    # ---------------------------- Constructor ----------------------------

    def __init__(self):

        self._name = "Entity"

        self._max_health = 1
        self._current_health = 1

        self._strength = 1

        self._defeated = False
    
    # ---------------------------- Set Methods ----------------------------
    
    def set_name(self, new_name: str):

        self._name = new_name
    
    def set_max_health(self, new_max_health: int):

        self._max_health = new_max_health

    def set_current_health(self, new_current_health: int):

        self._current_health = new_current_health
    
    def set_strength(self, new_strength: int):

        self._strength = new_strength

    def set_defeated(self, is_defeated: bool):

        self._defeated = is_defeated

    # ---------------------------- Get Methods ----------------------------

    def get_name(self):

        return self._name

    def get_max_health(self):

        return self._max_health
    
    def get_current_health(self):

        return self._current_health

    def get_strength(self):

        return self._strength
    
    def get_defeated(self):

        return self._defeated

    # ---------------------------- Class Methods ----------------------------

    def __str__(self):

        return f"""

                Name: {self._name}\n
                Max Health: {str(self._max_health)}\n
                Current Health: {str(self._current_health)}\n
                Strength: {str(self._strength)}\n
                Defeated: {str(self._defeated)}\n\n

                """
               
    def take_damage(self, damage: int):

        if self._current_health > damage:

            self._current_health -= damage
        
        else:

            self._current_health = 0
            self._defeated = True
