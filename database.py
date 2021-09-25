from tinydb import TinyDB


class Database:
    def __init__(self):
        self.db = 'db.json'

    def player_table(self):
        db = TinyDB(self.db)
        table = db.table('players')

        return table

    def round_table(self):
        db = TinyDB(self.db)
        table = db.table('rounds')

        return table

    def tournament_table(self):
        db = TinyDB(self.db)
        table = db.table('tournament')

        return table

    def running_tournament_table(self):
        db = TinyDB(self.db)
        table = db.table('running_tournament')

        return table