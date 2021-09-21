from Functions import pairing
from Model import Tournament, Player


player_list = []


for new_p in range(8):
    player_list.append(Player('Prénom' + str(new_p + 1), 'nom' + str(new_p + 1), new_p, 'M', new_p + 1))


tournament1 = Tournament('Tournois1', 'Paris', '11/09/2021', 4, [], player_list, 'blitz', '')


for pair in pairing(tournament1.players):
    print(pair[0][0], pair[1][0])
