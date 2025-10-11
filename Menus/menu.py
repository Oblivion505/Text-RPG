from abc import ABC as Abstract, abstractmethod

from Entities.player import Player

# ---------------------------- Menu Abstract Class ----------------------------

class Menu(Abstract):

    # ---------------------------- Attributes ----------------------------

    _player: Player
    _active: bool

    # ---------------------------- Constructor ----------------------------

    def __init__(self) -> None:

        self._active = False
    
    # ---------------------------- Set Methods ----------------------------

    def set_player(self, new_player: Player) -> None:

        self._player = new_player

    def set_active(self, currently_active: bool) -> None:

        self._active = currently_active

    # ---------------------------- Get Methods ----------------------------

    def get_player(self) -> Player:

        return self._player

    def is_active(self) -> bool:

        return self._active
    
    # ---------------------------- Instance Methods ----------------------------

    @abstractmethod
    def activate(self) -> None:
        pass