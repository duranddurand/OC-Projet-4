import os
from model_control import PlayerControl, TournamentControl
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

    def tournament_menu(self):
        Views.print(2)
        choice = input("\n>> ")
        if choice == "1":
            clear()
            Database.tournament_table()
            Database.tournament_table.insert(self.tournament.generate())
        elif choice == "2":
            clear()
            self.tournament.open()
        elif choice == "3":
            clear()
            self.tournament.history()
        elif choice == "4":
            clear()
            MainController.main_menu()
        else:
            pass

    @staticmethod
    def player_menu():
        Views.print(3)
        choice = input("\n>> ")

        if choice == "1":
            Player.create_player()
        elif choice == "2":
            Player.edit_player()
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

