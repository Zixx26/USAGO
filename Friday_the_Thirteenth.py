"""
ID: lel
LANG: PYTHON3
PROG: friday
"""
fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

years = int(fin.readline())
year=1900
monthlist=[
"Ja",6,
"Fe",2,
"Ma",2,

"Ap",5,
"Ma",7,
"Ju",3,

"Jul",5,
"Au",1,
"Se",4,

"Oc",6,
"No",2,
"De",4
]
Daylist=[0,0,0,0,0,0,0]

def calendershift():
    for i in range(1,len(monthlist),2):
        monthlist[i]+=1
        if monthlist[i]==8:
            monthlist[i]=1

for i in range(years):
    Currentyear=year+i
    for i in range(1,len(monthlist),2):
        Daylist[monthlist[i]-1]+=1
        if monthlist[i-1]=="Fe":
            if Currentyear%4 == 0:
                if Currentyear/100 == Currentyear//100:
                    if Currentyear%400 == 0:
                        calendershift()
                else:
                    calendershift()
    calendershift()


answer1 = " ".join([str(i) for i in Daylist[5:]])
answer2 = " ".join([str(i) for i in Daylist[:5]])

fout.write(answer1+" "+answer2 + '\n')


