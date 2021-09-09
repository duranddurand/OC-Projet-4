class Player:
    def __init__(self, surname, name, birthdate, gender, rank):
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank

#player1 = Player('Manis','Duran','26/01/1996','M','1')
#player2 = Player('Doe','John','21/04/2000','M','2')
#print(player2.birthdate)

class tournament:
    def __init__(self, name, place, date, rounds, turns, players, timing, description):
        self.name = name
        self.place = place
        self.rounds = rounds
        self.turns = turns
        self.players = players
        self.timing = timing
        self.description = description

