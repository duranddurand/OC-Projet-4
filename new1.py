from tinydb import TinyDB, Query

db = TinyDB('db.json')
table = db.table('fruits')

table.insert({'type': 'peach', 'count': 3})
table.insert({'type': 'apple', 'count': 3})


Fruit = Query()
# print(table.search(Fruit.type == 'apple'))
print(table.all())

