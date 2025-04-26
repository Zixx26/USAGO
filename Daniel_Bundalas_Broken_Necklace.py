"""""
ID: jonlenin
LANG: PYTHON3
PROG: beads
"""

fin = open('beads.in', 'r')
fout = open ('beads.out', 'w')

fin.readline()

Necklace = fin.readline().replace("\n","")
DoubleNecklace = Necklace+Necklace

left =[0 for i in DoubleNecklace],[0 for i in DoubleNecklace]
right =[0 for i in DoubleNecklace],[0 for i in DoubleNecklace]

m,m2 = 0,0

addition = [0,0]




def resolve(Current):
    if Current == "b":addition[0],addition[1] = 0,1
    elif Current == "r":addition[0],addition[1] = 1,0
    else :addition[0],addition[1] = 1,1



for i in range(len(DoubleNecklace)):
    resolve(DoubleNecklace[i])
    
    if i>0:
        
        left[0][i] = (left[0][i-1]+addition[0])*addition[0]
        left[1][i] = (left[1][i-1]+addition[1])*addition[1]
        
    else:
        left[0][i] = addition[0]
        left[1][i] = addition[1]
        

     

for i in range(len(DoubleNecklace)-1,0,-1):
    
    resolve(DoubleNecklace[i])

    #j = len(DoubleNecklace)-i-1

    
    #print(j)
    if i<len(DoubleNecklace)-1:
        right[0][i] = (right[0][i+1]+addition[0])*addition[0]
        right[1][i] = (right[1][i+1]+addition[1])*addition[1]
    else:
        right[0][i] = addition[0]
        right[1][i] = addition[1] 

    #print("right","r",right[0][j],"b",right[1][j],"j",j)
    #print("left","r",left[0][j],"b",left[1][j],"j",j)  

#print("left",left,"right",right)

for i in range(len(DoubleNecklace)-1):
    #print("i",i)
    #print("left r",left[0][i],"right r",right[0][i])
    #print("left b+1",left[1][i+1],"right b+1",right[1][i+1])
    m = max(m,max(left[0][i],right[0][i])+max(left[1][i+1],right[1][i+1]))
    m2 = max(m2,max(left[0][i+1],right[0][i+1])+max(left[1][i],right[1][i]))
    
    
    
   
#print("left",left)
#print(len(left[1]),len(left[0]))
#print("right",right)
#print("m",m,"m3",m3,"m4",m4)

m = max(m,m2)
m = min(m,len(Necklace))
#print(m)


#print(DoubleNecklace)




fout.write(str(m) +"\n")

#29
#wwwbbrwrbrbrrbrbrwrwwrbwrwrrb
#11

#77
#rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr
#74

#50
#bbrrrbrrrrrrrrbrbbbrbrrbrrrrbbbrbrbbbbbrbrrrbbrbbb
#9