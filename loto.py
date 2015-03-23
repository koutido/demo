import random

tab1=[4,10,14,37,46]
taba=[4,7]
tab5=[]
tab2=[]
tab_double5=[]
tab_double2=[]
#tirage des 5 chiffres
def gen_tab5(tab):
    tab_res=[]
    for i in tab:
        n=1
        numbers=range(1,51)
        c=0
        while numbers:
        # melanger la liste numbers
            for t in range(1,10):
                random.shuffle(numbers)
                
            #random.shuffle(numbers)
            c=numbers.pop()
            if c==i:
            #print("numero trouve"),
            #print n
                tab_res.append(n)
                #chiffre trouve, vider le tableau
                numbers=[]
            n=n+1
    return tab_res

#tirage des etoiles
def gen_tab2(tab):
    tab_res=[]
    for i in tab:
        n=1
        numbers=range(1,12)
        c=0
        while numbers:
        # melanger la liste numbers
            random.shuffle(numbers)
            c=numbers.pop()
            if c==i:
            #print("numero trouve"),
            #print n
                tab_res.append(n)
                #chiffre trouve, vider le tableau
                numbers=[]
            n=n+1
    return tab_res

#chercher le doublon
def find_double(tab):
    while tab:
        d=tab.pop()
        for i in tab:
            if i==d:
                return i
    return 0

#tirage des doublons
while len(tab_double5)<5:
    tab5=gen_tab5(tab1)
    i=find_double(tab5)
    if i!=0:
        tab_double5.append(i)
    list(set(tab_double5)) 

#tirage des doublons pour 2 etoiles       
while len(tab_double2)<2:
    tab2=gen_tab2(taba)
    i=find_double(tab2)
    if i!=0:
        tab_double2.append(i)
    list(set(tab_double2)) 

for i in tab_double5:
    print(i),

print('etoiles:'),
for i in tab_double2:
    print(i),
       
     
