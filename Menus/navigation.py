import GameData.player_data as Player_Data

import Utilities.format as Text

from Menus.menu import Menu
from Menus.adventure import Adventure

from Entities.player import Player

# ---------------------------- Navigation Menu Class ----------------------------

class Navigation(Menu):

    # ---------------------------- Constructor ----------------------------

    def __init__(self, player: Player) -> None:
        
        super().__init__()

        self._player = player
    
    # ---------------------------- Instance Methods ----------------------------

    def activate(self) -> None:

        self.set_active(True)
         
        while self._active:

            Text.options_list("Main Menu", ["View Your Character", "Go On An Adventure", "Save Progress", "Go Back To Start Menu"])
            
            option: str = Text.get_input()

            match option:

                case "1":

                    print(self._player)

                    Text.halt()
                
                case "2":

                    print("\nYou venture into the wilds where danger lurks...\n")

                    Text.halt()

                    adventure_menu: Adventure = Adventure(self._player)
                    adventure_menu.activate()
                
                case "3":

                    Player_Data.save_data(self._player)

                    print("\nProgress successfully saved!\n")
                
                case "4":

                    self.set_active(False)