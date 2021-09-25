from tinydb import TinyDB

class Database:
    def __init__(self):
        self.db = 'db.json'

    def player_table(self):
        db = TinyDB(self.db)
        table = db.table('players')

        return table