class Player:
    def __init__(self, name, surname, birthdate, gender, ranking):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.id = (name[0].upper() + surname.upper() + birthdate.replace("/", ""))

    def display(self):
        print(self.surname, self.name, self.birthdate, self.gender, self.ranking)

    def tupler(self):
        return self.surname, self.name, self.ranking


class Tournament:

    def __init__(self, name, place, date, rounds, matchs, players, timing, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.matchs = matchs
        self.players = players
        self.timing = timing
        self.description = description

    def players_listed(self):
        players_list = []
        for player in self.players:
            player_dict = {
                'id': player.id,
                'name': player.name,
                'surname': player.surname,
                'birthdate': player.birthdate,
                'gender': player.gender,
                'ranking': player.ranking
            }
            players_list.append(player_dict)

        return players_list

    def matchs_listed(self):
        matchs_list = []
        for match in self.matchs:
            match_dict = {
                'players': [match[0][0], match[1][0]],
                'score': [match[0][1], match[1][1]]
            }
            matchs_list.append(match_dict)

        return matchs_list


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
