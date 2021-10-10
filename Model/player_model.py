class Model:
    def __init__(self, name, surname, birthdate, gender, ranking):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.id = (name[0].upper() + surname.upper() + birthdate.replace("/", "").upper())



