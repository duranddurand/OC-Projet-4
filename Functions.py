from Model import Tournament


class Manage:
    def input(self):
        tournament_name = input("Nom du tournoi: ")
        venue = input("Lieu: ")
        tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
        rounds = input("Nombre de tours du tournoi: ")
        if len(rounds) == 0:
            rounds = 4
        timing = input("Contrôle du temps: ")
        description = input("Description: ")
        tournament = Tournament(tournament_name, venue, tournament_date, rounds,timing, [], [], description)

        return tournament


    def pairing(self, t: Tournament):

        leaderboard = []
        pairs = []

        players = t.players_listed()
        half = len(players) // 2
        leaderboard = sorted(players, key=lambda players: players.get('ranking', {}))

        for rank in range(half):
            pairs.append((leaderboard[rank], leaderboard[rank + half]))
        return pairs
