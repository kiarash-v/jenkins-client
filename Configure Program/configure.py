import os
from getpass import getuser
from shutil import rmtree

def asking_user_decision(displayMessage):
    '''
    This process is repeated many times in the code asking the user for yes/no answer
    so this process is turned into a function for simplicity

    :param displayMessage:  Message to be displayed for asking user his/her decision
    '''
    while True:
        UserDecision = input(displayMessage)
        if UserDecision.lower() in "y yes ye":
            return True
        elif UserDecision.lower() in "n no":
            return False


def create_desktop_shortcut():
    UserDecision=asking_user_decision("Do you want to create desktop shortcut for programs?[y/n] ")
    return True if UserDecision else False



username = (getuser())
print()
print("\t\t******** Welcome to JC initial setup ***********")
UserDecision=asking_user_decision("Start?[y/n] ")
if UserDecision:


    if os.path.exists("C:\\users\{0}\JC".format(username)):
        rmtree("C:\\users\{0}\JC".format(username))
        print("-directory {0} removed successfully".format("C:\\users\{0}\JC".format(username)))

    os.mkdir("C:\\users\{0}\JC".format(username))
    print("-directory {0} created successfully".format("C:\\users\{0}\JC".format(username)))
    os.mkdir("C:\\users\{0}\JC\Jobs".format(username))
    print("-directory {0} created successfully".format("C:\\users\{0}\JC\Jobs".format(username)))
    fh=open("C:\\users\{0}\JC\Built".format(username),'w')
    fh.close()
    print("-file {0} created successfully".format("C:\\users\{0}\JC\Built".format(username),'w'))
    fh=open("C:\\users\{0}\JC\controls".format(username),'w')

    UserDecision=asking_user_decision("Do you want to change the location of job.conf and server.conf for better access?[y/n] ")
    if UserDecision:
        while True:
            Location=input("Enter location : ")
            if Location[-1]=="\\":
                Location=Location[:-1]
            Location=Location.replace("\\","\\\\")
            if os.path.exists(Location):
                if not os.path.isdir(Location):
                    print("Location is not a directory")
                else:
                    fh.write("job.conf={0}".format("{0}\\\\job.conf\n").format(Location))
                    fh.write("server.conf={0}".format("{0}\\\\server.conf\n".format(Location)))
                    os.system("copy .\job.conf  {0}".format("{0}\\".format(Location)))
                    os.system("copy .\server.conf  {0}".format("{0}\\".format(Location)))

                    break
            else:
                UserDecision=asking_user_decision("Location does not exist.Do you want to create it now?[y/n] ")
                if UserDecision:
                    os.system("mkdir {0}".format(Location))
                    print("-directory {0} created successfully".format(Location))
                    fh.write("job.conf={0}".format("{0}\\\\job.conf\n".format(Location)))
                    fh.write("server.conf={0}".format("{0}\\\\server.conf\n".format(Location)))
                    os.system("copy .\job.conf  {0}".format("{0}\\".format(Location)))
                    os.system("copy .\server.conf  {0}".format("{0}\\".format(Location)))

                    break


    else:
        fh.write("job.conf={0}".format("C:\\\\users\\\\{0}\\\\JC\\\\job.conf\n".format(username)))
        fh.write("server.conf={0}".format("C:\\\\users\\\\{0}\\\\JC\\\\server.conf\n".format(username)))
        os.system("copy .\job.conf  {0}".format("C:\\\\users\\\\{0}\\\\JC\\\\".format(username)))

        os.system("copy .\server.conf  {0}".format("C:\\\\users\\\\{0}\\\\\JC\\\\".format(username)))

    fh.write("built={0}".format("C:\\\\users\\\\{0}\\\\JC\\\\Built\n".format(username)))
    fh.write("jobdir={0}".format("C:\\\\users\\\\{0}\\\\\JC\\\\Jobs\\\\\n".format(username)))
    fh.close()

    if create_desktop_shortcut():
        os.system("copy .\jc.exe  {0}".format("C:\\\\users\\\\{0}\\\\Desktop\\\\".format(username)))
        os.system("copy .\jcr.exe  {0}".format("C:\\\\users\\\\{0}\\\\Desktop\\\\".format(username)))
        print("\nSetup completed")
        print("Thank you")
        end = input()
        exit()



    else:
        print("\nSetup completed!!!")
        print("Thank you")
        end = input()
        exit()


else:
    exit()
    end = input()
    exit()
