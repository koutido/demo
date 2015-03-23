import random

#tab1=[17,31,33,44,50]
#taba=[7,11]
tab1=[5,2,18,43,30]
taba=[10,1]
tab5=[]
tab2=[]
test=[12,32,1,12,4]
tab_res=[]
for i in tab1:
    #print("chiffre du tab1"),
    #print(i)
    #numero cherche
    n=1
    numbers=range(1,51)

    c=0
    while numbers:
        # melanger la liste numbers
        random.shuffle(numbers)
        c=numbers.pop()
        #print("numero du tirage"),
        #print c
        if c==i:
            #print("numero trouve"),
            #print n
            tab5.append(n)
            #chiffre trouve, vider le tableau
            numbers=[]
            #print(n)
        n=n+1
        #print n
              
for i in taba:
    n=1
    numbers=range(1,12)
    c=0
    while numbers:
        random.shuffle(numbers)
        c=numbers.pop()
        if c==i:
            tab2.append(n)
            numbers=[]
        n=n+1

  

for i in tab5:
    print(i),
print("etoiles:"),
for i in tab2:
    print(i),
    
