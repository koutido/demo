for i in range(5):
    nom=raw_input('Entrez un nom')
    monFichier=open('fichier.txt','a')
    monFichier.write(nom)
    monFichier.write('\n')
    monFichier.close()
    print('fichier enregistré')
    
