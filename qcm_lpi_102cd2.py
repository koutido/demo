import random
question=['Where is the UID number range that can be assigned to new user accounts defined?',
          'You need to create a new user account for a user named George Sanders on your Linux system. You want to specify a user name of gsanders, a full name of George Sanders, a default shell of /bin/bash, and that a home directory be created. Which command will do this?',
          'The asanders user has recently married and changed her last name to Ebbert. Which command can be used to update her user account with her new last name?',
          'Where is the GID number range that can be assigned to new groups defined?',
          'You need to add the aebbert user to the dbusers group. Which command can be used to do this?',
          'You need to run the updatedb command two hours in the future. Which commands will do this? (Choose two.)',
          'Which at command can be used to view a listing of pending at jobs?',
          'You need to run the tar command to back up the /home directory using the tar –cvf /media/usb/backup.tar /home command every day of every month, except Sundays, at 11:05 P . M . Which crontab entry will accomplish this?',
          'Which file is used to restrict which users are allowed to create crontab files on your Linux system? (Choose two.)',
          'You are logged in to your Linux system as the tuxuser and need to set up a cron job. Which command can be used to edit tux’s crontab file?',
          'You’re writing a script that will require the end user to enter the name of his or her supervisor. Which of the following lines will input the user’s response into a variable named SUP?',
          'You’ve just created a new script in your home directory named runme.sh. When you try to run your script while in your home directory using the ./runme.sh command from the shell prompt, you see the following error: bash: ./runme.sh: Permission denied. Which resolution will fix this issue?',
          'You need to assign a numeric value to a variable named NUM1 in a script so that you can perform mathematical operations on it. Which line can you add to your script to do this?',
          'You need to write an if/then/else statement in a script that will test to see if a file named /var/opt/mydb/mydb exists and has the write permission assigned for the user running the script. Which statement will do this?',
          'You need to implement a for loop in a script. You want to use the seq command to generate a sequence of numbers that starts at 1, increments by 1, and stops at 100. Which statements will do this? (Choose two.)',
          'Which script structure executes over and over until a specified condition is no longer true.',
          'Which protocols operate at the Network layer of the OSI model? (Choose two.)',
          'Which port is used by the FTP protocol for its control connection?',
          'Which IP addresses are private (sometimes called reserved) addresses? (Choose two.)',
          'Consider the following IP address: 172.17.8.10/22. Which subnet mask is assigned to this address?']

choose=[' A. /etc/login.defs \n B. /etc/default/useradd \n C. /etc/skel \n D. /etc/passwd',
        ' A. useradd –c "George Sanders" –m –s "/bin/bash" gsanders \n B. useradd –c "George Sanders" –m –s "/bin/bash" –u gsanders \n C. usermod –c "George Sanders" –m –s "/bin/bash" gsanders \n D. useradd –c "George Sanders" –s "/bin/bash" gsanders',
        ' A. usermod –l asanders –c "Amber Ebbert" aebbert \n B. usermod –l aebbert –c "Amber Ebbert" –u asanders \n C. usermod –l aebbert –c "Amber Ebbert" asanders \n D. usermod–c "Amber Ebbert" asanders',
        ' A. /etc/login.defs \n B. /etc/default/useradd \n C. /etc/skel \n D. /etc/default/groupadd',
        ' A. useradd –g dbusers aebbert \n B. usermod –g dbusers aebbert \n C. groupadd –A "aebbert" dbusers \n D. groupmod –A "aebbert" dbusers',
        ' A. at now + 2 hours \n B. at updatedb –t +120m \n C. at now + 120 minutes \n D. at now + 2 hours updatedb \n E. at now + 2 hours updatedb',
        ' A. at –l \n B. atq \n C. atrm \n D. at –listjobs',
        ' A. 5 11 * * 1-6 /bin/tar –cvf /media/usb/backup.tar /home \n B. 5 23 * * * /bin/tar –cvf /media/usb/backup.tar /home \n C. 5 23 * * 1-6 /bin/tar –cvf /media/usb/backup.tar /home \n D. 11 5 * * 0-5 /bin/tar –cvf /media/usb/backup.tar /home',
        ' A. /etc/cron.deny \n B. /etc/cronusers.deny \n C. /etc/hosts.deny \n D. /etc/cron.allow \n E. /etc/hosts.allow \n F. /etc/cronusers.allow',
        ' A. crontab –e \n B. crontab –l \n C. crontab –r \n D. crontab –i \n E. vi /var/spool/cron/tabs/tux',
        ' A. read SUP \n B. input SUP \n C. prompt SUP \n D. query SUP',
        ' A. Copy the file to the ~/bin directory. \n B. Add your home directory to the PATH environment variable. \n C. Enter chmod u+x runme.sh at the shell prompt. \n D. Change the she-bang line of the script to #!/bin/sh.',
        ' A. declare –i NUM1 \n B. type NUM1 integer \n C. declare –r NUM1 \n D. declare –f NUM1',
        ' A. if test –e /var/opt/mydb/mydb; then... \n B. if test –w /var/opt/mydb/mydb; then... \n C. if test –f /var/opt/mydb/mydb; then... \n D. if test –x /var/opt/mydb/mydb; then...',
        " A. for i in 'seq 1 5 100' \n B. for i in 'seq 100' \n C. for i in 'seq 1 1 100' \n D. for i in 'seq 1-100' \n E. for i in 'seq 1..100'",
        ' A. For loop \n B. Case \n C. While loop \n D. Until loop',
        ' A. IP \n B. TCP \n C. UDP \n D. ICMP \n E. HTTP',
        ' A. 20 \n B. 21 \n C. 25 \n D. 110 \n E. 137',
        ' A. 11.23.5.254 \n B. 172.17.8.1 \n C. 10.254.254.1 \n D. 192.169.1.10 \n E. 137.65.5.5',
        ' A. 255.255.252.0 \n B. 255.255.0.0 \n C. 255.255.255.0 \n D. 255.255.255.252']

answer=['A','A','C','A','D','AC','B','C','AD','A',
        'A','C','A','B','BC','C','AD','B','BC','A']

note=0
num=1
while question:
    n=random.randint(0,len (question)-1)
    print('Question '+str(num)+': '),
    print(question[n])
    print(choose[n])
    rep=raw_input("Your answer: ")
    if rep==answer[n]:
        note=note+1
    question.pop(n)
    choose.pop(n)
    answer.pop(n)
    num=num+1
    print('***********************************************************************************')
print("The end of the questions")
print("Your result: "),
print(note)
