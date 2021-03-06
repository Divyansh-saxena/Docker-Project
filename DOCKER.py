import os

while True:
    print("""\n\n\t**************************************************************
        ################# WELCOME TO PROGRAM MENU ####################
          \n\t**************************************************************
        \n\n \t Press the following Keys to Continue :

               Press 1: Docker Installation 
               Press 2: for Docker yum error
               Press 3: Docker Compose Installation
               Press 4: To launch wordpress site with mysql database
	       Press 5  To stop the wordpress container
               Press 6: To see all docker images present in your system           
               Press 7: To see containers running
	       Press 8: To see the all commands in docker
               Press 0: EXIT

     """)

    choice = int(input("Enter your choice :"))

    if choice == 1:
        os.system("yum install docker-ce --nobest")

    elif choice == 2:
        os.system("firewalld-cmd --zone=public --add-masquerade --permanent")
        os.system("firewalld-cmd --zone=public --add-port=80/tcp")
        os.system("firewalld-cmd --zone=public --add-port=443/tcp")
        os.system("firewalld-cmd --reload")
        os.system("systemctl restart docker")
        printf("/n/n/tNOW your docker yum problem is solved Go and check................")

    elif choice == 3:
        os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
            os.system(" chmod +x /usr/local/bin/docker-compose")

    elif choice == 4:
        while True:
            os.system("clear")
            print("\n\nif you don't have wordpress and mysql image then follow these steps:\n\n")
            print("\n\t\tpress 1: for wordpress image ")
            print("\t\tpress 2: for mysql image")
            print("\n\n\tif you already have these images then follow to launch wordress ")
            print("\n\t\tpress 3: for launch wordpress server\n\n\n")
            print("\n\n\tpress 0: Back to main menu")
            choice1 = int(input("Enter your choice : "))
            if choice1 == 1:
                os.system("docker pull wordpress:5.1.1-php7.3-apache")
            elif choice1 == 2:
                os.system("docker pull mysql:5.1")
            elif choice1 == 3:
                os.system("docker-compose up -d")
            elif choice1 == 0:
                exit(1)
            else:
                print("oops wrong input try again.....................")

     elif choice == 5:
        os.system("docker-compose down -d")

     elif choice == 6:
        os.system("docker images")
        while True:
            os.system("clear")
            print(""" 
	            Press 1: To pull the image of centos:7
                    Press 2: To launch the centos:7
                    Press 3: To pull the image of latest version of ubuntu
                    Press 4: To launch the latest version of ubuntu
	            Press 5: Back to main menu
                """)
            choice1 = int(input("Enter your choice : "))
            elif choice1 == 1:
                os.system("docker pull centos:7")
                elif choice1 == 2:
                os.system("docker run -it centos:7")
            elif choice1 == 3:
                os.system("docker pull ubuntu:latest")
            elif choice1 == 4:
                os.system("docker run -it ubuntu:latest")
            elif choice1 == 5:
                exit(1)
     elif choice == 7:
        os.system("docker ps")
    elif choice == 8:
        os.system("docker --help")
    elif choice == 0:
        exit(0)






