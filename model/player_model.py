class Player:
    def __init__(self, name, surname, birthdate, gender, ranking, score):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.id = (name[0].upper() + surname.upper() + birthdate.replace("/", "").upper())
