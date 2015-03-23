import random
question=['You need to assign the eth0 interface an IP address of 172.17.8.1 with a subnet mask of 255.255.0.0 and a broadcast address of 172.17.255.255. Which command will do this?',
          'Which directive in the /etc/sysconfig/network/ifcfg-eth0 is used to specify whether the interface is configured with static IP address information or with dynamic IP address information from a DHCP server?',
          'One of your Linux workstations has been configured with an incorrect default gateway router address. Which file do you need to edit to correct this?',
          'For security reasons, you want your Linux system to always try to resolve hostnames using your DNS server before trying to resolve them using the /etc/hosts file. Which file can you use to configure the name resolver order?',
          'Which netstat command can be used to view performance statistics about the network interfaces in your Linux system?',
          'Which directives in the /etc/cups/cupsd.conf file must be enabled to share your local printers with other CUPS-compatible systems on the network? (Choose two.)',
          'Which term refers to gradual time adjustments made by the NTP daemon to your system clock when the time difference',
          'You’ve just added a new e-mail alias to the /etc/aliases file for use with the postfix MTA on your Linux system. Which command do you now need to run to apply the change to the file?',
          'You are working with data in a MySQL database table named customers. The fields in this table are first, last, street, city, state, zip, and phone. You want to retrieve records with a value of 83401 in the zip field. Which SQL command will do this?',
          'The /etc/sudoers file on your Linux system is configured by default such that users must supply the root password when using sudo. You want to change this such that they only must supply their own password to use sudo. Which directives in the /etc/sudoers file must be commented out to do this? (Choose two.)',
          'You need to use the chage command to specify a minimum password age of five days, a maximum password age of 60 days, and five warning days for the tux user. Which command uses the correct syntax to do this?',
          'The existence of which file prevents everyone except for root from logging in?',
          'Which command will search for files on your Linux system that have SUID permissions set?',
          'Which commands will perform a scan for open TCP ports on the local system? (Choose two.)',
          'Which syslog facility can be used to capture log messages from an application you develop yourself?',
          'Which directive in a given service’s xinetd configuration file specifies whether or not xinetd is allowed to start the daemon when requested?',
          'Which private host keys are used by the sshd daemon during an SSH version 2 session? (Choose two.)',
          'To harden the sshd daemon running on your Linux system, you decide to configure it to listen for SSH requests on a port other than the default of 22. Which directive in your etc/ssh/sshd_config file can you use to do this?',
          'You want to redirect the display from the X server on one Linux system to another Linux client system securely through an SSH tunnel. Which directive in the /etc/ssh_config file on the X server system do you need to configure to allow this?',
          'To configure public key authentication, the first thing you need to do is create the public/private key pair on the client system so that you can send the public key to the SSH server. Which commands will do this? (Choose two.)']

choose=[' A. ifconfig eth0 172.17.8.1 mask 255.255.0.0 bcast 172.17.255.255 \n B. ifconfig 172.17.8.1 netmask 255.255.0.0 broadcast 172.17.255.255 \n C. ifconfig eth0 172.17.8.1 subnetmask 255.255.0.0 bcast 172.17.255.255 \n D. ifconfig eth0 172.17.8.1 netmask 255.255.0.0 broadcast 172.17.255.255',
        ' A. STARTMODE \n B. BOOTPROTOC. IPADDR \n D. USERCONTROL',
        ' A. /etc/sysconfig/network/routes \n B. /etc/sysconfig/network/ifcfg-eth0 \n C. /etc/hostname \n D. /etc/resolv.conf',
        ' A. /etc/resolv.conf \n B. /etc/sysconfig/network/ifcfg-eth0 \n C. /etc/nsswitch.conf \n D. /etc/sysconfig/services',
        ' A. netstat –l \n B. netstat –i \n C. netstat –rD. netstat –s',
        ' A. DefaultPolicy \n B. BrowseAddress \n C. Listen \n D. Policy \n E. Browsing',
        ' A. Stepping \n B. Slewing \n C. Drift \n D. Jitter',
        ' A. newaliases \n B. postfix --reload \n C. postfix --newaliases \n D. postfix –D \n E. updatealiases',
        " A. UPDATE customers WHERE zip='83401' \n B. SELECT zip='83401' FROM customers; \n C. SELECT * FROM customers WHERE zip='83401'; \n D. SELECT * FROM customers; \n E. VIEW * FROM customers WHERE zip='83401';",
        ' A. Defaults env_keep \n B. root ALL=(ALL) ALL \n C. Defaults env_reset \n D. Defaults targetpw \n E. ALL ALL=(ALL) ALL',
        ' A. chage –m 5 –M 5 –W 60 tux \n B. chage –m 60 –M 5 –W 5 tux \n C. chage tux –m 5 –M 60 –W 5 \n D. chage –m 5 –M 60 –W 5 tux',
        ' A. /etc/nologin \n B. /etc/pam.d/login \n C. /lib/security/pam_nologin.so \n D. /usr/bin/rlogin',
        ' A. find / –type f –perm –g=s –ls \n B. find / –type f –perm –u=s –ls \n C. find / –type f –perm –u=rwx –ls \n D. find / –type f –perm –g=rwx –ls \n E. find / –type f –perm –o=rwx –ls',
        ' A. nmap –sT localhostB. netstat –l \n C. nmap –sU localhost \n D. netstat –i \n E. netstat –r',
        ' A. user \n B. authpriv \n C. daemon \n D. local1',
        ' A. server_args \n B. server \n C. disable \n D. wait',
        ' A. etc/ssh/ssh_host_rsa_key \n B. /etc/ssh/ssh_host_key \n C. /etc/ssh/ssh_host_dsa_keyD. /etc/ssh/ssh_host_key.pub \n E. etc/ssh/ssh_host_rsa_key.pub',
        ' A. Port \n B. BindAddress \n C. Protocol \n D. Tunnel',
        ' A. Protocol \n B. LocalCommand \n C. ForwardX11 \n D. PasswordAuthentication',
        ' A. ssh-keygen –t rsa \n B. ssh-keygen –t dsa \n C. ssh-add ~/.ssh/id_rsa \n D. ssh-add ~/.ssh/id_dsa \n E. ssh-agent bash']

answer=['D','B','A','C','B','BE','B','A','C','DE',
        'D','A','B','AB','D','C','AC','A','C','AB']

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
