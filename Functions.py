from Model import Tournament, Player

# out: variable (class: Tournament)
def create_tournament():
    tournament_name = input("Nom du tournoi: ")
    place = input("Lieu: ")
    tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
    rounds = input("Nombre de tours du tournoi: ")
    if rounds == 0:
        rounds = 4
    players = []
    timing = input("Contrôle du temps: ")
    description = input("Description: ")
    while len(players) < 8:
        players.append(create_players())
    tournament = Tournament(tournament_name, place, tournament_date, rounds, players, timing, description)

    return tournament

#out : list
def create_players():
    player_name = input("Prénom du joueur:")
    player_surname = input("Nom du joueur:")
    player_birthdate = input("Date de naissance:")
    player_gendre = input("sexe:")
    player_ranking = input("classement du joueur:")
    player = Player(player_name, player_surname, player_birthdate, player_gendre, player_ranking)
    b = []
    b.append(player)
    return b

def enter_score():

    return 0


def pairing(t: Tournament):

    pairs = []

    players = t.players_listed()
    half = len(players) // 2
    leaderboard = sorted(players, key=lambda players: players.get('ranking', {}))


    for rank in range(half):
        pairs.append((leaderboard[rank], leaderboard[rank + half]))
    return pairs

T = create_tournament()
print(pairing(create_tournament()))