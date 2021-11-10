import os

from models import *
from tinydb import TinyDB, table, Query


def clear():
    return 0

def exit_program():
    return 0

# Display a list of choices. each one opens a different menu or exit app
# 
def main_menu():
    Views.print(1)
    choice = input("\n>> ")

    if choice == "1":
        clear()
        tournament_menu()
    elif choice == "2":
        clear()
        player_menu()
    elif choice == "3":
        exit_program()


def tournament_menu():
    Views.print(2)
    choice = input("\n>> ")
    if choice == "1":
        clear()
        create_tournament()
    elif choice == "2":
        clear()
        list_open_tournaments()
    elif choice == "3":
        clear()
        list_tournaments_archive()
    elif choice == "4":
        clear()
        main_menu()
    else:
        pass


def player_menu():
    Views.print(3)
    choice = input("\n>> ")

    if choice == "1":
        create_player()
    elif choice == "2":
        return 0
    elif choice == "3":
        leaderboard_menu()
    elif choice == "4":
        main_menu()
    else:
        pass


def leaderboard_menu():
    Views.print(4)
    choice = input("\n>> ")

    if choice == "1":
        return 0()
    elif choice == "2":
        return 0
    elif choice == "3":
        player_menu()
    else:
        pass


################################################
################## Database ####################
################################################

db = TinyDB('chess.json')
player1 = Player("duran","anis","25/02/1998","M",1,0)
player2 = Player("duion","afnis","24/02/1998","M",1,0)

def insert_player(player) :
    table = db.table('players')
    table.insert(serialize_player(player))


def insert_tournament(tournament):
    table = db.table('tournaments')
    table.insert(serialize_tournament(tournament))


def insert_round(round):
    table = db.table('rounds')
    table.insert(round)

def list_players():
    table = db.table('players')
    tournaments = table.all()
    
    return tournaments


def list_tournaments():
    table = db.table('tournaments')
    tournaments = table.all()
    
    return tournaments

def list_open_tournaments():
    table = db.table('tournaments')
    tourn = Query()
    players = table.search(tourn.archive == '0')

    return table

def list_tournaments_archive():
    table = db.table('tournaments')
    tourn = Query()
    players = table.search(tourn.archive == '1')

    return table

def list_tournament_players(tournament):
    table = db.table('tournaments')
    tourn = Query()
    players = table.search(tourn.id == tournament.id)['players']
    
    return players

def list_tournament_rounds(tournament):
    table = db.table('rounds')
    tourn = Query()
    rounds = table.search(tourn.id == tournament.id)
    
    return rounds

def list_round_matches(round):
    table = db.table('matches')
    matches = table.all()
    
    return matches


################################################
#################### Player ####################
################################################



def create_player():
    name = input("Prénom du joueur:")
    surname = input("Nom du joueur:")
    birthdate = input("Date de naissance:")
    gender = input("sexe:")
    ranking = input("classement du joueur:")

    player = Player(name, surname, birthdate, gender, ranking, 0)

    Views.print(6)
    verify = input("\n>>> ")
    if verify == "1":
        insert_player(serialize_player(player))
    elif verify == "2":
        clear()
        create_player()
    else:
        TypeError

def serialize_player(player):
    player_in_dict = {
        'id': player.id,
        'nom': player.name,
        'surname': player.surname,
        'birthdate': player.birthdate,
        'gender': player.gender,
        'ranking': player.ranking
    }

    return player_in_dict

def select_players():
    for i in list_players:
        print(str(i + 1) + ': ' + list_players[i])
    
    selection = []
    selection.append(input('>>> : '))
    
    return selection

################################################
################## Tournament ##################
################################################

def create_tournament():
    name = input("Nom du tournoi: ")
    place = input("Lieu: ")
    date = input("Date du tournoi (Format: jj/mm/aaaa): ")
    rounds = input("Nombre de tours du tournoi: ")
    if rounds == 0:
        rounds = 4
    timing = input("Contrôle du temps: ")
    description = input("Description: ")
    players = tournament_players()
    tournament = Tournament(name, place, date, rounds, players, timing, description)

    Views.print(6)
    verify = input("\n>>> ")
    if verify == "1":
        insert_tournament(serialize_tournament(tournament))
    elif verify == "2":
        clear()
        create_tournament()
    else:
        pass

    return tournament

def tournament_players():
    players = []
    print("Decompte: " + str(len(players)))
    Views.print(6)
    while len(players) < 8:
        val = input("\n: ")
        if val == "1":
            players.append(serialize_player(create_player()))
        elif val == "2":
            players.append(select_players())
        elif val == "3":
            main_menu()
        else:
            pass
    
    return players

def serialize_tournament(tournament):
    tournament_in_dict = {
        'id': tournament.id,
        'name': tournament.name,
        'place': tournament.place,
        'date': tournament.date,
        'rounds': tournament.rounds,
        'players': tournament.players,
        'timing': tournament.timing,
        'description': tournament.description,
        'archive': tournament.archve

    }

def pairing_players(tournament_players):

    tournament_players=["a","b","c","d","e","f","g","h"]
    d1=[["a","b"],["b","c"],["e","h"],["a","g"]]
    d2=[]

    for i in range(8):
        for j in range(i+1,8):
            if [tournament_players[i],tournament_players[j]] not in d1:
                d2.append([tournament_players[i],tournament_players[j],i+j])

    d2.sort(key=lambda x:x[2],reverse=True)

    list_1=[]
    list_1.append(d2[0])
    list_1.append(d2[7])


def check_player_exist(list_matchs,match):
    for i in list_matchs:
        if match[0]==i[0] or match[0]==i[1] or match[1]==i[0] or match[1]==i[1]:
            return False
    return True


def list_comb(list_comb):
    for i in range(len(list_comb)):
        list2=[]
        list2.append(list_comb[i])
        for j in range(i+1,len(list_comb)):
            if check_player_exist(list2,list_comb[j]):
                list2.append(list_comb[j])
                for k in range(j+1,len(list_comb)):
                        if check_player_exist(list2,list_comb[k]):
                            list2.append(list_comb[k])
                            for l in range(k+1,len(list_comb)):
                                    if check_player_exist(list2,list_comb[l]):
                                        list2.append(list_comb[l])
                                        return list2
    return -1

    list_comb(d2)
