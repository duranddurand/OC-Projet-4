class Player:
    def __init__(self, name, surname, birthdate, gender, ranking):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.id = (name[0].upper() + surname.upper() + birthdate.replace("/", "").upper())

    def create_new(self):
        self.name = input("Prénom du joueur:")
        self.surname = input("Nom du joueur:")
        self.birthdate = input("Date de naissance:")
        self.gender = input("sexe:")
        self.ranking = input("classement du joueur:")

        new_player = Player(self.name, self.surname, self.birthdate, self.gender, self.ranking)

class Round:
    def __init__(self, name, round_matchs, start_time, end_time):
        self.name = name
        self.round_matchs = round_matchs
        self.start_time = start_time
        self.end_time = end_time


class Tournament:
    def __init__(self, name, place, date, rounds, players, timing, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players = players
        self.timing = timing
        self.description = description

    def create_new(self):
        self.name = input("Nom du tournoi: ")
        self.place = input("Lieu: ")
        self.date = input("Date du tournoi (Format: jj/mm/aaaa): ")
        self.rounds = input("Nombre de tours du tournoi: ")
        if self.rounds == 0:
            self.rounds = 4
        self.timing = input("Contrôle du temps: ")
        self.description = input("Description: ")

        print("\n\n1: Confirmer \n2: Refaire")
        verify = input("\n>>> ")
        if verify == "1":
            self.add_players()
        elif verify == "2":
            return 0
        else:
            pass

        return self.name, self.place, self.date, self.rounds, \
            self.players, self.timing, self.description

    def add_players(self):
        print("######## Les joueurs ########")
        print("\n \n1: Nouveau \n2: Ajouter \nR: Retour")
        while len(self.players) < 8:
            verify = input("\n>>> ")
            if verify == "1":
                self.players.append(Player.create_new())
            elif verify == "2":
                self.players.append(Player.add_players())
            elif verify == "3":
                return 0
            else:
                pass


class Match:
    def __init__(self, player1, player2, issue):
        self.player1 = player1
        self.player2 = player2
        self.issue = issue

