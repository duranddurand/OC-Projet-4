class Player:
    def __init__(self, surname, name, birthdate, sexe, rank):
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.sexe = sexe
        self.rank = rank

player1 = Player('Manis','Duran','26/01/1996','M','1')
print(player1.name)