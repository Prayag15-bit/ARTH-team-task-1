import os
import getpass
os.system("clear")
os.system("tput setaf 3")
print("\t\t\t-------------------------------")
os.system("tput setaf 2")
print("\t\t\tHey! Welcome to my personal TUI")
os.system("tput setaf 3")
print("\t\t\t-------------------------------")
os.system("tput setaf 1")
print("\t\t\t\tGlad to have you here")
os.system("tput setaf 3")
print("\t\t\t\t---------------------")
os.system("tput setaf 3")
print("\t\t++++++++++++++++++++++++++++++++++++++++++++++++++")
os.system("tput setaf 2")
print("\t\tREMEMBER, TO EXIT THE PROGRAM, ENTER '0' IN CHOICE")
os.system("tput setaf 3")
print("\t\t++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n")
os.system("tput setaf 3")
print("+++++++++++++++++++++++++++++++++++++++++")
os.system("tput setaf 2")
Key_to_access=getpass.getpass("Enter the password to get the acess: ")
print("\n")
os.system("tput setaf 7")
if Key_to_access!="redhat":
    print("WRONG PASSWORD ENTERED....")
    os.system("sleep 1")
    print("exiting the program.....")
    os.system("sleep 3")
    exit()
else:
    os.system("tput setaf 3")
    print("+++++++++++++++++++++++++++++++++++++++++++")
    os.system("tput setaf 2")
    print("Specify the way of your work (local/remote): ", end="")
    os.system("tput setaf 7")
    access=input()
if access=="local":
    os.system("clear")
    while True:
        print("--------------")
        print("""BASIC COMMANDS
--------------
        1. Press to see the current date
        2. Press to see a particular year's calender
        3. Press to check the manual of any command
-------------------
IP RELATED COMMANDS
-------------------
        4. Press to see your system's current IP and netmask
        5. Press to change the IP and netmask of your system
        6. Press to check the IP of any website
---------------------------
COMMANDS RELATED WITH 'USER'
---------------------------
        7. Press to create a new user
        8. Press to set the password of a user
        9. Press to delete a user
        10.Press to check whether a user exists or not
----------------
SELINUX COMMANDS
----------------
        11.Press to Enable/Disable SELinux
        12.Press to check the status of SELinux
----------------------
CONFIGURATION OF 'YUM'
----------------------
        13.Press to configure 'yum'""")

        print("Enter your choice: ", end="")
        ch=input()
        if int(ch)==1:
            os.system("date")
        elif int(ch)==2:
            print("Enter the year whose calender you want to see: ", end="")
            year=input()
            os.system("cal {}".format(year))
        elif int(ch)==3:
            print("Manual basically shows us how a command works or how it's syntax works")
            print("Enter the command whose manual you wan to see: ", end="")
            man=input()
            os.system("man {}".format(man))
        elif int(ch)==4:
            os.system("ifconfig enp0s3")
        elif int(ch)==5:
            print("Enter your new IP: ", end="")
            IP=input()
            print("Enter your new netmask: ", end="")
            netmask=input()
            os.system("ifconfig enp0s3 {0} netmask {1}".format(IP,netmask))
        elif int(ch)==6:
            print("Enter the website whose IP you want to find: ", end="")
            website=input()
            os.system("nslookup {}".format(website))
        elif int(ch)==7:
            print("Please give the new user name: ", end="")
            UserName=input()
            os.system("useradd {}".format(UserName))
        elif int(ch)==8:
            print("Enter the password for the user: ", end="")
            UserPassword=input()
            os.system("passwd {}".format(UserPassword))
        elif int(ch)==9:
            print("Enter the name of the user to be deleted: ", end="")
            UserDelete=input()
            os.system("userdel {}".format(UserDelete))
        elif int(ch)==10:
            print("Enter the name of the user: ", end="")
            user_name=input()
            os.system("id {}".format(user_name))
        elif int(ch)==11:
            print("Press '0' to disable or press '1' to enable SELinux: ", end="")
            status=input()
            os.system("setenforce {}".format(status))
        elif int(ch)==12:
            os.system("getenforce")
        elif int(ch)==13:
            print("Please wait while the code is being downloaded.....")
            os.system("sleep 2")
            print("This may take upto 5 mins")
            os.system("sleep 1")
            os.system("mkdir /root/cloning")
            os.system("git clone https://github.com/Prayag15-bit/YUM-repo-file.git /root/cloning")
            os.system("mv /root/cloning/rhel8.repo /etc/yum.repos.d/")
            os.system("rm /root/cloning/ -rvf")
            os.system("yum clean all")
            os.system("yum repolist")
            print("Your yum is configured successfully")
        elif int(ch)==0:
            print("Exiting the program.....")
            os.system("sleep 3")
            exit()
        else:
            print("INVALID CHOICE")
        input("If you want to continue, hit enter")
        os.system("clear")
