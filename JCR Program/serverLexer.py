# Generated from server.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\5\6\61\n\6\3\6\6\6\64\n\6\r\6")
        buf.write("\16\6\65\3\6\5\69\n\6\3\7\3\7\7\7=\n\7\f\7\16\7@\13\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\7\bH\n\b\f\b\16\bK\13\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\6\tS\n\t\r\t\16\tT\3\t\3\t\3\n\3\n")
        buf.write("\3I\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2")
        buf.write("\5\4\2\60\60\62;\3\2\f\f\5\2\13\f\17\17\"\"\2_\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3")
        buf.write("\25\3\2\2\2\5\35\3\2\2\2\7%\3\2\2\2\t*\3\2\2\2\13\60\3")
        buf.write("\2\2\2\r:\3\2\2\2\17C\3\2\2\2\21R\3\2\2\2\23X\3\2\2\2")
        buf.write("\25\26\7C\2\2\26\27\7f\2\2\27\30\7f\2\2\30\31\7t\2\2\31")
        buf.write("\32\7g\2\2\32\33\7u\2\2\33\34\7u\2\2\34\4\3\2\2\2\35\36")
        buf.write("\7c\2\2\36\37\7f\2\2\37 \7f\2\2 !\7t\2\2!\"\7g\2\2\"#")
        buf.write("\7u\2\2#$\7u\2\2$\6\3\2\2\2%&\7R\2\2&\'\7q\2\2\'(\7t\2")
        buf.write("\2()\7v\2\2)\b\3\2\2\2*+\7r\2\2+,\7q\2\2,-\7t\2\2-.\7")
        buf.write("v\2\2.\n\3\2\2\2/\61\7)\2\2\60/\3\2\2\2\60\61\3\2\2\2")
        buf.write("\61\63\3\2\2\2\62\64\t\2\2\2\63\62\3\2\2\2\64\65\3\2\2")
        buf.write("\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\679\7)\2\2")
        buf.write("8\67\3\2\2\289\3\2\2\29\f\3\2\2\2:>\7%\2\2;=\n\3\2\2<")
        buf.write(";\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3")
        buf.write("\2\2\2AB\b\7\2\2B\16\3\2\2\2CD\7\61\2\2DE\7,\2\2EI\3\2")
        buf.write("\2\2FH\13\2\2\2GF\3\2\2\2HK\3\2\2\2IJ\3\2\2\2IG\3\2\2")
        buf.write("\2JL\3\2\2\2KI\3\2\2\2LM\7,\2\2MN\7\61\2\2NO\3\2\2\2O")
        buf.write("P\b\b\3\2P\20\3\2\2\2QS\t\4\2\2RQ\3\2\2\2ST\3\2\2\2TR")
        buf.write("\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\b\t\3\2W\22\3\2\2\2XY\13")
        buf.write("\2\2\2Y\24\3\2\2\2\n\2\60\63\658>IT\4\2\3\2\b\2\2")
        return buf.getvalue()


class serverLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    DirectiveValue = 5
    COMMENT = 6
    BlockComment = 7
    WS = 8
    ERROR = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Address'", "'address'", "'Port'", "'port'" ]

    symbolicNames = [ "<INVALID>",
            "DirectiveValue", "COMMENT", "BlockComment", "WS", "ERROR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "DirectiveValue", "COMMENT", 
                  "BlockComment", "WS", "ERROR" ]

    grammarFileName = "server.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


