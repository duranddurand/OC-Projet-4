players = []
for i in range(8):
    players.append(["id" + str(i), 21*i, 9 - i])

tourn = ["TOURN01", "blabla", "paris", "29/10/2021", 4, players, "Blitz", "super sympa!"]

match = []
for i in range(8):
    match.append(["Match" + str(i), players[i][0], players[(i+2)%8][0]])

# list_player = get_list_players(tourn1)
# list_match = get_list_match(tourn1)


print(players)
print(match)



d=["a","b","c","d","e","f","g","h"]
d1=[["a","b"],["b","c"],["e","h"],["a","g"]]
d2=[]
for i in range(8):
    for j in range(i+1,8):
        if [d[i],d[j]] not in d1:
            d2.append([d[i],d[j],i+j])

d2.sort(key=lambda x:x[2],reverse=True)
list_1=[]
list_1.append(d2[0])
list_1.append(d2[7])
def check_player_exist(list_matchs,match):
    for i in list_matchs:
        if match[0]==i[0] or match[0]==i[1] or match[1]==i[0] or match[1]==i[1]:
            return False
    return True
def list_comb(list_comb):
    for i in range(len(list_comb)):
        list2=[]
        print(i)
        list2.append(list_comb[i])
        for j in range(i+1,len(list_comb)):
            if check_player_exist(list2,list_comb[j]):
                list2.append(list_comb[j])
                for k in range(j+1,len(list_comb)):
                        if check_player_exist(list2,list_comb[k]):
                            list2.append(list_comb[k])
                            for l in range(k+1,len(list_comb)):