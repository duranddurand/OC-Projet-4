from database_control import Database
from model.tournament_model import Tournament as TournamentModel
from model.player_model import Player


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
            Database.insert_in_db(tourn)
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
    def pairing_players(tournament):
        turn = Database.get_played_turns(tournament)
        if turn == 1:
            players.sort(key=lambda p: p['ranking'])

        else:
            players = Database('Tournament').get_played_turns(tournament)
            players.sort(key=lambda p: (p['ranking'], p['score']))

        half = len(players) // 2

        alpha = players[:half]
        beta = players[half:]

        pairs = zip(alpha, beta)

        return pairs


tourn = TournamentModel("blabla", "paris", "29/10/2021", 4, [], "Blitz", "super sympa!")
player1 = Player("joe1", "sddkfo", "20/10/2002", "M", 1, 500).serialized()
player2 = Player("joe2", "sddkfo", "20/10/2002", "M", 2, 500).serialized()
player3 = Player("joe3", "sddkfo", "20/10/2002", "M", 3, 500).serialized()
player4 = Player("joe4", "sddkfo", "20/10/2002", "M", 4, 500).serialized()
player5 = Player("joe5", "sddkfo", "20/10/2002", "M", 5, 500).serialized()
player6 = Player("joe6", "sddkfo", "20/10/2002", "M", 6, 500).serialized()
player7 = Player("joe7", "sddkfo", "20/10/2002", "M", 7, 500).serialized()
player8 = Player("joe8", "sddkfo", "20/10/2002", "M", 8, 500).serialized()
players = [player1, player2, player3, player4, player5, player6, player7, player8]
result = TournamentControl.pairing_players(players)
Database.insert_turn(turn)
print(*result)