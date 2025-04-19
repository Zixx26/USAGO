"""
ID: lel
LANG: PYTHON3
PROG: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')


Nps = int(fin.readline())
nps_List = []
for i in range(Nps):
    nps_List.append(fin.readline())
    nps_List.append(0)

for i in range(Nps):
    giver=fin.readline()
    amount = fin.readline().split()
    if amount[1] != "0":
        for i in range(int(amount[1])):
            nps_List[nps_List.index(fin.readline())+1]+=(int(amount[0])//int(amount[1]))

    if amount[0] != "0":
        nps_List[nps_List.index(giver)+1]-=(int(amount[0])-(int(amount[0])%int(amount[1])))
    

for i in range(1,len(nps_List),2):
    x,y = nps_List[i-1].replace('\n'," "),str(nps_List[i]).strip('\n')
    
    fout.write ( x+y+ '\n' )
    


fout.close()
    
        

