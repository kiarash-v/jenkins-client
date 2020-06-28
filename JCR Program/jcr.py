from antlr4 import *
from jobLexer import jobLexer
from jobParser import jobParser
from jobListener import jobListener
from serverLexer import serverLexer
from serverParser import serverParser
from serverListener import serverListener
from getpass import getuser
from os import path


print("--------")
print("jcr v0.3")
print("--------")

locationsFilePath='c:\\users\\{0}\\JC\\controls'.format(getuser())

if not path.exists(locationsFilePath):
    print("-directory {0} is not set up properly".format('c:\\users\\{0}\\JC'.format(getuser())))
    print("-please use configure.exe to reconfigure everything properly")
    exit()
else:
    JobConfFilePath=''
    ServerConfFilePath=''




    fh=open('c:\\users\\{0}\\JC\\controls'.format(getuser()))
    for line in fh:
        if (line.strip()).startswith("job.conf"):
            JobConfFilePath=((line).split("=")[1]).strip()
        elif (line.strip()).startswith("server.conf"):
            ServerConfFilePath=((line).split("=")[1]).strip()

    fh.close()

    '''testing server.conf'''
    try:
        print("\n#### server.conf ####")
        input_stream = FileStream(ServerConfFilePath)
        lexer = serverLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = serverParser(stream)

        tree = parser.serverconf()


        printer = serverListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

        addr, port= printer.return_socket_info()
        fh = open('c:\\users\\{0}\\JC\\controls'.format(getuser()),'a')
        fh.write("address={0}\n".format(addr))
        fh.write("port={0}\n".format(port))
        fh.close()

        print("-Parsed successfully\n")


    except Exception as e:
        fh = open('c:\\users\\{0}\\JC\\controls'.format(getuser()), 'a')
        fh.write("address=none\n")
        fh.write("port=none\n")
        fh.close()
        print(e.args[0])
        end=input()
        exit()

    '''testing job.conf'''
    try:
        print("\n#### job.conf ####")

        input_stream = FileStream(JobConfFilePath)
        lexer = jobLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = jobParser(stream)
        tree = parser.job()



        printer = jobListener()
        printer.initialize()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

    except Exception as e:
        print(e.args[0])
        end=input()
        exit()












