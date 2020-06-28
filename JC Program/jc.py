
from os import listdir
from os import remove
from os import path
from re import sub
from getpass import getpass
from getpass import getuser
from jenkins import Jenkins
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
from utils import *
from datetime import datetime

global_command_completer = WordCompleter([
    'show', 'read', 'create', 'delete',
    'select', 'connect', 'disconnect',
    'local', 'reconfig', 'server', 'jobs', 'job',
    'config', 'whoami', '?', '??', 'exit', 'quit'], ignore_case=True)

selected_job_command_completer = WordCompleter(['enable', 'disable', 'build', 'stat', 'history', '?', '??'],
                                               ignore_case=True)


class JC:
    def __init__(self):
        self.JCDirectoryLoc = ''
        self.JCBuiltFileLoc = ''
        self.JCServerConfFileLoc = ''
        self.JenkinsServerAddress = 'none'
        self.JenkinsServerPort = 'none'
        self.ServerHandler = None
        self.IpRegex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

        self.JCSelectedJobCommands = {
            '(enable)': ' - Enable the specified job on Jenkins Server',
            '(disable)': ' - Disable the specified job on Jenkins Server',
            '(build)': ' - Build the specified job on Jenkins Server',
            '(stat [*])': ' - Displays status and general information about the specified job',
            '(?)': ' - Displays list of available commands',
            '(??)': ' - Displays list of available commands verbosely',
            '(quit/exit)': ' - Quit Job configuration mode'

        }

        self.JigGlobalCommands = {
            '(show local jobs [*])': ' - Displays all jobs saved and waiting in your local machine to be created on server',
            '(show server jobs)': ' - Displays all jobs currently on your jenkins server',
            '(show build queue)': ' - Displays all jobs in build queue',
            '(delete local job)': ' - Deletes jobs on your local machine',
            '(delete server job)': ' - Deletes jobs on your jenkins server',
            '(reconfig server job)': ' - Reconfigures an existing job',
            '(select server job)': ' - Selects job and enter job configuration mode',
            '(connect)': ' - Connects to jenkins server',
            '(disconnect)': ' - Disconnects from jenkins server',
            '(create server job)': ' - Creates a new job on server ',
            '(?)': ' - Displays list of available commands',
            '(??)': ' - Displays list of available commands verbosely',
            '(exit / quit)': ' - Quit JC program'

        }

    def initialize(self):

        fh=open("C:\\Users\{0}\JC\controls".format(getuser()))
        for line in fh:
            if line.startswith('server.conf'):
                self.JCServerConfFileLoc=(line.split("=")[1]).strip()
            elif line.startswith('jobdir'):
                self.JCDirectoryLoc=(line.split("=")[1]).strip()
            elif line.startswith('built'):
                self.JCBuiltFileLoc=(line.split("=")[1]).strip()
            elif line.startswith('address'):
                self.JenkinsServerAddress=(line.split("=")[1]).strip()
            elif line.startswith('port'):
                self.JenkinsServerPort=(line.split("=")[1]).strip()
        fh.close()


    def display_introduction(self):
        '''
        Display an introduction message for the program containing the version and status of
        development
        '''

        print("     Welcome to JC 1.4")
        print("JC is a project which creates an interface to manage your Jenkins Server for your projects")
        print("This project is still under development ")

    def display_list_of_global_mode_commands(self, verbos=False, search_key=None):
        '''
        Display list of available commands in global mode

        :param verbos:  display description of command(s) if true
        :param search_key: display all commands starts with the 'key' param . default is None meaning all available commands

        '''

        print("---------------Commands---------------")
        if search_key is None:
            for command, description in self.JigGlobalCommands.items():
                print(command, description if verbos else '')
        else:
            for command, description in self.JigGlobalCommands.items():

                if command.startswith('({0}'.format(search_key)):
                    print(command, description if verbos else '')
        print("---------------------------------------")

    def display_list_of_selected_job_mode_commands(self, verbos=False, search_key=None):

        '''
        Display list of available commands in selected job mode

        :param verbos: display description of command(s) if true
        :param search_key: display all commands starts with the 'key' param . default is None meaning all available commands

        '''

        print("---------------Commands---------------")
        if search_key is None:
            for command, description in self.JCSelectedJobCommands.items():
                print(command, description if verbos else '')
        else:
            for command, description in self.JCSelectedJobCommands.items():
                if command.startswith('({0}'.format(search_key)):
                    print(command, description if verbos else '')
        print("---------------------------------------")

    def show_local_jobs(self, Detail=False):
        '''
        Display list of local jobs
        :param Detail: If True , Displays more detail about local jobs
        :return:
        '''

        # TODO display format
        if len(listdir(self.JCDirectoryLoc)) == 0:
            print("No local job")
        else:
            if Detail:
                print("Status".ljust(8), "CRL".ljust(23), "CRS".ljust(23), "RCFG".ljust(23), "Name")
                print("-----".ljust(8), "--------".ljust(23), "--------".ljust(23), "--------".ljust(23), "-----")

            else:
                print("Status".ljust(8),"Name".ljust(20))
                print("-----".ljust(8), "-----".ljust(33))

            fhandle = open(self.JCBuiltFileLoc)
            for line in fhandle:
                line = line.strip()
                if line.startswith("#"):
                    pass
                else:
                    if Detail:
                        Status=(line.split("@")[0]).ljust(8)
                        CRL = ((line.split("@")[1]).split(".")[0]).ljust(23)
                        CRS = ((line.split("@")[2]).split(".")[0] if line.split("@")[2]!='None' else 'None').ljust(23)
                        RCFG = ((line.split("@")[3]).split(".")[0] if line.split("@")[3]!='None' else 'None').ljust(23)
                        Name= (line.split("@")[4])
                        print(Status,CRL,CRS,RCFG,Name)
                    else:
                        Status = (line.split("@")[0]).ljust(8)
                        Name= (line.split("@")[4])
                        print(Status,Name)

            fhandle.close()



    def connect_to_jenkins_server(self):

        # Because if there is a problem in reading server.conf file
        # both IP address and Port number becomes none
        # so we just check server address to be none or not


        fh=open("C:\\Users\{0}\JC\controls".format(getuser()))
        for line in fh:
            if line.startswith('address'):
                self.JenkinsServerAddress=(line.split("=")[1]).strip()
            elif line.startswith('port'):
                self.JenkinsServerPort=(line.split("=")[1]).strip()
        fh.close()

        if self.JenkinsServerAddress !='none':
            print("Connecting {0}:{1}".format(self.JenkinsServerAddress, self.JenkinsServerPort))
            UserName = input("Username : ")
            Password = getpass("Password : ")
            self.ServerHandler = Jenkins('http://{0}:{1}'.format(self.JenkinsServerAddress, self.JenkinsServerPort),
                                         username=UserName, password=Password)

            # Checking successful connection to server by checking get_jobs() method
            try:
                self.ServerHandler.get_jobs()
                print("Connected successfully as {2}".format(self.JenkinsServerAddress, self.JenkinsServerPort, UserName))
            except:
                self.ServerHandler = None
                print("Connection to server Failed")

        else:
            print("-Server configuration parameters are not defined properly")
            print("-Check server.conf for parameters and then use jcr.exe to set them")


    def is_connected(self):
        '''
        Check whether we are connected to server or not
        '''
        return True if self.ServerHandler else False

    def disconnect_from_jenkins_server(self, place=None):
        '''
        Disconnect from the server
        :param place: Defines the place we are disconnecting . Displayed message can be different based on this parameter
        '''
        # TODO Close the TCP PORT

        if self.ServerHandler == None:
            # Disconnect and Stay in the program
            if place is None:
                print("You are already disconnected")
            return
        self.ServerHandler = None
        # Disconnect while exiting the program
        print("You are disconnected successfully")

    def create_server_job(self, JobName):
        '''
        Create a server job based on a config.xml file existing on the local machine
        :param JobName: job's name to be created
        '''

        if self.ServerHandler is None:
            print("Your are not connected to server")
            print("First connect by 'connect' command")
            return
        if not path.exists('{0}{1}{2}'.format(self.JCDirectoryLoc, JobName, '.config.xml')):
            print("-Job '{0}' config.xml file does not exist on your local machine".format(JobName))
            print("First create a config.xml file for job {0} by jigjr command".format(JobName))
        else:
            ListServerJobs = [server_job["name"] for server_job in self.ServerHandler.get_jobs()]
            if JobName in ListServerJobs:
                print("-Job '{0}' already exists on the server".format(JobName))
                AskingResult = self.asking_user_decision("Do you want to recreate job {0}?[y/n] : ".format(JobName))

                if AskingResult:
                    self.ServerHandler.delete_job(JobName)
                    print("-Deleting job '{0}' from server ..".format(JobName))

                    fhandle = open(self.JCDirectoryLoc + JobName + ".config.xml")
                    SelectedJobXml = fhandle.read()
                    fhandle.close()
                    self.ServerHandler.create_job(JobName, SelectedJobXml)
                    print("-Job '{0}' recreated successfully".format(JobName))

                    # Recreate a job is similar to reconfigure that job
                    update_built_file(self.JCBuiltFileLoc, 'update-reconfigure-date', JobName,
                                      reconfig_date=datetime.now())

            else:
                AskingResult = self.asking_user_decision("Sure creating job {0}?[y/n] : ".format(JobName))
                if AskingResult:
                    fhandle = open(self.JCDirectoryLoc + JobName + ".config.xml")
                    SelectedJobXml = fhandle.read()
                    fhandle.close()
                    self.ServerHandler.create_job(JobName, SelectedJobXml)
                    print("-Job '{0}' created successfully".format(JobName))
                    update_built_file(self.JCBuiltFileLoc, 'update-server-create-date', JobName,
                                      server_creation_date=datetime.now())

    def reconfigure_server_job(self, JobName, LocalConfigJobName=None):
        '''
        Reconfigure a server job
        :param JobName: Server job to be configured
        :param LocalConfigJobName:  If None , JobName.config.xml file is searched in local machine , else, LocalConfigJobName.config.xml is searched
        '''
        if self.ServerHandler is None:
            print("Your are not connected to server")
            print("First connect by 'connect' command")
            return
        ListServerJobs = [server_job["name"] for server_job in self.ServerHandler.get_jobs()]
        if JobName not in ListServerJobs:
            print("-Job '{0}' does not exist on the server".format(JobName))

        else:
            ListLocalJobs = [job.split(".")[0] for job in listdir(self.JCDirectoryLoc)]

            # If the LocalConfigJobName is not specified use the JobName as defualt
            LocalConfigJobName = JobName if LocalConfigJobName is None else LocalConfigJobName

            if LocalConfigJobName not in ListLocalJobs:
                print("-Job {0} config.xml file does not exist in your local machine".format(LocalConfigJobName))

            else:
                print("{0}.config.xml found".format(LocalConfigJobName))
                AskingResult = self.asking_user_decision("Sure reconfiguring job {0}?[y/n] : ".format(JobName))
                if AskingResult:
                    fhandle = open(self.JCDirectoryLoc + LocalConfigJobName + ".config.xml")
                    SelectedJobXml = fhandle.read()
                    fhandle.close()
                    self.ServerHandler.reconfig_job(LocalConfigJobName, SelectedJobXml)
                    print("-Job '{0}' reconfigured successfully".format(LocalConfigJobName))
                    update_built_file(self.JCBuiltFileLoc, 'update-reconfigure-date', LocalConfigJobName,
                                      reconfig_date=datetime.now())

    def show_build_queue(self):
        '''
        Display list of jobs which are currently under building process
        '''
        if self.ServerHandler is None:
            print("Your are not connected to server")
            print("First connect by 'connect' command")
            return
        else:
            BuildQueue = self.ServerHandler.get_queue_info()
            if len(BuildQueue) == 0:
                print("No job in build queue")
                return
            else:
                BuildQueueCounter = 1
                for job in BuildQueue:
                    jobInfo = self.ServerHandler.get_job_info(job['task']['name'])
                    print("{0}: {1}\tBuilding No: {2}".format(BuildQueueCounter, job["task"]["name"],
                                                              jobInfo['nextBuildNumber']))
                    BuildQueueCounter += 1

    def show_server_jobs(self):
        '''
        Display list of jobs currently configured on the server
        '''
        if self.ServerHandler is None:
            print("Your are not connected to server")
            print("First connect by 'connect' command")
            return
        else:
            if len(self.ServerHandler.get_jobs()) == 0:
                print("No job currently on the server")
            else:
                ListServerJobs = [server_job["name"] for server_job in self.ServerHandler.get_jobs()]
                # This list is to reduce the latency of display of all jobs
                # First collect information of all jobs then display
                ReadyList = []
                for job in ListServerJobs:
                    JobInfo = self.ServerHandler.get_job_info(job)
                    JobStatus = 'Disabled' if JobInfo['disabled'] else 'Enabled'
                    JobTotalBuilds = "0" if JobInfo['lastBuild'] is None else JobInfo['lastBuild']['number']
                    JobLastBuild = "None" if JobInfo['lastBuild'] is None else datetime.fromtimestamp(
                        self.ServerHandler.get_build_info(job, JobInfo['lastBuild']['number'])['timestamp'] / 1000)
                    ReadyList.append([JobStatus, JobTotalBuilds, JobLastBuild, job])

                print("Status".ljust(8), "Build".ljust(7), "Timestamp".ljust(22), "Name".ljust(20))
                print("-----".ljust(8), "-----".ljust(7), "------".ljust(22), "----".ljust(20))

                for j in ReadyList:
                    print(j[0].ljust(9), str(j[1]).ljust(6),('None' if str(j[2]) == 'None' else str(j[2]).split(".")[0]).ljust(22), j[3].ljust(20))



    def delete_local_job(self, JobName):
        '''
        Delete local jobs
        '''

        LocalJobs = [job.split(".")[0] for job in listdir(self.JCDirectoryLoc)]

        if JobName not in LocalJobs:
            print("-Job '{0}' does not exist in your local machine".format(JobName))
            return
        else:
            AskingResult = self.asking_user_decision("Sure deleting job '{0}'?[y/n] : ".format(JobName))
            if AskingResult:
                remove(self.JCDirectoryLoc + JobName + ".config.xml")
                print("-Job '{0}' removed successfully from your local machine".format(JobName))

                update_built_file(self.JCBuiltFileLoc, 'delete', JobName)

    def delete_server_job(self, JobName):
        '''
        Delete Specified server job
        '''
        if self.ServerHandler is None:
            print("Your are not connected to server")
            print("First connect by 'connect' command")
            return
        else:
            ListServerJobs = [server_job["name"] for server_job in self.ServerHandler.get_jobs()]
            if JobName not in ListServerJobs:
                print("-Job '{0}' does not exist in Jenkins Server".format(JobName))
                return
            else:
                AskingResult = self.asking_user_decision("Sure deleting job '{0}'?[y/n]: ".format(JobName))
                if AskingResult:
                    self.ServerHandler.delete_job(JobName)
                    print("-Job '{0}' removed successfully from server".format(JobName))
                    update_built_file(self.JCBuiltFileLoc, 'update-deploy-status-ND', JobName)

    def disable_server_job(self, JobName):
        '''
        Disable specified server job
        '''

        JobState = self.ServerHandler.get_job_info(JobName)['disabled']
        if JobState:
            print("-Job '{0}' is already disabled".format(JobName))
            return
        self.ServerHandler.disable_job(JobName)
        print("-Job '{0}' successfully disabled".format(JobName))

    def enable_server_job(self, JobName):
        '''
        Enable specified server job
        '''
        JobState = self.ServerHandler.get_job_info(JobName)['disabled']
        if not JobState:
            print("-Job '{0}' is already enabled".format(JobName))
            return
        self.ServerHandler.enable_job(JobName)
        print("-Job '{0}' successfully enabled".format(JobName))

    def build_server_job(self, JobName):
        '''
        Build specified server job
        '''
        JobState = self.ServerHandler.get_job_info(JobName)['disabled']
        if JobState:
            print("-Job '{0}' is disabled and cannot built".format(JobName))
        else:
            self.ServerHandler.build_job(JobName)
            print("-Job '{0}' successfully built".format(JobName))

    def stat_server_job(self, JobName, Detail=False):
        '''
        Display status of the selected job
        :param Detail: If * specified , more detail about job is displayed
        '''

        # Because building a job can take long time we do not display the status
        # until the building process gets done
        BuildQueue = self.ServerHandler.get_queue_info()

        for job in BuildQueue:
            if JobName == job["task"]["name"]:
                print("-Job '{0}' is under building process".format(JobName))
                return

        JobInfo = self.ServerHandler.get_job_info(JobName)
        JobName_Sta = "Name: {0}".format(JobName)
        JobStatus_Sta = "Status: {0}".format('Disabled' if JobInfo['disabled'] else 'Enabled')
        JobTotalBuilds_Sta = "TotalBuilds: {0}".format(
            "0" if JobInfo['lastBuild'] is None else JobInfo['lastBuild']['number'])
        JobLastBuild_Sta = "LastBuild: {0}".format("None" if JobInfo['lastBuild'] is None else datetime.fromtimestamp(
            self.ServerHandler.get_build_info(JobName, JobInfo['lastBuild']['number'])['timestamp'] / 1000))
        JobFirstBuild_Sta = "FirstBuild: {0}".format("None" if JobInfo['lastBuild'] is None else datetime.fromtimestamp(
            self.ServerHandler.get_build_info(JobName, JobInfo['lastBuild']['number'])['timestamp'] / 1000))

        JobLastCompletedBuild_Sta = "LastCompletedBuild: {0}".format(
            "None" if JobInfo['lastCompletedBuild'] is None else str(datetime.fromtimestamp(
                self.ServerHandler.get_build_info(JobName, JobInfo['lastCompletedBuild']['number'])[
                    'timestamp'] / 1000)).split(".")[0])
        JobLastFailedBuild_Sta = "LastFailedBuild: {0}".format(
            "None" if JobInfo['lastFailedBuild'] is None else str(datetime.fromtimestamp(
                self.ServerHandler.get_build_info(JobName, JobInfo['lastFailedBuild']['number'])['timestamp'] / 1000)).split(".")[0])
        JobLastStableBuild_Sta = "LastStableBuild: {0}".format(
            "None" if JobInfo['lastStableBuild'] is None else str(datetime.fromtimestamp(
                self.ServerHandler.get_build_info(JobName, JobInfo['lastStableBuild']['number'])['timestamp'] / 1000)).split(".")[0])
        JobLastSuccessfulBuild_Sta = "LastSuccessfulBuild: {0}".format(
            "None" if JobInfo['lastSuccessfulBuild'] is None else str(datetime.fromtimestamp(
                self.ServerHandler.get_build_info(JobName, JobInfo['lastSuccessfulBuild']['number'])[
                    'timestamp'] / 1000)).split(".")[0])
        JobLastUnstableBuild_Sta = "LastUnstableBuild: {0}".format(
            "None" if JobInfo['lastUnstableBuild'] is None else str(datetime.fromtimestamp(
                self.ServerHandler.get_build_info(JobName, JobInfo['lastUnstableBuild']['number'])['timestamp'] / 1000)).split(".")[0])
        JobLastUnsuccessfulBuild_Sta = "LastUnsuccessfulBuild: {0}".format(
            "None" if JobInfo['lastUnsuccessfulBuild'] is None else str(datetime.fromtimestamp(
                self.ServerHandler.get_build_info(JobName, JobInfo['lastUnsuccessfulBuild']['number'])[
                    'timestamp'] / 1000)).split(".")[0])

        print(JobName_Sta)
        print(JobStatus_Sta)
        print(JobTotalBuilds_Sta)
        print(JobLastBuild_Sta)
        print(JobLastStableBuild_Sta)
        print(JobLastCompletedBuild_Sta)

        if Detail:
            print(JobFirstBuild_Sta)
            print(JobLastFailedBuild_Sta)
            print(JobLastSuccessfulBuild_Sta)
            print(JobLastUnstableBuild_Sta)
            print(JobLastUnsuccessfulBuild_Sta)

    def select_server_job(self, JobName):
        '''
        Select a server job and enter selected job mode
        '''
        if self.ServerHandler is None:
            print("Your are not connected to server")
            print("First connect by 'connect' command")
            return
        else:

            ListServerJobs = [server_job["name"] for server_job in self.ServerHandler.get_jobs()]
            if JobName not in ListServerJobs:
                print("-Job '{0}'  not exist in Jenkins Server".format(JobName))
                return
            else:
                SelectedJobSession = PromptSession(
                    lexer=PygmentsLexer(SqlLexer), completer=selected_job_command_completer)
                while True:

                    try:
                        UserCommand = SelectedJobSession.prompt("(" + JobName + ')## ')
                        UserCommand = (sub(' +', ' ', UserCommand)).strip()

                        if UserCommand.startswith("??"):
                            keyValue = (UserCommand.split("??")[1].strip())
                            if keyValue == '':
                                jc.display_list_of_selected_job_mode_commands(verbos=True)
                            else:
                                jc.display_list_of_selected_job_mode_commands(search_key=keyValue, verbos=True)

                        elif UserCommand.startswith("?"):
                            keyValue = (UserCommand.split("?")[1].strip())

                            if keyValue == '':
                                jc.display_list_of_selected_job_mode_commands()
                            else:
                                jc.display_list_of_selected_job_mode_commands(search_key=keyValue)


                        elif UserCommand == "quit" or UserCommand == "exit":
                            return

                        elif UserCommand == "enable":
                            self.enable_server_job(JobName)

                        elif UserCommand == "disable":
                            self.disable_server_job(JobName)

                        elif UserCommand == "build":
                            self.build_server_job(JobName)

                        elif UserCommand == 'stat *':
                            self.stat_server_job(JobName, Detail=True)

                        elif UserCommand == 'stat':
                            self.stat_server_job(JobName)

                        elif UserCommand == "":
                            pass
                        else:
                            print("%Invalid Command")

                    except KeyboardInterrupt:
                        break
                    except EOFError:
                        break
                    except:
                        print("There was a problem in program")
                        return

    def get_whoami(self):
        '''
        Display who is connected to server
        '''
        if self.ServerHandler is None:
            print("Your are not connected to server")
            print("First connect by 'connect' command")
            return
        else:
            UserInfo = self.ServerHandler.get_whoami()
            print("Full Name : ", UserInfo["fullName"])
            print("Id : ", UserInfo["id"])

    def asking_user_decision(self, displayMessage):
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

    def get_job_directory(self):
        return self.JCDirectoryLoc


