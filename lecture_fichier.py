fichier=open('fichier.txt','r')
nom=[]
for ligne in fichier:
    ligne=ligne.strip('\n')
    nom.append(ligne)
fichier.close()
print("l'opération terminée")

for i in nom:
    print(i)
