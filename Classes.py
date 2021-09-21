class Player:
    def __init__(self, surname, name, birthdate, gender, ranking):
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = ranking

    def display(self):
        print(self.surname, self.name, self.birthdate, self.gender, self.rank)

    def tupler(self):
        return self.surname, self.name, self.rank


class Tournament:
    players = []

    def __init__(self, name, place, date, rounds, turns, players, timing, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.turns = turns
        self.players = players.copy()
        self.timing = timing
        self.description = description


class Round:
    def __init__(self, name, round_matchs, start_time, end_time):
        self.name = name
        self.round_matchs = round_matchs
        self.start_time = start_time
        self.end_time = end_time


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


player_list = []


for new_p in range(8):
    player_list.append(Player('Prénom' + str(new_p + 1), 'nom' + str(new_p + 1), new_p, 'M', new_p + 1))


tournament1 = Tournament('Tournois1', 'Paris', '11/09/2021', 4, [], player_list, 'blitz', '')


def pairing(joueurs: Tournament.players) -> list:

    tuples = []

    for j in joueurs:
        tuples.append(j.tupler())

    leaderboard = sorted(tuples, key=lambda player: player[2])
    half = len(leaderboard) // 2
    pairs = []

    for rank in range(half):
        pairs.append((leaderboard[rank], leaderboard[rank + half]))
    return pairs


for pair in pairing(tournament1.players):
    print(pair[0][0], pair[1][0])