jc = JC()

jc.display_introduction()

jc.initialize()


jig_global_session = PromptSession(lexer=PygmentsLexer(SqlLexer), completer=global_command_completer)

while True:
    '''
    I put quit and exit outside the try/except because then for exiting
    the program I had to implement exit() method
    so I put it outside of tre/except and rest of commands are still in try/except block

    for handling *Invalid Commands* I had to make distinction between newline 
    so I added (elif UserCommand == "" ) condition too
    '''

    try:
        UserCommand = jig_global_session.prompt('## ' if jc.is_connected() else ">> ")
        UserCommand = (sub(' +', ' ', UserCommand)).strip()
    except KeyboardInterrupt:
        continue
    except EOFError:
        break

    if UserCommand == "quit" or UserCommand == "exit":
        jc.disconnect_from_jenkins_server(place='exit')
        quit()

    try:

        # ?? have higher precedence than ?
        # so we have to check it before ?

        if UserCommand.startswith('??'):
            Search_KeyWord = (UserCommand.split("??")[1].strip())
            if Search_KeyWord == '':
                jc.display_list_of_global_mode_commands(verbos=True)

            else:
                jc.display_list_of_global_mode_commands(search_key=Search_KeyWord, verbos=True)



        elif UserCommand.startswith('?'):

            Search_KeyWord = (UserCommand.split("?")[1].strip())

            if Search_KeyWord == '':
                jc.display_list_of_global_mode_commands()
            else:
                jc.display_list_of_global_mode_commands(search_key=Search_KeyWord)

        elif UserCommand == "show local jobs *":
            jc.show_local_jobs(Detail=True)

        elif UserCommand == "show local jobs":
            jc.show_local_jobs()


        elif UserCommand == 'connect':
            jc.connect_to_jenkins_server()

        elif UserCommand == 'disconnect':
            jc.disconnect_from_jenkins_server()

        elif UserCommand.startswith('create server job'):
            JobName = UserCommand.split(" ")
            JobName = '' if len(JobName) == 3 else (" ".join(JobName[3:]))
            JobName = JobName.replace("'", "")

            if JobName == '' and len(listdir(jc.get_job_directory())) != 0:
                print("% Incomplete Command (job name not specified)")
            elif JobName == '':
                print("No local job available to create on server")
                print("First create a local job with jigjr command")
            else:
                jc.create_server_job(JobName)

        elif UserCommand.startswith('reconfig server job'):
            JobNames = []
            s = ""
            for word in UserCommand.split():
                if word in 'reconfig server job':
                    pass
                elif word.count("'") == 2:
                    JobNames.append(word.replace("'", ""))
                elif word.count("'") == 1:
                    if s == "":
                        s = word
                    else:
                        JobNames.append((s + " " + word).replace("'", ""))
                        s = ""
                else:
                    JobNames.append(word)

            if len(JobNames) == 0:
                print("% Incomplete Command (job name not specified)")
            else:
                if len(JobNames) == 1:
                    jc.reconfigure_server_job(JobNames[0])
                else:
                    jc.reconfigure_server_job(JobNames[0], LocalConfigJobName=JobNames[1])





        elif UserCommand.startswith("show server job"):
            jc.show_server_jobs()

        elif UserCommand.startswith("delete local job"):
            JobName = UserCommand.split(" ")
            JobName = '' if len(JobName) == 3 else (" ".join(JobName[3:]))
            JobName = JobName.replace("'", "")

            if JobName == '' and len(listdir(
                    jc.get_job_directory())) == 0:  # if no local job exist then specifying a job name is optional
                print("No local job available to delete")
            elif JobName == '':
                print("% Incomplete Command (job name not specified)")
            else:
                jc.delete_local_job(JobName)

        elif UserCommand == "show build queue":
            jc.show_build_queue()

        elif UserCommand.startswith("delete server job"):
            JobName = UserCommand.split(" ")
            JobName = '' if len(JobName) == 3 else (" ".join(JobName[3:]))
            JobName = JobName.replace("'", "")

            if JobName == '':
                print("% Incomplete Command (job name not specified)")
            else:
                jc.delete_server_job(JobName)

        elif UserCommand.startswith("select server job"):
            JobName = UserCommand.split(" ")
            JobName = '' if len(JobName) == 3 else (" ".join(JobName[3:]))
            JobName = JobName.replace("'", "")

            if JobName == '':
                print("% Incomplete Command (job name not specified)")
            else:
                jc.select_server_job(JobName)

        elif UserCommand == "whoami":
            jc.get_whoami()

        elif UserCommand == "":
            pass
        else:
            print("%Invalid Command")

    except KeyboardInterrupt:
        continue
    except EOFError:
        break
    except:
        print("There was a problem in program")



