table=0
while table==0:
    choix=raw_input("Quelle table de multiplication voulez vous de 1 à 9? ")
    table=int(choix)
    i=1
    if table<1 or table>9:
        table=0
    else:
        while i<=10:
            print(i),
            print(" x "),
            print(table),
            print(" = "),
            print(i*table)
            i=i+1

