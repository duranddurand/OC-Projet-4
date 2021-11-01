from tinydb import TinyDB


class Database:

    @staticmethod
    def insert_player(inst):
        db = TinyDB("./database/tournament_database.json")
        db.table("players").insert(inst.serialized)

    @staticmethod
    def insert_tournament(inst):
        db = TinyDB("./database/tournament_database.json")
        db.table("tournament").insert(inst.serialized)

    @staticmethod
    def insert_turn(inst):
        db = TinyDB("./database/tournament_database.json")
        db.table("turn").insert(inst.serialized)

    @staticmethod
    def insert_match(inst):
        db = TinyDB("./database/tournament_database.json")
        db.table("match").insert(inst.serialized)

    def get_ongoing_tournament(self):
        db = TinyDB(self.db)
        table = db.table('running_tournament')

        return table

    def save_rounds(self, match):
        table = self.round_table()
        for match in match:
            match_dict = {
                "players": [match[0][0], match[1][0]],
                "score": [float(match[0][1]), float(match[1][1])]
            }
            table.insert(match_dict)

    def save_turn(self):
        db = TinyDB("./database/tournament_database.json")
        db.table("turn")

    @staticmethod
    def get_played_turns(tournament):
        db = TinyDB("./database/tournament_database.json")
        db

        return table

