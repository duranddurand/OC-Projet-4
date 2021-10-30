
d={"joueur2":12,"joueur1":10,"joueur3":18,"joueur4":20,"joueur5":45,"joueur6":4,"joueur7":3,"joueur8":23}
l=list([i,d[i]] for i in d.keys())
l=sorted(l,key=lambda l:l[1])
l=list((l[i][0],i/len(l)) for i in range(len(l)))
hist=[]
l0=list([min(l[i][0],l[i+len(l)//2][0]),max(l[i][0],l[i+len(l)//2][0])] for i in range(len(l)//2))
l0
hist.extend(l0)
hist
l1=[]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if [min(l[i][0],l[j][0]),max(l[i][0],l[j][0])] not in hist:
            l1.append([min(l[i][0],l[j][0]),max(l[i][0],l[j][0]),d[min(l[i][0],l[j][0])]+d[max(l[i][0],l[j][0])]])

l1=list(map(lambda x:[x[0],x[1]],sorted(l1,key=lambda l:l[2],reverse=True)))
def test_exlu(l1,l2):
    for i in l1:
        if i in l2:
            return False
    return True
list_combi=[]
def best_combi(l1):
    if len(list_combi)==4:
        return list_combi
    for i in