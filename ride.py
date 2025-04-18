"""
ID: lel
LANG: PYTHON3
PROG: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')


Comet = map(str, fin.readline())
CometCode=1
Group = map(str, fin.readline())
GroupCode=1
for i in Comet:
    CometCode = CometCode * (ord(i)-64)
for i in Group:
    GroupCode = GroupCode * (ord(i)-64)

CometCode,GroupCode = CometCode%47,GroupCode%47
if CometCode == GroupCode: fout.write (str("GO") + '\n')
else:fout.write (str("STAY") + '\n')


fout.close()