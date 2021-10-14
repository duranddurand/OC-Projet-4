from model.tournament_model import Model as TournamentModel
from model.player_model import Model as PlayerModel


class PlayerControl:

    @staticmethod
    def create_player():
        name = input("Prénom du joueur:")
        surname = input("Nom du joueur:")
        birthdate = input("Date de naissance:")
        gender = input("sexe:")
        ranking = input("classement du joueur:")

        player = PlayerModel(name, surname, birthdate, gender, ranking)

        return player

    @staticmethod
    def edit_player():
        return 0

    @staticmethod
    def add_player():
        return 0


class TournamentControl:
    @staticmethod
    def create_tournament():
        name = input("Nom du tournoi: ")
        place = input("Lieu: ")
        date = input("Date du tournoi (Format: jj/mm/aaaa): ")
        rounds = input("Nombre de tours du tournoi: ")
        if rounds == 0:
            rounds = 4
        timing = input("Contrôle du temps: ")
        description = input("Description: ")
        tournament = TournamentModel(name, place, date, rounds, [], timing, description)

        print("\n\n1. Confirmer\n2. Refaire\n3. Retour")
        verify = input("\n>>> ")
        if verify == "1":
            pass
        elif verify == "2":
            pass
        elif verify == "3":
            return 0
        else:
            pass

        return tournament

    @staticmethod
    def open_tournament():
        return 0

    @staticmethod
    def tournament_history():
        return 0

    @staticmethod
    def display_leaderboard():
        return 0

    @staticmethod
    def edit_leaderboard():
        return 0

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
