# Generated from server.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\34\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\7\2\13\n\2\f\2\16")
        buf.write("\2\16\13\2\3\3\3\3\6\3\22\n\3\r\3\16\3\23\3\4\3\4\6\4")
        buf.write("\30\n\4\r\4\16\4\31\3\4\2\2\5\2\4\6\2\4\3\2\3\4\3\2\5")
        buf.write("\6\2\34\2\f\3\2\2\2\4\17\3\2\2\2\6\25\3\2\2\2\b\13\5\4")
        buf.write("\3\2\t\13\5\6\4\2\n\b\3\2\2\2\n\t\3\2\2\2\13\16\3\2\2")
        buf.write("\2\f\n\3\2\2\2\f\r\3\2\2\2\r\3\3\2\2\2\16\f\3\2\2\2\17")
        buf.write("\21\t\2\2\2\20\22\7\7\2\2\21\20\3\2\2\2\22\23\3\2\2\2")
        buf.write("\23\21\3\2\2\2\23\24\3\2\2\2\24\5\3\2\2\2\25\27\t\3\2")
        buf.write("\2\26\30\7\7\2\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2")
        buf.write("\2\2\31\32\3\2\2\2\32\7\3\2\2\2\6\n\f\23\31")
        return buf.getvalue()


class serverParser ( Parser ):

    grammarFileName = "server.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Address'", "'address'", "'Port'", "'port'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DirectiveValue", "COMMENT", "BlockComment", 
                      "WS", "ERROR" ]

    RULE_serverconf = 0
    RULE_addressrule = 1
    RULE_portrule = 2

    ruleNames =  [ "serverconf", "addressrule", "portrule" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    DirectiveValue=5
    COMMENT=6
    BlockComment=7
    WS=8
    ERROR=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ServerconfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addressrule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(serverParser.AddressruleContext)
            else:
                return self.getTypedRuleContext(serverParser.AddressruleContext,i)


        def portrule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(serverParser.PortruleContext)
            else:
                return self.getTypedRuleContext(serverParser.PortruleContext,i)


        def getRuleIndex(self):
            return serverParser.RULE_serverconf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServerconf" ):
                listener.enterServerconf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServerconf" ):
                listener.exitServerconf(self)




    def serverconf(self):

        localctx = serverParser.ServerconfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_serverconf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << serverParser.T__0) | (1 << serverParser.T__1) | (1 << serverParser.T__2) | (1 << serverParser.T__3))) != 0):
                self.state = 8
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [serverParser.T__0, serverParser.T__1]:
                    self.state = 6
                    self.addressrule()
                    pass
                elif token in [serverParser.T__2, serverParser.T__3]:
                    self.state = 7
                    self.portrule()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:

            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)

        finally:
            self.exitRule()
        return localctx


    class AddressruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DirectiveValue(self, i:int=None):
            if i is None:
                return self.getTokens(serverParser.DirectiveValue)
            else:
                return self.getToken(serverParser.DirectiveValue, i)

        def getRuleIndex(self):
            return serverParser.RULE_addressrule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddressrule" ):
                listener.enterAddressrule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddressrule" ):
                listener.exitAddressrule(self)




    def addressrule(self):

        localctx = serverParser.AddressruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_addressrule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            _la = self._input.LA(1)
            if not(_la==serverParser.T__0 or _la==serverParser.T__1):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.match(serverParser.DirectiveValue)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==serverParser.DirectiveValue):
                    break

        except RecognitionException as re:

            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)

        finally:
            self.exitRule()
        return localctx


    class PortruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DirectiveValue(self, i:int=None):
            if i is None:
                return self.getTokens(serverParser.DirectiveValue)
            else:
                return self.getToken(serverParser.DirectiveValue, i)

        def getRuleIndex(self):
            return serverParser.RULE_portrule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPortrule" ):
                listener.enterPortrule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPortrule" ):
                listener.exitPortrule(self)




    def portrule(self):

        localctx = serverParser.PortruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_portrule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            _la = self._input.LA(1)
            if not(_la==serverParser.T__2 or _la==serverParser.T__3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.match(serverParser.DirectiveValue)
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==serverParser.DirectiveValue):
                    break

        except RecognitionException as re:

            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





