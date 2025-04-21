"""
ID: lel
LANG: PYTHON3
PROG: beads
"""
fin = open('beads.in', 'r')
fout = open ('beads.out', 'w')
fin.readline()
halfNecklace = fin.readline().replace("\n","")
if halfNecklace[0:2] == halfNecklace[-2:] or len(halfNecklace)%4 == 0:fullNecklace = halfNecklace
else:fullNecklace = halfNecklace + halfNecklace



fullNecklace = fullNecklace.replace("\n","")

things = []

white = 0

stage = " "

current = 0

Cwhites = [0,0,0]
CwhitesCounter = [0,0,0]

CCvalue = [0,0]
BiggestValue = 0
shifts=2

def whiteshift():
    for j in range(len(CwhitesCounter)):
        
        if CwhitesCounter[j] == 0:
            Cwhites[j] = 0
        else:CwhitesCounter[j]-=1

def whitechange():
    if Cwhites[0]==0: 
        Cwhites[0]=white
        CwhitesCounter[0]=shifts
    elif Cwhites[1]==0:
        Cwhites[1]=white
        CwhitesCounter[1]=shifts
    else:
        Cwhites[2]=white
        CwhitesCounter[2]=shifts
        

       

for i in fullNecklace:
    
    if i == "w":
        white+=1
    else:
        if stage == " ": 
            stage=i
            current+=1+white
            white=0
        elif stage == i: 
            current+=1+white
            white=0
        else:
            CCvalue[0],CCvalue[1] = CCvalue[1],current
           
            #things.append(current)
            stage=i
            current=1 

            whiteshift()
                   
            if white != 0:
                #things.append(str(white))
                whitechange()
                white=0
           
            if Cwhites[0]+Cwhites[1]+Cwhites[2]+CCvalue[0]+CCvalue[1]> BiggestValue:
                BiggestValue = Cwhites[0]+Cwhites[1]+Cwhites[2]+CCvalue[0]+CCvalue[1]
                


whiteshift()

whitechange()

CCvalue[0],CCvalue[1] = CCvalue[1],current

if Cwhites[0]+Cwhites[1]+Cwhites[2]+CCvalue[0]+CCvalue[1]> BiggestValue: 
    BiggestValue = Cwhites[0]+Cwhites[1]+Cwhites[2]+CCvalue[0]+CCvalue[1]
    

fout.write(str(BiggestValue) + "\n")
fin.close()
fout.close()   
    




