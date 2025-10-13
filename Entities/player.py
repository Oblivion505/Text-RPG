from Entities.entity import Entity

import Utilities.formulas as Formulas

# ---------------------------- Player Class ----------------------------

class Player(Entity):

    # ---------------------------- Attributes ----------------------------

    _exp: int

    # ---------------------------- Constructor ----------------------------

    def __init__(self) -> None:

        super().__init__()

        self._type = "Player"

        self._max_health = 100
        self._current_health = 100

        self._strength = 10

        self._moves = ["Basic Attack"]

        self._exp = 0

    # ---------------------------- Set Methods ----------------------------
    
    def set_exp(self, new_exp: int) -> None:

        self._exp = new_exp

    # ---------------------------- Get Methods ----------------------------
    
    def get_exp(self) -> int:

        return self._exp

    # ---------------------------- Instance Methods ----------------------------

    def __str__(self) -> str:

        return f"""
                [====================================]

                    Name: {self._name}

                    Level: {str(self._level)}

                    Experience Points: {str(self._exp)}

                    Max Health: {str(self._max_health)}

                    Current Health: {str(self._current_health)}

                    Strength: {str(self._strength)}

                [====================================]\n\n
                """

    def add_exp(self, exp_amount: int) -> None:

        self.set_exp(self._exp + exp_amount)

        if self._exp >= 100:

            levels: int = int(self._exp / 100)

            self.set_exp(self._exp - (100 * levels))

            self.level_up(levels)
    
    def exp_from_monster(self, monster: Entity) -> None:

        exp_gained: int = 0

        if monster.get_level() >= self._level:

            exp_gained = monster.get_exp_value()
        
        else:

            exp_gained = int(monster.get_exp_value() / 2)
        
        self.add_exp(exp_gained)

    def level_up(self, levels: int) -> None:

        self.set_level(self._level + levels)

        new_health: int = Formulas.health_increase(self._max_health, levels)

        self.set_max_health(new_health)

        new_strength: int = Formulas.strength_increase(self._strength, levels)

        self.set_strength(new_strength)