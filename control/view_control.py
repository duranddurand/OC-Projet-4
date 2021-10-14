from .model_control import PlayerControl as Player, TournamentControl as Tournament
from .main_control import MainController as Main


def test_imports():
    print('works')


class ViewController:

    @staticmethod
    def main_menu():
        print("######## Bienvenue ########\
                \n\nT: Tournois \nJ: Joueurs \nQ: Quitter")
        choice = input("\n>> ")

        if choice == "T":
            Main.clear()
            ViewController.tournament_menu()
        elif choice == "J":
            Main.clear()
            ViewController.player_menu()
        elif choice == "Q":
            Main.exit_program()

    @staticmethod
    def player_menu():
        print("######## Joueurs ########\
                \n\n1: Ajouter \n2: Modifier \n3: leaderboard \nR: Retour")
        choice = input("\n>> ")

        if choice == "1":
            Player.create_player()
        elif choice == "2":
            Player.edit_player()
        elif choice == "3":
            ViewController.leaderboard()
        elif choice == "R":
            ViewController.main_menu()
        else:
            pass

    @staticmethod
    def tournament_menu():
        print("######## Tournois ########\
                \n\n1. Nouveau \n2. Reprende \n3. Historique \nR: Retour")
        choice = input("\n>> ")
        if choice == "1":
            Tournament.create_tournament()
        elif choice == "2":
            Tournament.open_tournament()
        elif choice == "3":
            Tournament.tournament_history()
        elif choice == "R":
            ViewController.main_menu()
        else:
            pass

    @staticmethod
    def leaderboard():
        print("######## Leaderboard ########\
                \n\n1: Afficher \n2: Modifier \nR: Retour")
        choice = input("\n>> ")

        if choice == "1":
            Tournament.display_leaderboard()
        elif choice == "2":
            Tournament.edit_leaderboard()
        elif choice == "R":
            ViewController.player_menu()
        else:
            pass
