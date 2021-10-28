import os
from player_control import PlayerControl
from tournament_control import TournamentControl
from views import Views
from database_control import Database


class MainController:

    def __init__(self):
        self.player = PlayerControl
        self.tournament = TournamentControl
        self.view = Views

    @staticmethod
    def main_menu():
        Views.print(1)
        choice = input("\n>> ")

        if choice == "1":
            clear()
            MainController.tournament_menu()
        elif choice == "2":
            clear()
            MainController.player_menu()
        elif choice == "3":
            exit_program()
        return 0

    @staticmethod
    def tournament_menu():
        Views.print(2)
        choice = input("\n>> ")
        if choice == "1":
            clear()
            TournamentControl.generate()
        elif choice == "2":
            clear()
            TournamentControl.open()
        elif choice == "3":
            clear()
            TournamentControl.history()
        elif choice == "4":
            clear()
            MainController.main_menu()
        else:
            pass

    def player_menu(self):
        Views.print(3)
        choice = input("\n>> ")

        if choice == "1":
            clear()
            new = self.player.generate()
        elif choice == "2":
            Player.edit()
        elif choice == "3":
            MainController.leaderboard()
        elif choice == "4":
            MainController.main_menu()
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
            MainController.player_menu()
        else:
            pass


def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def exit_program():
    return 0
    pass

