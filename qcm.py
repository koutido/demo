def menu():
    print("Choisir un sujet: ")
    print("1-Sujet A")
    print("2-Sujet B")

#afficher le contenu d'un tableau
def list_display(tab):
    for ligne in tab:
        print(ligne)

#déterminer si le début d'une ligne est un chiffre
def is_question(ligne):
    debut=ligne[0:1]
    #return isinstance(debut,int)
    return debut.isdigit()

#copier les questions et les réponses dans 2 tableaux différents
#le 3ème tableau pour stocker le nombre de réponses de chaque question
def file_to_list(fichier,tab_quest,tab_rep):
    #compteur question
    nb_quest=0
    #compteur réponses
    nb_rep=0
    for ligne in fichier:
        ligne=ligne.strip('\n')
        if is_question(ligne)==True:         
            #une nouvelle question, donc il faut sauvegarder le nombre de réponses de la précédente
            if nb_rep>0:
                tab_quest.append(nb_rep)
                nb_rep=0
            tab_quest.append(ligne)
        else:
            tab_rep.append(ligne)
            nb_rep=nb_rep+1
            #print(ligne)
    #ajouter le dernier nb de réponses pour la dernière question
    #print(nb_rep)
    if nb_rep>0:
        tab_quest.append(nb_rep)

#afficher la question et ses réponses et retourner le tableau des questions affichées
def question_display(tab_quest,tab_rep):
    displayed=[]
    if len(tab_quest)>0 and len(tab_rep)>0:
        question=tab_quest.pop(0)
        nb_question=tab_quest.pop(0)

        print(question)
        #copier la question dans le tableau displayed
        displayed.append(question)
        #afficher les réponses de cette question
        for i in range(nb_question):
            reponse=tab_rep.pop(0)
            print(reponse)
            displayed.append(reponse)
    else:
        print("Plus de question a afficher")
    return displayed

#compter le nb de questions
def question_counter(fichier):
    nb=0
    for ligne in fichier:
        if is_question(ligne)==True:
            nb=nb+1
    return nb

#retourner la réponse
def answer(num):

    return reponse

#calculer la note
def note_calcul(can_rep,rep):

    return note

question=open('question.txt','r')
reponse=open('reponse.txt','r')
tab_question=[]
tab_reponse=[]
#nb_question=question_counter(question)
file_to_list(question,tab_question,tab_reponse)
for i in range(6):
    question_display(tab_question,tab_reponse)
#question_display(tab_question,tab_reponse)

question.close()
reponse.close()
