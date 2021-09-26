from tinydb import TinyDB


class Database:
    def __init__(self):
        self.db = 'db.json'

    def player_table(self):
        db = TinyDB(self.db)
        table = db.table('players')

        return table

    def round_table(self):
        db = TinyDB(self.db)
        table = db.table('rounds')

        return table

    def tournament_table(self):
        db = TinyDB(self.db)
        table = db.table('tournament')

        return table

    def running_tournament_table(self):
        db = TinyDB(self.db)
        table = db.table('running_tournament')

        return table

    def save_player(self, player):
        player_row = {
            'first_name': player.name,
            'last_name': player.surname,
            'birth_date': player.birthdate,
            'gender': player.gender,
            'ranking': player.ranking,
            'id': player.id
        }

        players_table = self.player_table()
        players_table.insert(player_row)

    def save_rounds(self, match):
        table = self.round_table()
        for match in match:
            match_dict = {
                "players": [match[0][0], match[1][0]],
                "score": [float(match[0][1]), float(match[1][1])]
            }
            table.insert(match_dict)
