import controls


def dashboard():
    print("######## Bienvenue ########\
            \n\nT: Tournois \nJ: Joueurs \nQ: Quitter")
    choice = input("\n>> ")
    if choice == "T":
        tournament()
    elif choice == "J":
        player()
    elif choice == "Q":
        controls.exit_program()


def tournament():
    print("######## Tournois ########\
            \n\n1. Nouveau \n2. Reprende \n3. Historique \nR: Retour")
    choice = input("\n>> ")
    if choice == "1":
        controls.create_tournament()
    elif choice == "2":
        controls.continue_tournament()
    elif choice == "3":
        controls.tournament_history()
    elif choice == "R":
        dashboard()


def player():

    print("######## Joueurs ########\
            \n\n1: Ajouter \n2: Modifier \n3: leaderboard \nR: Retour")
    choice = input("\n>> ")

    if choice == "1":
        controls.create_player()
    elif choice == "2":
        controls.edit_player()
    elif choice == "3":
        leaderboard()
    elif choice == "R":
        dashboard()


def leaderboard():

    print("######## Leaderboard ########\
            \n\n1: Afficher \n2: Modifier \nR: Retour")
    choice = input("\n>> ")

    if choice == "1":
        controls.display_leaderboard()
    elif choice == "2":
        controls.edit_leaderboard()
    elif choice == "R":
        player()