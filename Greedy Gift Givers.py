"""
ID: lel
LANG: PYTHON3
PROG: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

from collections import Counter
Nps = map(str, fin.readline())
nps_List = []
for i in range(Nps):
    nps_List.append(map(str, fin.readline()))
    nps_List.append(0)

for i in range(Nps):
    giver=input()
    amount = map(int, fin.readline())
    

    if amount[1] != "0":
        for i in range(int(amount[1])):
            nps_List[nps_List.index(map(str, fin.readline()))+1]+=(amount[0]//amount[1])

    if amount[0] != "0":
        nps_List[nps_List.index(giver)+1]-=(int(amount[0])-(int(amount[0])%int(amount[1])))
    

for i in range(1,len(nps_List),2):
    print(nps_List[i-1],nps_List[i])
    
    
    
        

