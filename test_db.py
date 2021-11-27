from controls import *
from models import *

#vider les tables de la base de données
"""Database('db2').truncate_table("player")
Database('db2').truncate_table("match")
Database('db2').truncate_table("tournament")"""

#créer une liste de joueurs
for i in range(8):
    Database('db2').insert_db(Player('name' + str(i),'surname'  + str(i), '20/11/200' + str(i), 'M', i + 1, i*3))
                           
#créer des tournois
Database('db2').insert_db(Tournament(4,list(map(lambda x:x["id"],Database('db2').get_all("player")))))
Database('db2').insert_db(Tournament(3,list(map(lambda x:x["id"],Database('db2').get_all("player")))))
t=Database('db2').get_list_id("tournament")
#créer des matchs
for i in range(4):
    match_=Match(str(i)+'raoul'+str(i),'raoul'+str(i+4),2,t[0])
    match_.score=i%3
    Database('db2').insert_db(match_)
for i in range(3):
    match_=Match(str(i)+'raoul'+str(i),'raoul'+str(i+4),3,t[0])
    match_.score=i%3
    Database('db2').insert_db(match_)
for i in range(3):
    match_=Match(str(i)+'raoul'+str(i),'raoul'+str(i+4),3,t[1])
    match_.score=i%3
    Database('db2').insert_db(match_)

g=Database('db2').get_list_turns_all()

