class Player:
    def __init__(self, surname, name, birthdate, gender, ranking):
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking

    def display(self):
        print(self.surname, self.name, self.birthdate, self.gender, self.ranking)

    def tupler(self):
        return self.surname, self.name, self.ranking


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
