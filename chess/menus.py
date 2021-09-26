from controls import *


def dashboard() -> object:
    print("######## Bienvenue ########\
            \n\nT: Tournois \nJ: Joueurs \nQ: Quitter")
    choice = input("\n>> ")
    if choice == "T":
        tournament()
    elif choice == "J":
        player()
    elif choice == "Q":
        pass

    return 0


def tournament():
    print("######## Tournois ########\
            \n\n1. Nouveau \n2. Reprende \n3. Historique \nQ: Quitter")
    choice = input("\n>> ")
    if choice == "1":
        create_tournament()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "Q":
        pass


def player():

    print("######## Joueurs ########\
            \n\n1: Ajouter \n2: Modifier \n3: leaderboard \nQ: Quitter")
    choice = input("\n>> ")

    if choice == "1":
        create_players()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "Q":
        pass
