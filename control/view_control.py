from model_control import PlayerControl
from model_control import TournamentControl
from main_control import MainController as Main


class Controller:

    @staticmethod
    def main_menu():
        print("######## Bienvenue ########\
                \n\nT: Tournois \nJ: Joueurs \nQ: Quitter")
        choice = input("\n>> ")

        if choice == "T":
            Main.clear()
            Controller.tournament_menu()
        elif choice == "J":
            Main.clear()
            Controller.player_menu()
        elif choice == "Q":
            Main.exit_program()

    @staticmethod
    def player_menu():
        print("######## Joueurs ########\
                \n\n1: Ajouter \n2: Modifier \n3: leaderboard \nR: Retour")
        choice = input("\n>> ")

        if choice == "1":
            PlayerControl.create_player()
        elif choice == "2":
            PlayerControl.edit_player()
        elif choice == "3":
            Controller.leaderboard()
        elif choice == "R":
            Controller.main_menu()
        else:
            pass

    @staticmethod
    def leaderboard():
        print("######## Leaderboard ########\
                \n\n1: Afficher \n2: Modifier \nR: Retour")
        choice = input("\n>> ")

        if choice == "1":
            TournamentControl.display_leaderboard()
        elif choice == "2":
            TournamentControl.edit_leaderboard()
        elif choice == "R":
            Controller.player_menu()
        else:
            pass

    @staticmethod
    def tournament_menu():
        print("######## Tournois ########\
                \n\n1. Nouveau \n2. Reprende \n3. Historique \nR: Retour")
        choice = input("\n>> ")
        if choice == "1":
            TournamentControl.create_tournament()
        elif choice == "2":
            TournamentControl.open_tournament()
        elif choice == "3":
            TournamentControl.tournament_history()
        elif choice == "R":
            Controller.main_menu()
        else:
            pass
