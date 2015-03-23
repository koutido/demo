import random
question=['Which bash shell configuration files contain parameters that are applied system wide (Choose two.)',
          'You’ve logged in to your Linux system through the GNOME graphical desktop environment. You’ve opened a terminal session within GNOME to complete several command-line tasks. Which bash configuration files were used to configure the bash environment within the shell session? (Choose two.)',
          'In your user’s home directory, there are four hidden bash shell configuration files: ~/.bash_profile, ~/.bash_login, ~/.bashrc, and ~/.profile. Which file will be used by default for bash login shells?',
          'You want to create a new alias on your system named ldir that will run the ls –al command when executed. Which command will do this?',
          'Which locale variable is used to define the currency format used in your location?',
          'Which locale environment variable has the highest degree of precedence on a Linux system?',
          'Which of the following terms refers to the clock that runs via software within the Linux kernel?',
          'Where are time zone settings stored? (Choose two.)',
          'Which environment variable specifies a Linux system’s time zone?',
          'Which configuration files are used to store your X server configuration settings? (Choose 2.)',
          'Which section of the /etc/X11/xorg.conf file is used to specify global X server options?',
          'The ServerLayout section within the /etc/X11/xorg.conf file ties together two other types of sections found within the file. What are they? (Choose two.)',
          'Which environment variable specifies which display manager is loaded by default when the X environment is initially loaded?',
          'Which option, when added to the :0 line of the /etc/xdm/Xservers file, will configure the display manager to use 24-bit color?',
          'The /etc/xdm/Xservers file on your Linux system contains the following entry: :0 local /usr/X11R6/bin/X -nolisten tcp -br vt7. Which parameter must be removed in order to enable remote access to the display manager on this host?',
          'Which AccessX setting allows users to lock modifier keys such as CTRL and SHIFT ?',
          'Which mouse accessibility setting allows you to send a mouse click whenever the mouse pointer stops moving for a specified amount of time?',
          'When using local authentication on a Linux system, which file contains the passwords for your user accounts?',
          'Consider the following entry from the /etc/passwd file: ksanders:x:1001:100:Kimberly Sanders:/home/ksanders:/bin/bash. What user ID (UID) has been assigned to this user account?',
          'Consider the following entry from the /etc/shadow file: ksanders:$2a$05$KL1DbTBqpSEMiL.2FoI3ue4bdyR.eL6GMKs7MU6.nZl5 SCC7/REUS:15043:1:60:7:5::. In how many days will this account be disabled after the user’s password has expired?']

choose=[' A. /etc/bash.bashrc \n B. ~/.profile \n C. ~/.bashrc \n D. /etc/profile \n E. /etc/environment',
        ' A. /etc/profile \n B. ~/.profile \n C. /etc/bashrc \n D. ~/.bashrc \n E. ~/.bash_profile',
        ' A. ~/.bash_profile \n B. ~/.bash_login \n C. ~/.profile \n D. ~/.bashrc',
        ' A. alias --create ldir "ls –al" \n B. alias –new ldir="ls –al" \n C. alias ldir ls –al \n D. alias ldir="ls –al"',
        ' A. LC_MESSAGES \n B. LC_MONETARY \n C. LC_CURRENCY \n D. LC_MEASUREMENT',
        ' A. LC_ALL \n B. LC_MEASUREMENT \n C. LANG \n D. LANGUAGE',
        ' A. Hardware clock \n B. Time server \n C. System clock \n D. Local time',
        ' A. /etc/sysconfig/services \n B. /etc/timezone \n C. /etc/sysconfig/clock \n D. /etc/systemclock \n E. /etc/environment',
        ' A. TZ \n B. TIME \n C. TIME_ZONE \n D. CLOCK',
        ' A. /etc/X11/XF86Config \n B. /etc/sysconfig/windowmanager \n C. /etc/sysconfig/displaymanagerD. /etc/X11/xorg.conf \n E. /etc/X11/xinit',
        ' A. Files \n B. Module \n C. Modes \n D. ServerFlags',
        ' A. Screen \n B. Modes \n C. Device \n D. Monitor \n E. InputDevice',
        ' A. XAUTHORITY \n B. DISPLAY \n C. WINDOWMANAGERD. DISPLAYMANAGER',
        ' A. –color 24 \n B. –bpp 24 \n C. –24 \n D. –color_depth=24',
        ' A. local \n B. –nolisten tcp \n C. /usr/X11R6/bin/X \n D. –br vt7',
        ' A. RepeatKeys \n B. ToggleKeys \n C. SlowKeys \n D. StickyKeys',
        ' A. Simulated secondary click \n B. Dwell click \n C. Mouse gestures \n D. Delay keys',
        ' A. /etc/passwd \n B. /etc/passwords \n C. /etc/gshadow \n D. /etc/shadow',
        ' A. ksanders \n B. 1001 \n C. 100 \n D. Kimberly Sanders',
        ' A. 1 day \n B. 7 days \n C. 5 days \n D. Null value (Never)']


answer=['AD','CD','A','D','B','A','C','BC','A','AD',
        'D','AE','C','B','B','D','B','D','B','C']
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
