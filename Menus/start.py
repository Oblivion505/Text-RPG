import GameData.player_data as Player_Data

import Utilities.format as Text

from Menus.menu import Menu
from Menus.navigation import Navigation

from Entities.player import Player

# ---------------------------- Start Menu Class ----------------------------

class Start(Menu):

    # ---------------------------- Constructor ----------------------------

    def __init__(self) -> None:
        
        super().__init__()
    
    # ---------------------------- Instance Methods ----------------------------

    def activate(self) -> None:
         
        self.set_active(True)
         
        while self._active:

            Text.options_list("Start Menu", ["New Game", "Load Game", "Exit Game"])
             
            option: str = Text.get_input()

            if option == "2":

                file_data: dict = {}

                with open('GameData/player_data.json', 'r') as f:

                    file_data = Player_Data.load_json(f)

                if Player_Data.is_empty(file_data):

                    option = "1"

            match option:
        
                case "1":

                    print("\nPlease enter the name of your character:\n")

                    name: str = Text.get_input()

                    new_player: Player = Player()
                    new_player.set_name(name)

                    navigation_menu: Navigation = Navigation(new_player)
                    navigation_menu.activate()
                
                case "2":

                    new_player: Player = Player()

                    new_player = Player_Data.load_data(new_player)

                    print("\nProgress successfully loaded!\n")

                    navigation_menu: Navigation = Navigation(new_player)
                    navigation_menu.activate()

                case "3":

                    print("\n--[[Exiting Game]]--\n")

                    self.set_active(False)