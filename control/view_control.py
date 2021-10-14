from model_control import PlayerControl as Player, TournamentControl as Tournament
from main_control import MainController as Main
from view.views import print_view


class ViewController:

    @staticmethod
    def main_menu():
        print_view(1)
        choice = input("\n>> ")

        if choice == "1":
            Main.clear()
            ViewController.tournament_menu()
        elif choice == "2":
            Main.clear()
            ViewController.player_menu()
        elif choice == "3":
            Main.exit_program()

    @staticmethod
    def tournament_menu():
        print_view(2)
        choice = input("\n>> ")
        if choice == "1":
            Tournament.create_tournament()
        elif choice == "2":
            Tournament.open_tournament()
        elif choice == "3":
            Tournament.tournament_history()
        elif choice == "4":
            ViewController.main_menu()
        else:
            pass

    @staticmethod
    def player_menu():
        print_view(3)
        choice = input("\n>> ")

        if choice == "1":
            Player.create_player()
        elif choice == "2":
            Player.edit_player()
        elif choice == "3":
            ViewController.leaderboard()
        elif choice == "4":
            ViewController.main_menu()
        else:
            pass

    @staticmethod
    def leaderboard():
        print_view(4)
        choice = input("\n>> ")

        if choice == "1":
            Tournament.display_leaderboard()
        elif choice == "2":
            Tournament.edit_leaderboard()
        elif choice == "3":
            ViewController.player_menu()
        else:
            pass
