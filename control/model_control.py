from model.tournament_model import Tournament as TournamentModel
from model.player_model import Player as PlayerModel
from views import print_view


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

    @staticmethod
    def serialize_player(player):
        player_in_dict = {
            'id': player.id,
            'nom': player.name,
            'surname': player.surname,
            'birthdate': player.birthdate,
            'gender': player.gender,
            'ranking': player.ranking
        }

        return player_in_dict




class TournamentControl:
    @staticmethod
    def generate():
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
        print("Decompte: " + str(len(players)))
        print_view(6)
        while len(players) < 8:
            val = input("\n: ")
            if val == "1":
                PlayerControl.create_player()
            elif val == "2":
                PlayerControl.add_player()
            elif val == "3":
                return 0
            else:
                pass

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
