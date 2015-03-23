#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#Ligne 1 necessaire sous Linux
 
from Tkinter import *
from math import *
import random
 
 
 
 
#Liste + variable
compteur=0
nombre_de_question=0
 
liste_questions=["Question  : Quelle est la capitale du Liban ?\n ",\
				"Question  : Quand l'armistice de la seconde Guerre Mondiale a-t-elle été signée ? ",\
				"Question  : Quelle est la capitale de l'Estonie /n? ",\
				"Question  : Quelle est la langue maternelle la plus parlée au monde ? \n",\
				"Question  : Quelle est la langue officielle au Nigeria \n?",\
				"Question  : Qui a réalisé le père noel est une ordure ? \n",\
				"Question  : Quel est l'état le plus grand des Etats-Unis ?",\
				"Question  : Qui a écrit l'Assommoir ? \n",\
				"Question  : La pénicilline a été découverte par : \n",\
				"Question  : Le premier président de la République était : \n",\
				"Question  : En quelle année ont été créées les régions ? \n",\
				"Question : Que collectionne un conchyophile ? \n",\
				"Question  : Quelle est la ville la plus peuplée du monde ? \n",\
				"Question  : Quelle formule mathématique permet d'établir les développements limités ? \n",\
				"Question  : Quel évènement a marqué l'année 1935 ? \n",\
				"Question : Quelle est la hauteur de la Tour Eiffel ? \n",\
				"Question  : Quel est l'organe le plus volumineux et le plus massif parmi ceux-ci ? \n",\
				"Question : En quelle année Neil Amstrong a-t-il posé le premier pas sur la lune ? \n",\
				"Question : Quel chanteur fait partie des Rolling Stones ? \n",\
				"Question : Quelle équipe de football a remporté la première coupe du monde en 1930 ? \n"]
 
liste_choix=["1) Beyrouth,2) Damas,3) Rabat ",\
			"1) 8 mai 1945,2) 11 novemble 1945,3) 18 juin 1940 ",\
				"1) Riga,2) Tallin,3) Vilnius",\
				"1) L'Anglais,2) L'espagnol,  3) le chinois madarin ",\
				"1) L'anglais,2) Le nigerian,3) L'afrikaans ",\
				"1) Coline Serreau,2) Gerard Oury,3) Jean Marie Poiré ",\
				"1) Le Texas,2) L'Alaska,3) Le Montana ",\
				"1) Stendhal,2) Flaubert,3) Zola ",\
				"1) Ian Fleming,2) Alexander Flening,3) Marie Curie ",\
				"1) R.Coty,2) A.Pinay,3) V.Auriol ",\
				"1) 1806,2) 1956,3) 1901 ",\
				"1) Des bières,2) des coquillages,3) Des animaux empaillés ",\
				"1) Tokyo,2) Mexico,3) New York ",\
				"1) Schrodinger,2) Crutz,3) Taylor ",\
				"1) Les lois sociales du Front populaire,2) Lois de Nüremberg,3) Hitler chancelier ",\
				"1) 250 mètres,2) 324 mètres,3) 295 mètres ",\
				"1) Le foie,2) L'estomac,3) Le colon ",\
				"1) 1967,2) 1969,3) 1971 ",\
				"1) Jonh Lennon,2) Mick Jagger,3) Brian Johnson ",\
				"1) Italie,2) Brésil,3) Uruguay "]
 
liste_reponse=[1,1,2,3,1,3,2,3,2,3,2,2,1,3,2,2,1,2,2,3]
 
 
 
 
#début du programme 
def quest():
	newWindow= Tk()
	newWindow.title('Question')
	newWindow.geometry("400x300+600+400")
	Mafenetre.destroy()
	global compteur 
	print("commençons !\n ")
 
	while liste_questions :
		n=random.randint(0,len (liste_questions)-1)
		print (liste_questions[n])
		print (liste_choix[n])
		Q=int(input("quel numéros choississez-vous ?"))
		if Q == liste_reponse[n]:
			 compteur = compteur +1
		liste_questions.pop(n)
		liste_choix.pop(n)
		liste_reponse.pop(n)
	print ("c'est finis")
 
	#système de note + commentaire :		
	print("Note:")	
	if compteur == 20 :
		showinfo('NOTE', "20/20...Que pouvons nous dire... si ce n'est BRAVO")		
 
	elif 19>=compteur>=16 :
		showinfo('NOTE', "19/20 C'est presque excellent... Courage ! Le succes est au bout du chemin.")
 
	elif 15>=compteur>=12 :
		showinfo('NOTE',"Tu as entre 12/20 et 15/20. Ne sois pas modeste, tu peux mieux faire !")
 
	elif 11>=compteur>=10 :
		showinfo('NOTE',"Tu as entre 10/20 et 11/20. Il faut tra-vai-ller !")
 
	elif 9>=compteur>=6 :
		showwarning('NOTE', "Tu as entre 9 et 6. Tu sais ce qu'il te reste à faire ..." )
 
	elif 5>=compteur>=0 :
		showwarning('NOTE',"Tu as en dessous de 5/20... Sans commentaire...")
#~ else :
	#~ print (" à une prochaine fois")	
 
 
 
 
# Création de la fenêtre principale (main window)
def ihm():
	Mafenetre = Tk()
 
	Mafenetre.title('QCM')
	Mafenetre.geometry('400x300+600+400')
 
	Label1 = Label(Mafenetre, text = 'Voici un petit QCM présenté par Jonathan, Thibault , Landry ')
	Label1.pack(side = TOP, padx = 5, pady = 5)
 
 
	Label2 = Label(Mafenetre, text = 'Voulez- vous commencez ? ')
	Label2.pack(side = LEFT, padx = 5, pady = 5)
 
	Bouton = Button(Mafenetre, text ='Oui', command = quest )
	Bouton.pack(side = LEFT, padx = 5, pady = 5)
 
	Bouton = Button(Mafenetre, text ="Non", command = Mafenetre.destroy )
	Bouton.pack(side = LEFT, padx = 5, pady = 5)
 
	return Mafenetre
 
 
 
 
if __name__ == "__main__":
	Mafenetre = ihm()
	Mafenetre.mainloop()
