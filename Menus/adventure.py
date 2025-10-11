import Utilities.format as Text

from Menus.menu import Menu
from Menus.encounter import Encounter

from Entities.entity import Entity
from Entities.player import Player

# ---------------------------- Adventure Menu Class ----------------------------

class Adventure(Menu):

    # ---------------------------- Constructor ----------------------------

    def __init__(self, player: Player) -> None:
        
        super().__init__()

        self._player = player
    
    # ---------------------------- Instance Methods ----------------------------

    def activate(self) -> None:

        self.set_active(True)

        while self._active:

            Text.options_list("Adventure Menu", ["Continue Your Adventure", "End Your Adventure"])

            option: str = Text.get_input()

            match option:

                case "1":

                    new_enemy = Entity()
                    new_enemy.set_name("Skeleton")
                    new_enemy.set_max_health(50)
                    new_enemy.set_current_health(50)
                    new_enemy.set_strength(20)
                    new_enemy.set_moves(["Basic Attack"])
                    new_enemy.set_exp_value(10)

                    new_encounter = Encounter(self._player, new_enemy)
                    new_encounter.activate()

                    self._player.set_defeated(False)
                    self._player.heal_health(self._player.get_max_health())

                case "2":

                    print("\nYour adventure finally comes to an end...\n")

                    Text.halt()

                    self.set_active(False)