from Menus.menu import Menu

from Entities.player import Player
from Entities.entity import Entity

import Utilities.format as Text

# ---------------------------- Encounter Class ----------------------------

class Encounter(Menu):

    # ---------------------------- Attributes ----------------------------

    _opponent: Entity
    _round_num: int

    # ---------------------------- Constructor ----------------------------

    def __init__(self, player: Player, opponent: Entity) -> None:

        super().__init__()

        self._player = player
        self._opponent = opponent

        self._round_num = 1

    # ---------------------------- Set Methods ----------------------------
    
    def set_opponent(self, new_opponent: Entity) -> None:

        self._opponent = new_opponent
    
    def set_round(self, new_round: int) -> None:

        self._round_num = new_round

    # ---------------------------- Get Methods ----------------------------

    def get_opponent(self) -> Entity:

        return self._opponent

    def get_round(self) -> int:

        return self._round_num
    
    # ---------------------------- Instance Methods ----------------------------

    def increment_rounds(self) -> None:

        self.set_round(self._round_num + 1)

    def activate(self) -> None:

        print(f'\n <========|- You have encountered {self._opponent.get_name()}. -|========>\n\n')
        Text.halt()

        self.set_active(True)

        player: Player = self.get_player()
        opponent: Entity = self.get_opponent()

        while self._active:

            print(f'-------------------------------------- Turn {self._round_num} --------------------------------------')

            print(player.short_profile())
            print(opponent.short_profile())

            Text.options_list("Encounter Menu", ["Fight", "See Opponent's Stats", "See your Stats", "Run Away"])

            option: str = Text.get_input()

            match option:

                case "1":

                    print("\nYou choose to fight.\n")

                    damage_dealt: int = player.take_turn(opponent, player.get_moves()[0])

                    print(f'\nYou dealt {damage_dealt} damage.\n\n')

                    if opponent.is_defeated():

                        print(f'\nYou have defeated {opponent.get_name()}.')
                        print(f'\nTotal Turns: {self.get_round()}\n\n')

                        player.exp_from_monster(opponent)

                        self.set_active(False)
                    
                    else:

                        damage_taken: int = opponent.take_turn(player, opponent.random_move())

                        print(f'You received {damage_taken} damage.\n\n')

                        if player.is_defeated():

                            print(f'\n{opponent.get_name()} has defeated you.')
                            print(f'\nTotal Turns: {self.get_round()}\n\n')

                            self.set_active(False)

                    self.increment_rounds()
                    
                case "2":

                    print(opponent)
                
                case "3":

                    print(player)

                case "4":

                    print("\nSuccessfully Ran Away.\n")
                    self.set_active(False)

            Text.halt()