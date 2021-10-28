class Tournament:
    def __init__(self, name, place, date, rounds, players, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description

    def serialized(self):
        serialized_tournament = {
            'name': self.name,
            'place': self.place,
            'date': self.date,
            'rounds': self.rounds,
            'players': self.players,
            'time control': self.time_control,
            'description': self.description
        }

        return serialized_tournament


class Round:
    def __init__(self, name, round_matchs, start_time, end_time):
        self.name = name
        self.round_matchs = round_matchs
        self.start_time = start_time
        self.end_time = end_time


class Match:
    def __init__(self, player1, player2, issue):
        self.player1 = player1
        self.player2 = player2
        self.issue = issue
