#fonction qui affiche le menu
def menu():
    print("0-Quitter")
    print("1-Ecrire dans le répertoire")
    print("2-Rechercher dans le répertoire")

def ecriture(nom,num):
    fichier=open('carnet.txt','a')
    fichier.write(nom)
    fichier.write('\n')
    fichier.write(str(num))
    fichier.write('\n')
    fichier.close()

def lecture(nom):
    erreur='Inconnu'
    fichier=open('carnet.txt','r')
    #liste des contacts et numéro 
    contact=[]
    #lire le carnet.txt et écrire dans la liste contact
    for ligne in fichier:
        ligne=ligne.strip('\n')
        contact.append(ligne)
    fichier.close()
    #recherche de nom dans la liste
    for i in contact:
        if i==nom:
            index=contact.index(i)
            return contact[(index+1)]
    return erreur

i=3
#fin de la boucle quand i=0
while i==3:
    menu()
    choix=raw_input('Votre choix? ')
    if int(choix)==0:
        i=0
    if int(choix)==1:
        fin='false'
        while fin=='false':
            nom=raw_input("Nom (0 pour terminer) : ")
            if nom=='0':
                fin='true'
            else:
                num=raw_input("Téléphone : ")
                ecriture(nom,num)
    if int(choix)==2:
        nom=raw_input("Entrer un nom : " )
        print("Le numéro recherché est: "),
        print(lecture(nom))

        
    
