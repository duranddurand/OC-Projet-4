from tinydb import *


class Player:
    def __init__(self, name, surname, birthdate, gender, ranking, score):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.id = (name[0].upper() + surname.upper() + birthdate.replace("/", "").upper())

    def serialize_player(self):
        player_in_dict = {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'ranking': self.ranking,
            'participation': 0
        }

        return player_in_dict


db = TinyDB('chess.json')
player1 = Player("duran", "anis", "25/02/1998", "M", 1, 0)
player2 = Player("duion", "afnis", "24/02/1998", "M", 1, 0)


def insert_player(player, database):
    table = database.table('players')
    table.insert(player.serialize_player())


db.truncate()
insert_player(player1, db)
insert_player(player2, db)

players_table = db.table('players')
q = Query()
result = players_table.search(q.participation == 1)


print(result)

def update_player(player, participation):
    players_table.update(q.participation == 0, 1)