"""
ID: lel
LANG: PYTHON3
PROG: milk2
"""

fin = open("milk2.in","r")
fout = open("milk2.out","w")



Info = [fin.readline().split() for _ in range(int(fin.readline()))]

for i in range(len(Info)):
    Info[i][0] = int(Info[i][0])
    Info[i][1] = int(Info[i][1])

Info.sort()

print(Info)

longestmilk = 0
longeststagger = 0
s = 0
e = 0
j = 0

for i in range(len(Info)-1):
    j = i+1

    

    if Info[e][1] >= Info[j][0]:
        if Info[j][1]>Info[e][1]:e=j
    else:
        if longestmilk <  Info[e][1] - Info[s][0]: longestmilk= Info[e][1] - Info[s][0]
        if longeststagger < Info[j][0]- Info[e][1]: longeststagger = Info[j][0]- Info[e][1]
        print(s,e)
        e = j
        s = j
        
    
   
        

if longestmilk <  Info[e][1] - Info[s][0]: longestmilk= Info[e][1] - Info[s][0]



fout.write(str(longestmilk)+" "+str(longeststagger) + "\n")  
