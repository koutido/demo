import random
question=['Question 1: dung hay sai',
          'Question 2: cai nao day?',
          'Question 3: nuoc nao?']
choix=['A. dung \n B. sai',
       'A. cai nay \n B. cai kia \n C. cai no',
       'A. Anh \n B. Phap \n C. Mi \n D. Viet Nam']
reponse=['A','C','D']
note=0
while question:
    n=random.randint(0,len (question)-1)
    print(question[n])
    print(choix[n])
    rep=raw_input("Votre réponse: ")
    if rep==reponse[n]:
        note=note+1
    question.pop(n)
    choix.pop(n)
    reponse.pop(n)
print("Fin des questions")
print("Votre note: "),
print(note)

