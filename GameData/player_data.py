from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from Entities.player import Player

from io import TextIOWrapper

import json

def has_key(dict: dict, key: str) -> bool:

    return key in dict.keys()

def is_empty(dict: dict) -> bool:

    return len(dict) == 0

def load_json(f: TextIOWrapper) -> dict:

    return json.load(f)

def load_data(player: Player) -> Player:

    with open('GameData/player_data.json', 'r') as f:

        file_data: dict = json.load(f)

    if not is_empty(file_data):

        if has_key(file_data, "name"):

            player.set_name(file_data["name"])
        
        if has_key(file_data, "level"):

            player.set_level(file_data["level"])
        
        if has_key(file_data, "max_health"):

            player.set_max_health(file_data["max_health"])
        
        if has_key(file_data, "current_health"):

            player.set_current_health(file_data["current_health"])
        
        if has_key(file_data, "strength"):

            player.set_strength(file_data["strength"])
        
        if has_key(file_data, "moves"):

            player.set_moves(file_data["moves"])

        if has_key(file_data, "exp"):

            player.set_exp(file_data["exp"])

    return player

def save_data(player: Player) -> None:

    saved_data: dict = {

        "name" : player.get_name(),

        "level" : player.get_level(),

        "max_health" : player.get_max_health(),

        "current_health" : player.get_current_health(),

        "strength" : player.get_strength(),

        "moves" : player.get_moves(),

        "exp" : player.get_exp()

    }

    json_str: str = json.dumps(saved_data, indent = 4)

    with open('GameData/player_data.json', 'w') as f:

        f.write(json_str)