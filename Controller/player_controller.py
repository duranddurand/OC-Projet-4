from Model.player_model import Model


class PlayerControl:

    @staticmethod
    def create_player():
        name = input("Prénom du joueur:")
        surname = input("Nom du joueur:")
        birthdate = input("Date de naissance:")
        gender = input("sexe:")
        ranking = input("classement du joueur:")

        player = Model(name, surname, birthdate, gender, ranking)

        return player

    @staticmethod
    def edit_player():
        return 0

