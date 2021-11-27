import os

from models import Player, Tournament, Views
from tinydb import TinyDB, table, Query


def clear():
    return 0

def exit_program():
    return 0

# Display a list of choices
# each one opens a different menu or exit app
def main_menu():
    print("######## Bienvenue ######## \n\n1: Creer joueur \n2: Creer Tournois \n3: Quitter")
    choice = input("\n>> ")

    if choice == "1":
        clear()
        tournament_menu()
    elif choice == "2":
        clear()
        player_menu()
    elif choice == "3":
        exit_program()

"""# Display a list of choices.
# Create tournament
# list open tournaments
# list tournament archives
# return to main menu
def tournament_menu():
    Views.print(2)
    choice = input("\n>> ")
    if choice == "1":
        clear()
        create_tournament()
    elif choice == "2":
        clear()
        Database.list_open_tournaments()
    elif choice == "3":
        clear()
        Database.list_tournaments_archive()
    elif choice == "4":
        clear()
        main_menu()
    else:
        pass

# Display a list of choices.
# Create player
# edit player
# access leaderboard menu
# return to main menu 
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

# Display a list of choices.
# Display leaderboard
# edit leaderboard
# return to main menu
def leaderboard_menu():
    Views.print(4)
    choice = input("\n>> ")

    if choice == "1":
        return 0
    elif choice == "2":
        return 0
    elif choice == "3":
        player_menu()
    else:
        pass
"""

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
        Database.insert_player(player)
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
    for i in Database.list_all_players:
        print(str(i + 1) + ': ' + Database.list_all_players[i])
    
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
        Database.insert_tournament(serialize_tournament(tournament))
    elif verify == "2":
        clear()
        create_tournament()
    else:
        pass

    return tournament

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
        'archive': tournament.archive
    }

    return tournament_in_dict

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


################################################
################## Database ####################
################################################

player1 = Player("duran","anis","25/02/1998","M",1,0)
player2 = Player("duion","afnis","24/02/1998","M",1,0)

class Database:

    def __init__ (self,db_name):
        self.db=TinyDB(str(db_name) + '.json')
        
    def truncate_table(self,table_):
        self.db.table(table_).truncate()

    def query_1(self, table_,var_,val_):
        q=Query()
        return self.db_.table(table_).search(q[var_]==val_)
    
    def query_2(self, table_,var_1,val_1,var_2,val_2):
        q=Query()
        return self.db_.table(table_).search((q[var_1]==val_1)&(q[var_2]==val_2))
    
    def insert_db(self,object):
        table = str(type(object))[17:-2]
        if not len(self.query_1(table,"id",object.id)):
            self.db_.table(table).insert(object.serialized())

    def get_all(self,table_):
        return self.db.table(table_).all()

    # list all open in the database table 'tournament'
    def list_open_tournaments(self):
        table = self.db.table('tournaments')
        tourn = Query()
        players = table.search(tourn.archive == '0')

        return table

    # list all archived tournament in the database table 'tournament'
    def list_tournaments_archive(self):
        table = self.db.table('tournaments')
        tourn = Query()
        players = table.search(tourn.archive == '1')

        return table

    # lists players for a designated tournament in the database
    def list_tournament_players(self, tournament):
        table = self.db.table('tournaments')
        tourn = Query()
        players = table.search(tourn.id == tournament.id)[5]
        
        return players

    # lists rounds for a designated tournament in the database
    def list_tournament_matches(self, tournament):
        table = self.db.table('matches')
        tourn = Query()
        matches = table.search(tourn.id == tournament.id)['matches']
        
        return matches

    # lists matches in a designated round in the database
    def list_tournament_rounds(self, tournament):
        table = self.db.table('matches')
        matches = table.all()
        
        return matches


################################################
################### Pairing  ###################
################################################

"""playerslist1 = []
for i in range(8):
    playerslist1.append(Player('name' + str(i),'surname'  + str(i), '20/11/200' + str(i), 'M', i + 1, i*3))
    Database.insert_player(Player('name' + str(i),'surname'  + str(i), '20/11/200' + str(i), 'M', i + 1, i*3))

tournament1 = Tournament('superchampion', 'Lisbon', '20/11/2021', 4, playerslist1, 'blitz', 'super')

print(tournament1['id'])

print(Database.list_tournament_players(tournament1))"""

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