elif access=="remote":
    print("Enter the IP whose remote access you want: ", end="")
    IP=input()
    print(IP)
    while True:
        print("--------------")
        print("""BASIC COMMANDS
--------------
        1. Press to see the current date
        2. Press to see a particular year's calender
        3. Press to check the manual of any command
-------------------
IP RELATED COMMANDS
-------------------
        4. Press to see your system's current IP and netmask
        5. Press to change the IP and netmask of your system
        6. Press to check the IP of any website
---------------------------
COMMANDS RELATED WITH 'USER'
---------------------------
        7. Press to create a new user
        8. Press to set the password of a user
        9.Press to delete a user
        10.Press to check whether a user exists or not
----------------
SELINUX COMMANDS
----------------
        11.Press to Enable/Disable SELinux
        12.Press to check the status of SELinux""")
        print("Enter your choice: ", end="")
        ch=input()
        if int(ch)==1:
            os.system("ssh {0} date".format(IP))
        elif int(ch)==2:
            print("Enter the year whose calender you want to see: ", end="")
            year=input()
            os.system("ssh {0} cal {1}".format(IP,year))
        elif int(ch)==3:
            print("Manual basically shows us how a command works or how it's syntax works")
            print("Enter the command whose manual you wan to see: ", end="")
            man=input()
            os.system("ssh {0} man {1}".format(IP,man))
        elif int(ch)==4:
            os.system("ssh {0} ifconfig enp0s3".format(IP))
        elif int(ch)==5:
            print("Enter your new IP: ", end="")
            IPAdress=input()
            print("Enter your new netmask: ", end="")
            netmask=input()
            os.system("ssh {0} ifconfig enp0s3 {1} netmask {2}".format(IP,IPAddress,netmask))
        elif int(ch)==6:
            print("Enter the website whose IP you want to find: ", end="")
            website=input()
            os.system("ssh {0} nslookup {1}".format(IP,website))
        elif int(ch)==7:
            print("Please give the new user name: ", end="")
            UserName=input()
            os.system("ssh {0} useradd {1}".format(IP,UserName))
        elif int(ch)==8:
            print("Enter the password for the user: ", end="")
            UserPassword=input()
            os.system("ssh {0} passwd {1}".format(IP,UserPassword))
        elif int(ch)==9:
            print("Enter the name of the user to be deleted: ", end="")
            UserDelete=input()
            os.system("ssh {0} userdel {1}".format(UserDelete))
        elif int(ch)==10:
            print("Enter the name of the user: ", end="")
            user_name=input()
            os.system("ssh {0} id {1}".format(IP,user_name))
        elif int(ch)==11:
            print("Press '0' to disable or press '1' to enable SELinux: ", end="")
            status=input()
            os.system("ssh {0} setenforce {1}".format(IP,status))
        elif int(ch)==12:
            os.system("ssh {0} getenforce".format(IP))
            print("Exiting the program.....")
            os.system("sleep 3")
            exit()
        else:
            print("INVALID CHOICE")
        input("If you want to continue, hit enter")
        os.system("clear")
else:
    print("Access is not specified/correct.....Exiting the program")
    os.system("sleep 3")

