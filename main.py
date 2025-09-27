from typing import Any

running: bool = True

while running:

    print(  "\nWelcome to my Text Based RPG.\n\n"
      + "Please select an option from the menu by typing the corresponding number:\n\n\n"
      + "--------------------------------------\n"
      + "[1] >> New Game\n"
      + "--------------------------------------\n"
      + "[2] >> Play Game\n"
      + "--------------------------------------\n"
      + "[3] >> Exit Game\n"
      + "--------------------------------------\n")

    option: str = input("Your Input >> ")

    match option:
        case "1":

            print("\nA new game is loading.\n")

        case "2":

            print("\n\n")

        case "3":

            print("\nSaving progress before exit.\n")
            running = False