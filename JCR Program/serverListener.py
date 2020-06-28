# Generated from server.g4 by ANTLR 4.8
from antlr4 import *
import re
if __name__ is not None and "." in __name__:
    from .serverParser import serverParser
else:
    from serverParser import serverParser

# This class defines a complete listener for a parse tree produced by serverParser.
class serverListener(ParseTreeListener):

    def __init__(self):
        self.ServerAddress = None
        self.ServerPort = None

        self.IpRegex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
    			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
    			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
    			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

        self.RuleCode = {
            0: 'RULE_serverconf',
            1: 'RULE_addressrule',
            2: 'RULE_portrule'
        }
        self.Errors = {
            0: "(Missed-Directive) 'address' directive is missing in server.conf file",
            1: "(Multi-directive-declaration) 'address' directive is declared multiple times",
            2: "(Multi-directive-declaration) 'port' directive is declared multiple times",
            3: "(Bad-IP-address) IP address '*' is not a valid IP address",
            4: "(Bad-Port-number) Port number '*' is not a valid Port number(0-65535)"
        }

    def return_socket_info(self):
        return self.ServerAddress,self.ServerPort

    # Enter a parse tree produced by serverParser#serverconf.
    def enterServerconf(self, ctx:serverParser.ServerconfContext):
        ConfFileRules = []
        for i in range(ctx.getChildCount()):
            ConfFileRules.append(self.RuleCode[ctx.getChild(i).getRuleIndex()])

        if ConfFileRules.count("RULE_addressrule") == 0:
            raise Exception(self.Errors[0])

        elif ConfFileRules.count("RULE_addressrule") > 1:
            raise Exception(self.Errors[1])

        if ConfFileRules.count("RULE_portrule") == 0:
            self.ServerPort = '80'

        elif ConfFileRules.count("RULE_portrule") > 1:
            raise Exception(self.Errors[2])

    # Exit a parse tree produced by serverParser#serverconf.
    def exitServerconf(self, ctx:serverParser.ServerconfContext):
        pass


    # Enter a parse tree produced by serverParser#addressrule.
    def enterAddressrule(self, ctx:serverParser.AddressruleContext):
        pass

    # Exit a parse tree produced by serverParser#addressrule.
    def exitAddressrule(self, ctx:serverParser.AddressruleContext):
        # Below condition is because if you do not specify value for the address directive
        # it throws an exception no getText() function and parser does not handle it :((
        # TODO not a good method for handling above problem

        if ctx.getChildCount() == 2:
            IpAddress = ctx.DirectiveValue(0).getText()

            if re.search(self.IpRegex, IpAddress):
                self.ServerAddress = IpAddress
            else:
                raise Exception(self.Errors[3].replace("*", IpAddress))




    # Enter a parse tree produced by serverParser#portrule.
    def enterPortrule(self, ctx:serverParser.PortruleContext):
        pass

    # Exit a parse tree produced by serverParser#portrule.
    def exitPortrule(self, ctx:serverParser.PortruleContext):
        # Below condition is because if you do not specify value for the address directive
        # it throws an exception no getText() function and parser does not handle it :((
        # TODO not a good method for handling above problem

        if ctx.getChildCount() == 2:
            PortNum = ctx.DirectiveValue(0).getText()
            if int(PortNum) not in range(0, 65536):
                raise Exception(self.Errors[4].replace("*", PortNum))
            else:
                self.ServerPort = PortNum



del serverParser