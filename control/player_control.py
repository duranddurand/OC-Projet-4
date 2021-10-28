from model.player_model import Player as PlayerModel


class PlayerControl:

    @staticmethod
    def generate():
        name = input("Prénom du joueur:")
        surname = input("Nom du joueur:")
        birthdate = input("Date de naissance:")
        gender = input("sexe:")
        ranking = input("classement du joueur:")

        player = PlayerModel(name, surname, birthdate, gender, ranking)

        return player

    @staticmethod
    def edit():
        return 0

    @staticmethod
    def serialized(player):
        dict = {
            'id': player.id,
            'nom': player.name,
            'surname': player.surname,
            'birthdate': player.birthdate,
            'gender': player.gender,
            'ranking': player.ranking
        }

        return dict



