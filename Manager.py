import Functions


def start():
    print("######## Bienvenue ########\
            \n\n1. Commencer un tournoi\n2. Reprende un tournoi existant\
            \n3. Rapport des tournois passés\n4. Quitter")
    game_choice = input("\n>> ")
    if game_choice == "1":
        Functions.create_tournament()
    elif game_choice == "2":
        pass
    elif game_choice == "3":
        pass
    elif game_choice == "4":
        pass
