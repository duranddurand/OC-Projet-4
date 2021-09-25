from model import Tournament, Player


def create_tournament():
    tournament_name = input("Nom du tournoi: ")
    place = input("Lieu: ")
    tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
    rounds = input("Nombre de tours du tournoi: ")
    if rounds == 0:
        rounds = 4
    timing = input("Contrôle du temps: ")
    description = input("Description: ")
    tournament = Tournament(tournament_name, place, tournament_date, rounds, [], timing, description)

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


def create_players():
    player_name = input("Prénom du joueur:")
    player_surname = input("Nom du joueur:")
    player_birthdate = input("Date de naissance:")
    player_gendre = input("sexe:")
    player_ranking = input("classement du joueur:")
    player = Player(player_name, player_surname, player_birthdate, player_gendre, player_ranking)

    return player


def enter_score():
    return 0


def pairing(tournament: Tournament):
    pairs = []

    players = tournament.players_listed()
    half = len(players) // 2
    leaderboard = sorted(players, key=lambda player: player.get('ranking', {}))

    for rank in range(half):
        pairs.append((leaderboard[rank], leaderboard[rank + half]))
    return pairs
