from database_control import Database
from model.tournament_model import Tournament as TournamentModel


class TournamentControl:

    @staticmethod
    def generate():
        tourn = TournamentModel("blabla", "paris", "29/10/2021",\
                                4, [], "Blitz", "super sympa!")

        """name = input("Nom du tournoi: ")
        place = input("Lieu: ")
        date = input("Date du tournoi (Format: jj/mm/aaaa): ")
        rounds = input("Nombre de tours du tournoi: ")
        if rounds == 0:
            rounds = 4
        time_control = input("Contrôle du temps: ")
        description = input("Description: ")
        tournament = TournamentModel(name, place, date, rounds, [], time_control, description)
"""
        print("\n\n1. Confirmer\n2. Refaire\n3. Retour")
        verify = input("\n>>> ")

        if verify == "1":
            Database.in_sert(tourn)
        elif verify == "2":
            pass
        elif verify == "3":
            return 0
        else:
            return 0

    @staticmethod
    def open():
        return 0

    @staticmethod
    def history():
        return 0

    @staticmethod
    def display_leaderboard():
        return 0

    @staticmethod
    def edit_leaderboard():
        return 0

    @staticmethod
    def tournament_players(players):
        all_players = Database.get_all_players
        for player in all_players:
            print(player + ". " + all_players[player])

        selected = []
        count = 0

        while count < 8:
            selection = int(input('Choisissez un joueur:'))
            selected.append(all_players[selection])
            count += 1
        return selected

    @staticmethod
    def pairing_players():
        """pairs = []

        half = len(players) // 2
        leaderboard = sorted(players, \
        key=lambda player: player.get('ranking', {}))

        for rank in range(half):
            pairs.append((leaderboard[rank], \
            leaderboard[rank + half]))
        return pairs"""
        return 0
