from tinydb import *

from controls import Database

class player():
    def __init__(self,name,rank):
        self.id=name[:2]+str(rank)
        self.name=str(name)
        self.rank=rank
        self.points=0
    
    def serialize(self):
        return {'id':self.id,'name':self.name,'rank':self.rank,'points':self.points}

class match():
    score=-1
    def __init__(self,player1,player2,turn_id,tournament_id):
        self.id=player1[:2]+player2[:2]+str(turn_id)+str(tournament_id)
        self.player1=str(player1)
        self.player2=str(player2)
        self.turn_id=str(turn_id)
        self.tournament_id=str(tournament_id)
    def add_score(self,score):
        self.score=score
        
    def serialize(self):
        return {'id':self.id,'player1':self.player1,'player2':self.player2,'score':self.score,'turn_id':self.turn_id,'tournament_id':self.tournament_id}

class tournament():
    status=1
    def __init__(self,num_turns,players):
        self.id=players[0][0]+players[1][0]+str(num_turns)
        self.num_turns=num_turns
        self.players=players
    def close_tournament(self,score):
        self.status=0
    
    def serialize(self):
        return {'id':self.id,'status':self.status,'num turns':self.num_turns,'players':';'.join(self.players)}

class db_op():
    def __init__ (self,db_name):
        self.db_=TinyDB(str(db_name)+'.json')
        
    def truncate_table(self,table_):
        self.db_.table(table_).truncate()

    def query_1(self, table_,var_,val_):
        q=Query()
        return self.db_.table(table_).search(q[var_]==val_)
    
    def query_2(self, table_,var_1,val_1,var_2,val_2):
        q=Query()
        return self.db_.table(table_).search((q[var_1]==val_1)&(q[var_2]==val_2))
    
    def get_all(self,table_):
        return self.db_.table(table_).all()
    
    def insert_db(self,object_):
        table_=str(type(object_))[17:-2]
        if not len(self.query_1(table_,"id",object_.id)):
            self.db_.table(table_).insert(object_.serialize())
    
    def get_list_id(self,object_):
        return list(map(lambda x:x["id"],db_op('db2').get_all(object_)))
    
    def get_list_turns_all(self):
         return list(list(i.split(":")) for i in set(map(lambda x:str(x["turn_id"])+":"+str(x["tournament_id"]),self.get_all("match"))))
    
    def get_list_players_by_tournament(self,tournament_id):
        return list(self.query_1("tournament","id",tournament_id)[0]["players"].split(";"))
    
    def list_match_pairs(self,tournament_id):
        return list(map(lambda x:[x["player1"],x["player2"]],self.query_1("match","tournament_id",tournament_id)))
        #return self.query_2("match","turn_id",turn,"tournament_id",tournament)

    def update_(self, object_, var_, val_, varfiltre_, valfiltre_):
        return self.db_.table(object_).update({var_: val_}, where(varfiltre_) == valfiltre_)

#vider les tables de la base de données
db_op('db2').truncate_table("player")
db_op('db2').truncate_table("match")
db_op('db2').truncate_table("tournament")

#créer une liste de joueurs
for i in range(8):
    db_op('db2').insert_db(player(str(i)+"raoult"+str(i),100+i))
                           
#créer des tournois
db_op('db2').insert_db(tournament(4,list(map(lambda x:x["id"],db_op('db2').get_all("player")))))
db_op('db2').insert_db(tournament(3,list(map(lambda x:x["id"],db_op('db2').get_all("player")))))
t=db_op('db2').get_list_id("tournament")
#créer des matchs
for i in range(4):
    match_=match(str(i)+'raoul'+str(i),'raoul'+str(i+4),2,t[0])
    match_.score=i%3
    db_op('db2').insert_db(match_)
for i in range(3):
    match_=match(str(i)+'raoul'+str(i),'raoul'+str(i+4),3,t[0])
    match_.score=i%3
    db_op('db2').insert_db(match_)
for i in range(3):
    match_=match(str(i)+'raoul'+str(i),'raoul'+str(i+4),3,t[1])
    match_.score=i%3
    db_op('db2').insert_db(match_)
g=db_op('db2').get_list_turns_all()

db_op('db2').update_('player', 'point', 2, 'id', '0r100')
print("list de tous les joueurs: ",*db_op('db2').get_list_id("player"))
print("list de tous les matchs: ",*db_op('db2').get_list_id("match"))
print("list de tous les tournois: ",*db_op('db2').get_list_id("tournament"))
print("list de tous les tours avec leur tournois: ",db_op('db2').get_list_turns_all())
print("list des matchs précédents d'un tournois: ",*db_op('db2').list_match_pairs(g[0][1]))
print("list des joueurs d'un tournois: ",db_op('db2').get_list_players_by_tournament(g[0][1]))
