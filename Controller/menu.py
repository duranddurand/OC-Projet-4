import os
from player_controller import PlayerControl as P
from tournament_controller import TurnControl as T

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


class Controller:

    def main(self):
        print("######## Bienvenue ########\
                \n\nT: Tournois \nJ: Joueurs \nQ: Quitter")
        choice = input("\n>> ")

        if choice == "T":
            clear()
            self.tournament()
        elif choice == "J":
            clear()
            self.player()
        elif choice == "Q":
            clear()
            self.exit_program()

    def tournament(self):
        print("######## Tournois ########\
                \n\n1. Nouveau \n2. Reprende \n3. Historique \nR: Retour")
        choice = input("\n>> ")
        if choice == "1":
            T.create_tournament()
        elif choice == "2":
            T.continue_tournament()
        elif choice == "3":
            T.tournament_history()
        elif choice == "R":
            self.main()
        else:
            pass

    def player(self):
        print("######## Joueurs ########\
                \n\n1: Ajouter \n2: Modifier \n3: leaderboard \nR: Retour")
        choice = input("\n>> ")

        if choice == "1":
            P.create_player()
        elif choice == "2":
            P.edit_player()
        elif choice == "3":
            self.leaderboard()
        elif choice == "R":
            self.main()
        else:
            pass

    def leaderboard(self):
        print("######## Leaderboard ########\
                \n\n1: Afficher \n2: Modifier \nR: Retour")
        choice = input("\n>> ")

        if choice == "1":
            T.display_leaderboard()
        elif choice == "2":
            T.edit_leaderboard()
        elif choice == "R":
            self.player()
        else:
            pass

    @staticmethod
    def exit_program():
        pass


Controller.main()