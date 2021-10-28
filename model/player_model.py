class Player:
    def __init__(self, name, surname, birthdate, gender, ranking, score):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.id = (name[0].upper() + surname.upper() + birthdate.replace("/", "").upper())

    def serialized(self):
        selialized_player = {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'ranking': self.ranking,
            'score': self.score
        }

        return selialized_player
