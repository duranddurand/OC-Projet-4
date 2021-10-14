from model_control import PlayerControl as Player, TournamentControl as Tournament
from view.views import print_view
import os


class Controller:

    @staticmethod
    def main_menu():
        print_view(1)
        choice = input("\n>> ")

        if choice == "1":
            Controller.clear()
            Controller.tournament_menu()
        elif choice == "2":
            Controller.clear()
            Controller.player_menu()
        elif choice == "3":
            Controller.exit_program()

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
            Controller.main_menu()
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
            Controller.leaderboard()
        elif choice == "4":
            Controller.main_menu()
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
            Controller.player_menu()
        else:
            pass

    @staticmethod
    def clear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

    @staticmethod
    def exit_program():
        pass
