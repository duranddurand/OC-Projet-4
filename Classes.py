class Player:
    def __init__(self, surname, name, birthdate, gender, points, rank):
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.points = points
        self.rank = rank

    def display(self):
        print(self.surname, self.name, self.birthdate, self.gender, self.points, self.rank)

    def tupler(self):
        return self.surname, self.name, self.birthdate, self.gender, self.points, self.rank


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


player_list = []


for new_p in range(8):
    player_list.append(Player('Prénom' + str(new_p + 1), 'nom' + str(new_p), new_p, 'M', 0, 9 - new_p))
#   player_list[i].display()


tournament1 = Tournament('Tournois1', 'Paris', '11/09/2021', 4, [], player_list, 'blitz', '')


def pairing(joueurs: Tournament.players) -> list:
    tuples = []

    for j in joueurs:
        tuples.append(j.tupler())

    leaderboard = sorted(tuples, key=lambda player: player[5])
    half = len(leaderboard) // 2
    pairs = []

    for rank in range(half):
        pairs.append((leaderboard[rank], leaderboard[rank + half]))
    return pairs


for i in pairing(player_list):
    print(i[0][0], i[1][0])
