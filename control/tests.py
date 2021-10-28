from model.player_model import Player
from tinydb import TinyDB

player = Player('john', 'doe', '12/10/2001', 'M', 10, 0)
player2 = Player('james', 'adsf', '13/10/3001', 'F', 9, 0)


def serialize_player(play):
    player_in_dict = {
        'id': play.id,
        'name': play.name,
        'surname': play.surname,
        'birthdate': play.birthdate,
        'gender': play.gender,
        'ranking': play.ranking,
        'score': play.score
    }

    return player_in_dict



players_table.truncate() # clear the table first
players_table.insert(serialize_player(player))
players_table.insert(serialize_player(player2))

for i in players_table:
    print('\n')
    print(i)
    print('\n')

# search(where('name') == 'john')