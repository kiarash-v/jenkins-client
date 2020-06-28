# Generated from job.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jobParser import jobParser
else:
    from jobParser import jobParser

from os import listdir
from os import remove
from datetime import datetime
from getpass import getuser
from utils import update_built_file

# This class defines a complete listener for a parse tree produced by jobParser.
class jobListener(ParseTreeListener):

    def __init__(self):
        '''
            Naming convention is : ScopeDirective
        '''

        self.Errors = {
            1: "(Bad-declaration) specifying git branches without specifying the repository urls are mean",
            2: "(Bad-value) trigger method number should be 1,2,3",
            3: "(Bad-directive) root_pom directive is acceptable only if the project is a maven project",
            4: "(Double-Scope-Declaration) source scope is declared twice",
            5: "(Double-Scope-Declaration) build_triggers scope is declared twice",
            6: "(Double-Scope-Declaration) building scope is declared twice",
            7: "(Double-Scope-Declaration) poll_scm scope is declared twice",
            8: "(Double-Scope-Declaration) build_periodically scope is declared twice",
            9: "(Double-Scope-Declaration) build_after_other_projects scope is declared twice",
            10: "(Double-Directive-Declaration) project_url directive is declared twice",
            11: "(Double-Directive-Declaration) credential_name directive is declared twice",
            12: "(Double-Directive-Declaration) root_pom directive is declared twice",
            13: "(Double-Directive-Declaration) goals_options directive is declared twice",
            14: "(Double-Directive-Declaration) post_step directive is declared twice",
            15: "(Bad-directive) goals_options directive is acceptable only if the project is a maven project",
            16: "(Double-Directive-Declaration) project_name directive is declared twice",
            17: "(Missing-Directive-Declaration) project_name directive is not declared",
            18: "(Bad-declaration) specifying credentials without specifying the repository urls are mean"
        }

        self.RuleCode = {
            0: 'RULE_job',
            1: 'RULE_configuration_scopes',
            2: 'RULE_style',
            3: 'RULE_project_name',
            4: 'RULE_project_source_scope',
            5: 'RULE_project_source_op',
            6: 'RULE_build_triggers_scope',
            7: 'RULE_triggers',
            8: 'RULE_poll_scm',
            9: 'RULE_build_after_other_projects',
            10: 'RULE_build_periodically',
            11: 'RULE_pattern',
            12: 'RULE_building_scope',
            13: 'RULE_build_directives',
            14: 'RULE_shell_command',
            15: 'RULE_goals_option',
            16: 'RULE_root_pom',
            17: 'RULE_post_step'

        }
        self.JigBuiltFile =''
        self.JobsDirectory = ''



        self.JobName = None
        self.Style = None
        self.SourceProjectUrl = None
        self.SourceGitRepoUrls = None
        self.SourceGitRepoBranches = None
        self.SourceCredentialName = None

        self.PollScmPatterns = None
        self.PollScmIgnorePostCommitHooks = False
        self.BuildPeriodicallyPatterns=None

        self.BuildRootPomFileName= "pom.xml"
        self.BuildPostStepAction="run_regardless"
        self.BuildShellCommands=None


        # Scope Declaration Status
        self.SourceScope=False
        self.BuildTriggerScope=False
        self.BuildScope=False
        self.PollScmScope=False
        self.BuildPeriodicallyScope=False
        self.BuildAfterOtherProjectsScope=False

        # Directive Declaration Status
        self.BuildRootPomFile=False
        self.BuildGoalsOption=False
        self.BuildPostStep=False

        self.MavenJobBasicStructure='''<?xml version='1.1' encoding='UTF-8'?>
<maven2-moduleset plugin="maven-plugin@3.6">
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>true</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <aggregatorStyleBuild>true</aggregatorStyleBuild>
  <incrementalBuild>false</incrementalBuild>
  <ignoreUpstremChanges>false</ignoreUpstremChanges>
  <ignoreUnsuccessfulUpstreams>false</ignoreUnsuccessfulUpstreams>
  <archivingDisabled>false</archivingDisabled>
  <siteArchivingDisabled>false</siteArchivingDisabled>
  <fingerprintingDisabled>false</fingerprintingDisabled>
  <resolveDependencies>false</resolveDependencies>
  <processPlugins>false</processPlugins>
  <mavenValidationLevel>-1</mavenValidationLevel>
  <runHeadless>false</runHeadless>
  <disableTriggerDownstreamProjects>false</disableTriggerDownstreamProjects>
  <blockTriggerWhenBuilding>true</blockTriggerWhenBuilding>
  <settings class="jenkins.mvn.DefaultSettingsProvider"/>
  <globalSettings class="jenkins.mvn.DefaultGlobalSettingsProvider"/>
  <reporters/>
  <publishers/>
  <buildWrappers/>
  <prebuilders/>
  <postbuilders/>
  <runPostStepsIfResult>
    <name>FAILURE</name>
    <ordinal>2</ordinal>
    <color>RED</color>
    <completeBuild>true</completeBuild>
  </runPostStepsIfResult>
</maven2-moduleset>'''


        self.GeneralSamples = {
            'ProjectUrl': '''<com.coravy.hudson.plugins.github.GithubProjectProperty plugin="github@1.29.5">
              <projectUrl>URL</projectUrl>
              <displayName></displayName>
            </com.coravy.hudson.plugins.github.GithubProjectProperty>''',

            'ShellCommand': '''<hudson.tasks.Shell>
                      <command>*</command>
                    </hudson.tasks.Shell>''',

            'SourceCodeGit': '''
                <scm class="hudson.plugins.git.GitSCM" plugin="git@4.2.0">
                    <configVersion>2</configVersion>
                    <userRemoteConfigs>
                      URL
                    </userRemoteConfigs>
                    <branches>
                      BRANCH
                    </branches>
                    <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
                    <submoduleCfg class="list"/>
                    <extensions/>
                  </scm>
                ''',

            'GitRepositoryUrlEmpty': '''<hudson.plugins.git.UserRemoteConfig/>''',

            'GitRepositoryUrl': '''
                            <hudson.plugins.git.UserRemoteConfig>
                        <url>*</url>CREDENTIAL
                </hudson.plugins.git.UserRemoteConfig>''',

            'GitBranchName': '''
                            <hudson.plugins.git.BranchSpec>
                        <name>*</name>
                      </hudson.plugins.git.BranchSpec>''',

            'GitBranchDefault': '''
                                    <hudson.plugins.git.BranchSpec>
                                <name>*/master</name>
                              </hudson.plugins.git.BranchSpec>''',

            'PollScmTrigger': '''<hudson.triggers.SCMTrigger>TIME
                      <ignorePostCommitHooks>IGNORE</ignorePostCommitHooks>
                    </hudson.triggers.SCMTrigger>''',

            'BuildPeriodicallyTrigger': '''<hudson.triggers.TimerTrigger>TIME
                    </hudson.triggers.TimerTrigger>''',

            'BuildAfterOtherProjects': '''<jenkins.triggers.ReverseBuildTrigger>
                      <spec></spec>
                      <upstreamProjects>PROJECTNAME</upstreamProjects>
                      <threshold>
                        <name>TYPE</name>    
                        <ordinal>ORDINAL</ordinal>
                        <color>COLOR</color>
                        <completeBuild>true</completeBuild>
                      </threshold>
                    </jenkins.triggers.ReverseBuildTrigger>
                ''',
            'root_pom' : '''<rootPOM>pom</rootPOM>''',




        }


        self.FreeJobBasicStructure= '''<?xml version="1.0" encoding="UTF-8"?>
          <project>
          <actions/>
          <description/>
          <keepDependencies>false</keepDependencies>
          <properties/>
          <scm class="jenkins.scm.NullSCM"/>
          <canRoam>true</canRoam>
          <disabled>false</disabled>
          <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
          <triggers/>
          <concurrentBuild>false</concurrentBuild>
          <builders/>
          <publishers/>
          <buildWrappers/>
        </project>'''




    def asking_user_decision(self , displayMessage):
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



    def initialize(self):
        '''
        This function is for initialize   self.JigBuiltFile and self.JobsDirectory
        '''
        fh = open('c:\\users\\{0}\\JC\\controls'.format(getuser()))
        for line in fh:
            if (line.strip()).startswith("jobdir"):
                self.JobsDirectory = ((line).split("=")[1]).strip()
            elif (line.strip()).startswith("built"):
                self.JigBuiltFile = ((line).split("=")[1]).strip()
        fh.close()


    # Enter a parse tree produced by jobParser#job.
    def enterJob(self, ctx:jobParser.JobContext):

        ConfigFileRules=[]
        for i in range(ctx.getChildCount()):
            if (self.RuleCode[ctx.getChild(i).getRuleIndex()]) not in ConfigFileRules:
                ConfigFileRules.append((self.RuleCode[ctx.getChild(i).getRuleIndex()]))
        if 'RULE_project_name' not in ConfigFileRules:
            print(self.Errors[17])
            exit()
        if 'RULE_style' not in ConfigFileRules:
            self.Style='free'




    # Exit a parse tree produced by jobParser#job.
    def exitJob(self, ctx:jobParser.JobContext):
        print("-Parsed successfully\n")
        AskingResult = self.asking_user_decision("Create XML configuration file for job '{0}'?[y/n] ".format(self.JobName))
        if AskingResult:
            '''check file existence '''
            for file in listdir(self.JobsDirectory):
                if file.startswith(self.JobName):

                    print("\nA xml configuration file with name same as '{0}' does exist".format(self.JobName))
                    AskingResult = self.asking_user_decision('Overwrite the existing file ?[y/n] : ')
                    if AskingResult:
                        remove(self.JobsDirectory + file)
                        break
                    else:
                        return

            job_config_xml=''
            if self.Style== 'free':
                job_config_xml = self.FreeJobBasicStructure
            else:
                job_config_xml=self.MavenJobBasicStructure



            '''Setting Source scope'''

            if self.SourceScope:
                GitUrlsXml = str()
                GitBranchXml = str()
                if self.SourceProjectUrl:
                    ProjectUrlXml=self.GeneralSamples['ProjectUrl']
                    ProjectUrlXml=ProjectUrlXml.replace("URL",self.SourceProjectUrl)

                    job_config_xml=job_config_xml.replace("<properties/>","<properties>\n{0}\n</properties>".format(ProjectUrlXml))

                if self.SourceGitRepoUrls:

                    for url in self.SourceGitRepoUrls:
                        GitUrlsXml += self.GeneralSamples['GitRepositoryUrl'].replace("*", url) + "\n"

                    if self.SourceGitRepoBranches:
                        for branch in self.SourceGitRepoBranches:
                            GitBranchXml += self.GeneralSamples['GitBranchName'].replace("*", branch) + "\n"

                    else:
                        GitBranchXml = self.GeneralSamples['GitBranchDefault']


                    if self.SourceCredentialName is not None :

                        GitUrlsXml=GitUrlsXml.replace("CREDENTIAL","\n<credentialsId>{0}</credentialsId>".format(self.SourceCredentialName))
                    else:
                        GitUrlsXml=GitUrlsXml.replace("CREDENTIAL","")

                    #TODO for each repo one credit not implemented (grammar should be changed)


                    SourceCodeXml = self.GeneralSamples['SourceCodeGit']
                    SourceCodeXml = SourceCodeXml.replace("URL", GitUrlsXml)
                    SourceCodeXml = SourceCodeXml.replace("BRANCH", GitBranchXml)

                    if self.Style=='free':
                        job_config_xml = job_config_xml.replace('''<scm class="jenkins.scm.NullSCM"/>''', SourceCodeXml)

                    else:
                        job_config_xml = job_config_xml.replace('''<scm class="hudson.scm.NullSCM"/>''', SourceCodeXml)



            '''Setting build_triggers scope'''
            BuildTriggerFinalResult = str()  ## Because we can have multiple build trigger we should wait until collection of all their xmls

            '''Setting poll_scm scope '''
            if self.PollScmScope:
                PollScmXml = self.GeneralSamples['PollScmTrigger']

                # Ignore the post commit hooks always is presented in the config file
                PollScmIgnoreHooks = 'true' if self.PollScmIgnorePostCommitHooks is True else 'false'
                PollScmXml = PollScmXml.replace('IGNORE', PollScmIgnoreHooks)

                # Patterns can be presented or not presented in the config.xml file
                if self.PollScmPatterns:
                    PollScmPatterns = "\n".join(self.PollScmPatterns)
                    PollScmXml = PollScmXml.replace('TIME', "\n<spec>"+PollScmPatterns+"</spec>")
                else:
                    PollScmXml = PollScmXml.replace('TIME', "")


                PollScmXml += "\n"
                BuildTriggerFinalResult += PollScmXml


            '''Setting build_after_other_projets scope'''
            if self.BuildAfterOtherProjectsScope:
                #TODO This function is not implemented because the usage was not necessary
                pass
                # Ordinal = str()
                # Color = str()
                # Type = str()
                # ProjectName = self.UpstreamProjects[0]
                # if self.TriggerOnlyBuildStable:
                #     Ordinal = '0'
                #     Type = 'SUCCESS'
                #     Color = 'BLUE'
                # elif self.TriggerEvenBuildUnstable:
                #     Ordinal = '1'
                #     Type = 'UNSTABLE'
                #     Color = 'YELLOW'
                # elif self.TriggerEvenBuildFail:
                #     Ordinal = '2'
                #     Type = 'FAILURE'
                #     Color = 'RED'
                #
                # BuildAfterOtherProjectsXml = self.GeneralSamples['BuildAfterOtherProjects']
                # BuildAfterOtherProjectsXml = BuildAfterOtherProjectsXml.replace("PROJECTNAME", ProjectName)
                # BuildAfterOtherProjectsXml = BuildAfterOtherProjectsXml.replace("TYPE", Type)
                # BuildAfterOtherProjectsXml = BuildAfterOtherProjectsXml.replace("ORDINAL", Ordinal)
                # BuildAfterOtherProjectsXml = BuildAfterOtherProjectsXml.replace("COLOR", Color)
                # BuildAfterOtherProjectsXml += "\n"
                # BuildTriggerFinalResult += BuildAfterOtherProjectsXml

            '''Setting build_periodically scope'''
            if self.BuildPeriodicallyScope:
                BuildPeriodicallyXml = self.GeneralSamples['BuildPeriodicallyTrigger']

                if self.BuildPeriodicallyPatterns:
                    patterns = "\n".join(self.BuildPeriodicallyPatterns)
                    BuildPeriodicallyXml = BuildPeriodicallyXml.replace('TIME', "\n<spec>"+patterns+"</spec>")
                    BuildPeriodicallyXml += "\n"
                else:
                    BuildPeriodicallyXml = BuildPeriodicallyXml.replace('TIME',"")
                    BuildPeriodicallyXml += "\n"


                BuildTriggerFinalResult += BuildPeriodicallyXml


            job_config_xml = job_config_xml.replace("<triggers/>",
                                                    "<triggers>\n{0}</triggers>\n".format(BuildTriggerFinalResult))


            '''Setting shell commands'''
            if (self.BuildShellCommands) is not None:
                ShellCommands = '\n'.join(self.BuildShellCommands)


                ShellCommandsXml = (self.GeneralSamples['ShellCommand']).replace("*", ShellCommands)

                if self.Style=='free':
                    job_config_xml = job_config_xml.replace("<builders/>",
                                                        "<builders>\n{0}\n</builders>".format(ShellCommandsXml))

                else:
                    job_config_xml = job_config_xml.replace("<prebuilders/>",
                                                            "<prebuilders>\n{0}\n</prebuilders>".format(ShellCommandsXml))


            '''Setting root_pom file'''
            if self.Style=='maven':
                # root_pom
                if self.BuildRootPomFileName!='pom.xml':
                    RootPomXml=self.GeneralSamples['root_pom']
                    RootPomXml=RootPomXml.replace("pom",self.BuildRootPomFileName)

                    # The reason I substituted with <reporters/> was that I had to
                    # add the rootPOM in the middle of the config file . So I choosed
                    # a directive that will not change by our configurations
                    job_config_xml=job_config_xml.replace("<reporters/>","<reporters/>\n{0}\n".format(RootPomXml))

                '''Setting post-step'''
                if self.BuildPostStep:
                    if self.BuildPostStepAction != 'run_regardless':

                        if self.BuildPostStepAction == 'run_if_build_succeed':
                            job_config_xml=job_config_xml.replace('''<name>FAILURE</name>''','''<name>SUCCESS</name>''')
                            job_config_xml=job_config_xml.replace('''<ordinal>2</ordinal>''','''<ordinal>0</ordinal>''')
                            job_config_xml=job_config_xml.replace('''<color>RED</color>''','''<color>BLUE</color>''')



                        elif self.BuildPostStepAction == 'run_if_build_succeed_unstable':
                            job_config_xml = job_config_xml.replace('''<name>FAILURE</name>''',
                                                                    '''<name>UNSTABLE</name>''')
                            job_config_xml = job_config_xml.replace('''<ordinal>2</ordinal>''',
                                                                    '''<ordinal>1</ordinal>''')
                            job_config_xml = job_config_xml.replace('''<color>RED</color>''',
                                                                    '''<color>YELLOW</color>''')




            '''Setting description'''
            UserDecision=self.asking_user_decision("\nDo you want to add a description for this job?[y/n] ")
            if UserDecision:
                JobDescription=input()
                job_config_xml = job_config_xml.replace("<description/>","<description>{0}</description>".format(JobDescription))


            fhandle = open(self.JobsDirectory + self.JobName + '.config.xml', 'w')
            fhandle.write(job_config_xml)
            print("\nFile '{0}.config.xml' created successfully".format(self.JobName))

            config_file_creation_timestamp=datetime.now()
            fhandle.close()

            update_built_file(self.JigBuiltFile,'update-local-create-date', JobName=self.JobName,
                              LocalCreationDate=config_file_creation_timestamp)

            end = input()

        else:
            return

    # Enter a parse tree produced by jobParser#configuration_scopes.
    def enterConfiguration_scopes(self, ctx:jobParser.Configuration_scopesContext):
        pass

    # Exit a parse tree produced by jobParser#configuration_scopes.
    def exitConfiguration_scopes(self, ctx:jobParser.Configuration_scopesContext):
        pass


    # Enter a parse tree produced by jobParser#style.
    def enterStyle(self, ctx:jobParser.StyleContext):

        pass

    # Exit a parse tree produced by jobParser#style.
    def exitStyle(self, ctx:jobParser.StyleContext):
        self.Style=(ctx.getChild(1).getText())


    # Enter a parse tree produced by jobParser#project_name.
    def enterProject_name(self, ctx:jobParser.Project_nameContext):
        if self.JobName:
            print(self.Errors[16])
            exit()



    # Exit a parse tree produced by jobParser#project_name.
    def exitProject_name(self, ctx:jobParser.Project_nameContext):
        job_name = ' '
        for e in ctx.Identifier():
            job_name += e.getText() + ' '

        # replace method is for deleting single quotes if the user specified them
        self.JobName = (job_name.strip()).replace("'", "")



    # Enter a parse tree produced by jobParser#project_source_scope.
    def enterProject_source_scope(self, ctx:jobParser.Project_source_scopeContext):
        if self.SourceScope :
            print(self.Errors[4])
            exit()
        else:
            self.SourceScope=True


    # Exit a parse tree produced by jobParser#project_source_scope.
    def exitProject_source_scope(self, ctx:jobParser.Project_source_scopeContext):
        pass


    # Enter a parse tree produced by jobParser#project_source_op.
    def enterProject_source_op(self, ctx:jobParser.Project_source_opContext):
        pass

    # Exit a parse tree produced by jobParser#project_source_op.
    def exitProject_source_op(self, ctx:jobParser.Project_source_opContext):
        project_source_op = ctx.getChild(0).getText()

        if project_source_op == 'project_url':
            if self.SourceProjectUrl is not None:
                print(self.Errors[10])
                exit()
            self.SourceProjectUrl = ctx.getChild(1).getText()


        elif project_source_op == 'git_repo_urls':

            # This check is for when we want to append urls to previously
            # added urls
            if self.SourceGitRepoUrls is None:
                self.SourceGitRepoUrls = []

            for i in range(1, ctx.getChildCount()):
                self.SourceGitRepoUrls.append(ctx.getChild(i).getText())


        elif project_source_op == 'git_repo_branches':
            # If the user doesn't specify the repository urls but the branches
            # we should stop the process
            if self.SourceGitRepoUrls is None:
                print(self.Errors[1])
                exit()

            # This check is for when we want to append branches to previously
            # added branches
            if self.SourceGitRepoBranches is None:
                self.SourceGitRepoBranches = []

            for i in range(1, ctx.getChildCount()):
                self.SourceGitRepoBranches.append(ctx.getChild(i).getText())


        elif project_source_op == 'credential_name':
            # If the user doesn't specify the repository urls but the credential
            # we should stop the process
            if self.SourceGitRepoUrls is None:
                print(self.Errors[18])
                exit()

            if self.SourceCredentialName is not None:
                print(self.Errors[11])
                exit()
            credential_name = ' '
            for e in ctx.Identifier():
                credential_name += e.getText() + ' '

            self.SourceCredentialName = (credential_name.strip()).replace("'", '')



    # Enter a parse tree produced by jobParser#build_triggers_scope.
    def enterBuild_triggers_scope(self, ctx:jobParser.Build_triggers_scopeContext):
        if self.BuildTriggerScope:
            print(self.Errors[5])
            exit()
        else:
            self.BuildTriggerScope=True
        pass

    # Exit a parse tree produced by jobParser#build_triggers_scope.
    def exitBuild_triggers_scope(self, ctx:jobParser.Build_triggers_scopeContext):
        pass


    # Enter a parse tree produced by jobParser#triggers.
    def enterTriggers(self, ctx:jobParser.TriggersContext):
        pass

    # Exit a parse tree produced by jobParser#triggers.
    def exitTriggers(self, ctx:jobParser.TriggersContext):
        pass


    # Enter a parse tree produced by jobParser#poll_scm.
    def enterPoll_scm(self, ctx:jobParser.Poll_scmContext):
        if self.PollScmScope:
            print(self.Errors[7])
            exit()
        else:
            self.PollScmScope=True
        pass

    # Exit a parse tree produced by jobParser#poll_scm.
    def exitPoll_scm(self, ctx:jobParser.Poll_scmContext):
        if ctx.getChildCount() == 3:  # poll_scm method skipped even it is declared
            pass
        else:
            for i in range(ctx.getChildCount()):
                if ctx.getChild(i).getText() == 'ignore_post_commit_hooks':
                    self.PollScmIgnorePostCommitHooks = True if ctx.getChild(i + 1).getText() == 'yes' else False


    # Enter a parse tree produced by jobParser#build_after_other_projects.
    def enterBuild_after_other_projects(self, ctx:jobParser.Build_after_other_projectsContext):
        if self.BuildAfterOtherProjectsScope:
            print(self.Errors[9])
            exit()
        else:
            self.BuildAfterOtherProjectsScope=True


    # Exit a parse tree produced by jobParser#build_after_other_projects.
    def exitBuild_after_other_projects(self, ctx:jobParser.Build_after_other_projectsContext):
        if ctx.getChildCount() == 3: # build_after_other_projects method skipped even it is declared
            pass
        else:

            if (ctx.DIGIT().getText()) not in  '1 2 3':
                print(self.Errors[2])
                exit()

            project_names=[]


            for e in ctx.Identifier():

                if "'" in e.getText():
                    if len(project_names)==0 or ("'" not in project_names[-1]):
                        project_names.append(e.getText() if (e.getText()).count("'")==1 else (e.getText()).replace("'","") )
                    else:
                        first_part=project_names.pop()
                        project_names.append((first_part+" " + e.getText()).replace("'",""))
                else:
                    project_names.append(e.getText())

        #TODO This function is not implemented yet beacuase the usage is not necessary yet



    # Enter a parse tree produced by jobParser#build_priodically.
    def enterBuild_priodically(self, ctx:jobParser.Build_priodicallyContext):
        if self.BuildPeriodicallyScope:
            print(self.Errors[8])
            exit()
        else:
            self.BuildPeriodicallyScope=True


    # Exit a parse tree produced by jobParser#build_priodically.
    def exitBuild_priodically(self, ctx:jobParser.Build_priodicallyContext):
        pass


    # Enter a parse tree produced by jobParser#pattern.
    def enterPattern(self, ctx:jobParser.PatternContext):
        pass

    # Exit a parse tree produced by jobParser#pattern.
    def exitPattern(self, ctx:jobParser.PatternContext):

        if self.RuleCode[ctx.parentCtx.getRuleIndex()] == 'RULE_poll_scm':
            # Declaring multiple -p should be appended to previous patterns
            # but we have to check this is the first -p or not.
            # If it is the first PollScmPatterns is None else is not None
            if self.PollScmPatterns is None:
                self.PollScmPatterns = []

            pattern_str = ' '
            for i in range(1, ctx.getChildCount()):
                pattern_str += (ctx.getChild(i).getText()) + " "

            self.PollScmPatterns.append(pattern_str.strip())

        elif self.RuleCode[ctx.parentCtx.getRuleIndex()] == 'RULE_build_periodically':
            # Declaring multiple -p should be appended to previous patterns
            # but we have to check this is the first -p or not.
            # If it is the first BuildPeriodicallyPatterns is None else is not None
            if self.BuildPeriodicallyPatterns is None:
                self.BuildPeriodicallyPatterns = []
            pattern_str = ' '
            for i in range(1, ctx.getChildCount()):
                pattern_str += (ctx.getChild(i).getText()) + " "
            self.BuildPeriodicallyPatterns.append(pattern_str.strip())




    # Enter a parse tree produced by jobParser#building_scope.
    def enterBuilding_scope(self, ctx:jobParser.Building_scopeContext):
        if self.BuildScope:
            print(self.Errors[6])
            exit()
        else:
            self.BuildScope=True


    # Exit a parse tree produced by jobParser#building_scope.
    def exitBuilding_scope(self, ctx:jobParser.Building_scopeContext):
        pass


    # Enter a parse tree produced by jobParser#build_directives.
    def enterBuild_directives(self, ctx:jobParser.Build_directivesContext):
        pass

    # Exit a parse tree produced by jobParser#build_directives.
    def exitBuild_directives(self, ctx:jobParser.Build_directivesContext):
        pass


    # Enter a parse tree produced by jobParser#shell_command.
    def enterShell_command(self, ctx:jobParser.Shell_commandContext):
        pass

    # Exit a parse tree produced by jobParser#shell_command.
    def exitShell_command(self, ctx:jobParser.Shell_commandContext):

        '''
        The concept of path in shell command is considered very simple without space
        '''
        if self.BuildShellCommands is None:
            self.BuildShellCommands=[]

        command=''
        for e in ctx.Identifier():
            command+=e.getText() + " "
        self.BuildShellCommands.append(command)


    # Enter a parse tree produced by jobParser#goals_option.
    def enterGoals_option(self, ctx:jobParser.Goals_optionContext):
        if self.Style == "free":
            print(self.Errors[15])
            exit()
        if self.BuildGoalsOption:
            print(self.Errors[13])
            exit()
        self.BuildGoalsOption=True


    # Exit a parse tree produced by jobParser#goals_option.
    def exitGoals_option(self, ctx:jobParser.Goals_optionContext):
        #TODO this function is not implemented because the usage was unnecessary
        pass


    # Enter a parse tree produced by jobParser#root_pom.
    def enterRoot_pom(self, ctx:jobParser.Root_pomContext):
        if self.Style == "free":
            print(self.Errors[3])
            exit()
        if self.BuildRootPomFile:
            print(self.Errors[12])
            exit()
        self.BuildRootPomFile=True

    # Exit a parse tree produced by jobParser#root_pom.
    def exitRoot_pom(self, ctx:jobParser.Root_pomContext):
        pom_file_name = ''
        for e in ctx.Identifier():
            pom_file_name += e.getText() + ' '

        # replace method is for deleting single quotes if the user specified them
        self.BuildRootPomFileName = (pom_file_name.strip()).replace("'", "")


    # Enter a parse tree produced by jobParser#post_step.
    def enterPost_step(self, ctx:jobParser.Post_stepContext):
        if self.Style == "free":
            print(self.Errors[3])
            exit()
        if self.BuildPostStep:
            print(self.Errors[14])
            exit()
        self.BuildPostStep=True

    # Exit a parse tree produced by jobParser#post_step.
    def exitPost_step(self, ctx:jobParser.Post_stepContext):
        self.BuildPostStepAction=(ctx.getChild(1).getText())



del jobParser
