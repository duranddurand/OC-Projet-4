from Model.tournament_model import Tournament as T


class TurnControl:
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
        tournament = T(name, place, date, rounds, [], timing, description)

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
    def continue_tournament():
        return 0\

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
    def pairing():
        '''pairs = []

        half = len(players) // 2
        leaderboard = sorted(players, key=lambda player: player.get('ranking', {}))

        for rank in range(half):
            pairs.append((leaderboard[rank], leaderboard[rank + half]))
        return pairs'''