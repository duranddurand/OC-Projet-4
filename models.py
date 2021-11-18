class Player:
    def __init__(self, name, surname, birthdate, gender, ranking, score):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.id = (name[0].upper() + surname.upper() + birthdate.replace("/", "").upper())

class Tournament:
    def __init__(self, name, place, date, rounds, players, timing, description):
        self.id = (name[0].upper() + date.replace("/", "").upper())
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players = players
        self.timing = timing
        self.description = description
        self.archive = 0

class Match:
    def __init__(self, tournID, RoundNo, player1, player2, result):
        self.tournid = tournID,
        self.roundno = RoundNo,
        self.player1 = player1,
        self.player2 = player2,
        self.result = result       
        
class Views:
    @staticmethod
    def print(value):

        view_dict = {

            # Menu principal

            1: "######## Bienvenue ######## \n\n1: Tournois \n2: Joueurs \n3: Quitter",
            2: "######## Tournois ######## \n\n1: Nouveau \n2: Reprende \n3: Historique \n4: Retour",
            3: "######## Joueurs ######## \n\n1: Ajouter \n2: Modifier \n3: Classement \n4: Retour",
            4: "######## Classement ######## \n\n1: Afficher \n2: Modifier \n3: Retour",
            5: "\n\n1: Confirmer \n2: Refaire",

            # Tournois

            6: "######## Joueurs du tournois ########\n\n1: Nouveau\n2: Ajouter\n3: Retour"
        }

        print(view_dict[value])
