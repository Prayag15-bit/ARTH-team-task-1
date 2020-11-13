import os
import time 
os.system("clear")
time.sleep(1)
os.system("tput setaf 1")
print("-----------------------------")
print("""|   |
|___|  ___            ____
|   | |___|  |   |   (    )
|   | |____  |__ |__ (____)""")
print("-----------------------------")
os.system("tput setaf 11")
print("\n")
time.sleep(1)
print("""+++++++++++++++++++++++++++++++++++++++++
Welcome to our Python Automation Program
+++++++++++++++++++++++++++++++++++++++++""")
print("\n")
time.sleep(1)
os.system("tput setaf 14")
print("""+++++++++++++++++++++++++++++++++++++
A one-stop program for all your needs
+++++++++++++++++++++++++++++++++++++""")
print("\n")
time.sleep(1)
os.system("tput setaf 26")
print("=============================================")
print("Created with the efforts and dedication of :-")
os.system("tput setaf 70")
time.sleep(0.5)
print("1. Mahima Jindal")
time.sleep(0.5)
print("2. Pawar Suvarna")
time.sleep(0.5)
print("3. Prayag Magotra")
time.sleep(0.5)
print("4. Jitender Mahara")
time.sleep(0.5)
os.system("tput setaf 26")
print("=============================================")
print("\n")
time.sleep(0.5)
while True:
    os.system("tput setaf 7")
    print("-------------------------------------------------------------------")
    print("The list of the integrated technologies used in this program are :-")
    print("-------------------------------------------------------------------")
    time.sleep(0.25)
    print("1. Amazon Web Services (AWS)")
    time.sleep(0.25)
    print("2. Basic Linux Operations")
    time.sleep(0.25)
    print("3. Docker Engine")
    time.sleep(0.25)
    print("4. Hadoop")
    time.sleep(0.25)
    print("5. LVM")
    time.sleep(0.5)
    print("--------------------------------------------------------------------")
    print("Press '0' to exit the program")
    print("\n")
    time.sleep(0.25)
    print("Enter the number of the tool you want to work on : ", end="")
    tool_name = input()
    if int(tool_name) == 1:
        os.system("python3 aws-cli.py")
    elif int(tool_name) == 2:
        os.system("python3 linux.py")
    elif int(tool_name) == 3:
        os.system("python3 docker.py")
    elif int(tool_name) == 4:
        os.system("python3 hadoop.py")
    elif int(tool_name) == 5:
        os.system("python3 LVM.py")
    elif int(tool_name) == 0:
        time.sleep(0.5)
        print("\n")
        print("++++++++++++++++++++++++++++++++++++++")
        print("Exiting the program..... See ya around")
        print("++++++++++++++++++++++++++++++++++++++")
        time.sleep(1.5)
        print("\n")
        exit()
    else:
        print("INVALID CHOICE")
    input("To continue, hit enter")
    os.system("clear")





