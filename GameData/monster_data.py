import json
from io import TextIOWrapper

file_data: dict = {}

def load_file() -> None:

    file: TextIOWrapper = open('GameData/monsters.json', 'r')

    global file_data
    file_data = json.load(file)

    file.close()

def get_data(monster_name: str) -> dict:

    monster_data = {}

    if file_data != {}:

        monster_data = file_data[monster_name]

    return monster_data