# A module that contains useful functions for displaying structured text in the command line.

TEXT_ENHANCEMENT: dict = {

    "bold" : '\033[1m',

    "end" : '\033[0m'

}

def get_input() -> str:

    return input("Your Input >> ")

def halt() -> None:

    input("-- Press Enter To Continue -- ")

def options_list(list_name: str, options: list[str]) -> None:

    output: str = "\n"
    
    #output += "\n--------------------------------------\n"

    output += TEXT_ENHANCEMENT["bold"] + f'// {list_name} //\n' + TEXT_ENHANCEMENT["end"]

    output += "--------------------------------------\n"

    for option in options:

        output += f'[{options.index(option) + 1}] >> {option}\n'

        output += "--------------------------------------\n"

    print(output)