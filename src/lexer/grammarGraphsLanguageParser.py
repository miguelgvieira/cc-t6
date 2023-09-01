# Generated from grammarGraphsLanguage.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,254,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,5,0,67,
        8,0,10,0,12,0,70,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,5,4,94,8,4,10,4,
        12,4,97,9,4,1,5,1,5,3,5,101,8,5,1,6,1,6,3,6,105,8,6,1,7,1,7,1,7,
        1,7,5,7,111,8,7,10,7,12,7,114,9,7,1,7,1,7,1,8,1,8,3,8,120,8,8,1,
        9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,132,8,11,10,11,
        12,11,135,9,11,1,11,1,11,1,12,1,12,3,12,141,8,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,166,8,16,1,17,1,17,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,3,21,195,
        8,21,1,22,1,22,3,22,199,8,22,1,23,1,23,3,23,203,8,23,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,
        28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,0,0,32,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,0,2,1,0,11,13,1,0,23,24,242,0,68,1,0,0,0,2,79,1,0,0,0,4,
        81,1,0,0,0,6,84,1,0,0,0,8,95,1,0,0,0,10,100,1,0,0,0,12,104,1,0,0,
        0,14,106,1,0,0,0,16,119,1,0,0,0,18,121,1,0,0,0,20,123,1,0,0,0,22,
        127,1,0,0,0,24,140,1,0,0,0,26,142,1,0,0,0,28,148,1,0,0,0,30,156,
        1,0,0,0,32,165,1,0,0,0,34,167,1,0,0,0,36,173,1,0,0,0,38,179,1,0,
        0,0,40,185,1,0,0,0,42,194,1,0,0,0,44,198,1,0,0,0,46,202,1,0,0,0,
        48,204,1,0,0,0,50,211,1,0,0,0,52,220,1,0,0,0,54,225,1,0,0,0,56,230,
        1,0,0,0,58,235,1,0,0,0,60,243,1,0,0,0,62,251,1,0,0,0,64,67,3,2,1,
        0,65,67,3,32,16,0,66,64,1,0,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,
        1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,0,0,1,
        72,1,1,0,0,0,73,74,3,4,2,0,74,75,5,1,0,0,75,80,1,0,0,0,76,77,3,6,
        3,0,77,78,5,1,0,0,78,80,1,0,0,0,79,73,1,0,0,0,79,76,1,0,0,0,80,3,
        1,0,0,0,81,82,5,2,0,0,82,83,5,25,0,0,83,5,1,0,0,0,84,85,5,2,0,0,
        85,86,5,25,0,0,86,87,5,3,0,0,87,88,5,4,0,0,88,89,3,8,4,0,89,90,5,
        5,0,0,90,7,1,0,0,0,91,94,3,14,7,0,92,94,3,22,11,0,93,91,1,0,0,0,
        93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,9,1,0,
        0,0,97,95,1,0,0,0,98,101,3,16,8,0,99,101,3,24,12,0,100,98,1,0,0,
        0,100,99,1,0,0,0,101,11,1,0,0,0,102,105,3,18,9,0,103,105,3,26,13,
        0,104,102,1,0,0,0,104,103,1,0,0,0,105,13,1,0,0,0,106,107,5,6,0,0,
        107,112,3,16,8,0,108,109,5,7,0,0,109,111,3,16,8,0,110,108,1,0,0,
        0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,
        0,114,112,1,0,0,0,115,116,5,1,0,0,116,15,1,0,0,0,117,120,3,20,10,
        0,118,120,3,18,9,0,119,117,1,0,0,0,119,118,1,0,0,0,120,17,1,0,0,
        0,121,122,5,25,0,0,122,19,1,0,0,0,123,124,5,25,0,0,124,125,5,3,0,
        0,125,126,3,62,31,0,126,21,1,0,0,0,127,128,5,8,0,0,128,133,3,24,
        12,0,129,130,5,7,0,0,130,132,3,24,12,0,131,129,1,0,0,0,132,135,1,
        0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,
        0,0,0,136,137,5,1,0,0,137,23,1,0,0,0,138,141,3,26,13,0,139,141,3,
        28,14,0,140,138,1,0,0,0,140,139,1,0,0,0,141,25,1,0,0,0,142,143,5,
        9,0,0,143,144,5,25,0,0,144,145,3,30,15,0,145,146,5,25,0,0,146,147,
        5,10,0,0,147,27,1,0,0,0,148,149,5,9,0,0,149,150,5,25,0,0,150,151,
        3,30,15,0,151,152,5,25,0,0,152,153,5,7,0,0,153,154,3,62,31,0,154,
        155,5,10,0,0,155,29,1,0,0,0,156,157,7,0,0,0,157,31,1,0,0,0,158,166,
        3,34,17,0,159,166,3,38,19,0,160,166,3,42,21,0,161,166,3,44,22,0,
        162,166,3,36,18,0,163,166,3,40,20,0,164,166,3,46,23,0,165,158,1,
        0,0,0,165,159,1,0,0,0,165,160,1,0,0,0,165,161,1,0,0,0,165,162,1,
        0,0,0,165,163,1,0,0,0,165,164,1,0,0,0,166,33,1,0,0,0,167,168,5,25,
        0,0,168,169,5,14,0,0,169,170,3,16,8,0,170,171,5,10,0,0,171,172,5,
        1,0,0,172,35,1,0,0,0,173,174,5,25,0,0,174,175,5,15,0,0,175,176,3,
        18,9,0,176,177,5,10,0,0,177,178,5,1,0,0,178,37,1,0,0,0,179,180,5,
        25,0,0,180,181,5,16,0,0,181,182,3,24,12,0,182,183,5,10,0,0,183,184,
        5,1,0,0,184,39,1,0,0,0,185,186,5,25,0,0,186,187,5,17,0,0,187,188,
        3,26,13,0,188,189,5,10,0,0,189,190,5,1,0,0,190,41,1,0,0,0,191,195,
        3,48,24,0,192,195,3,50,25,0,193,195,3,52,26,0,194,191,1,0,0,0,194,
        192,1,0,0,0,194,193,1,0,0,0,195,43,1,0,0,0,196,199,3,54,27,0,197,
        199,3,56,28,0,198,196,1,0,0,0,198,197,1,0,0,0,199,45,1,0,0,0,200,
        203,3,58,29,0,201,203,3,60,30,0,202,200,1,0,0,0,202,201,1,0,0,0,
        203,47,1,0,0,0,204,205,5,25,0,0,205,206,5,18,0,0,206,207,3,12,6,
        0,207,208,5,3,0,0,208,209,3,62,31,0,209,210,5,1,0,0,210,49,1,0,0,
        0,211,212,5,25,0,0,212,213,5,18,0,0,213,214,3,18,9,0,214,215,3,30,
        15,0,215,216,5,25,0,0,216,217,5,18,0,0,217,218,3,18,9,0,218,219,
        5,1,0,0,219,51,1,0,0,0,220,221,5,25,0,0,221,222,5,3,0,0,222,223,
        5,25,0,0,223,224,5,1,0,0,224,53,1,0,0,0,225,226,5,19,0,0,226,227,
        5,25,0,0,227,228,5,10,0,0,228,229,5,1,0,0,229,55,1,0,0,0,230,231,
        5,20,0,0,231,232,5,25,0,0,232,233,5,10,0,0,233,234,5,1,0,0,234,57,
        1,0,0,0,235,236,5,25,0,0,236,237,5,21,0,0,237,238,5,25,0,0,238,239,
        5,7,0,0,239,240,5,25,0,0,240,241,5,10,0,0,241,242,5,1,0,0,242,59,
        1,0,0,0,243,244,5,25,0,0,244,245,5,22,0,0,245,246,5,25,0,0,246,247,
        5,7,0,0,247,248,5,25,0,0,248,249,5,10,0,0,249,250,5,1,0,0,250,61,
        1,0,0,0,251,252,7,1,0,0,252,63,1,0,0,0,15,66,68,79,93,95,100,104,
        112,119,133,140,165,194,198,202
    ]

class grammarGraphsLanguageParser ( Parser ):

    grammarFileName = "grammarGraphsLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'grafo'", "'='", "'{'", "'}'", 
                     "'vertice'", "','", "'aresta'", "'('", "')'", "'>'", 
                     "'<'", "'<>'", "'.adiciona_vertice('", "'.remove_vertice('", 
                     "'.adiciona_aresta('", "'.remove_aresta('", "'.'", 
                     "'imprime_estrutura('", "'imprime_grafo('", "'.caminho_mais_curto('", 
                     "'.imprime_caminho_mais_curto('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM_INT", 
                      "NUM_REAL", "IDENT", "CADEIA", "ESC_SEQ", "COMENTARIO", 
                      "WS" ]

    RULE_programa = 0
    RULE_declaracao_grafo = 1
    RULE_declaracao_simples = 2
    RULE_declaracao_complexa = 3
    RULE_grafo_info = 4
    RULE_vertice_ou_aresta = 5
    RULE_vertice_ou_aresta_simples = 6
    RULE_declaracao_vertice = 7
    RULE_vertice = 8
    RULE_vertice_sem_peso = 9
    RULE_vertice_com_peso = 10
    RULE_declaracao_aresta = 11
    RULE_aresta = 12
    RULE_aresta_declaracao_simples = 13
    RULE_aresta_declaracao_complexa = 14
    RULE_direcao = 15
    RULE_cmd = 16
    RULE_cmd_add_vertice = 17
    RULE_cmd_remove_vertice = 18
    RULE_cmd_add_aresta = 19
    RULE_cmd_remove_aresta = 20
    RULE_cmd_atribuicao = 21
    RULE_cmd_imprime = 22
    RULE_cmd_outros = 23
    RULE_atribuicao_peso = 24
    RULE_atribuicao_criacao_aresta = 25
    RULE_atribuicao_grafo = 26
    RULE_imprime_estrutura = 27
    RULE_imprime_grafo = 28
    RULE_caminho_mais_curto = 29
    RULE_imprime_caminho_mais_curto = 30
    RULE_valor = 31

    ruleNames =  [ "programa", "declaracao_grafo", "declaracao_simples", 
                   "declaracao_complexa", "grafo_info", "vertice_ou_aresta", 
                   "vertice_ou_aresta_simples", "declaracao_vertice", "vertice", 
                   "vertice_sem_peso", "vertice_com_peso", "declaracao_aresta", 
                   "aresta", "aresta_declaracao_simples", "aresta_declaracao_complexa", 
                   "direcao", "cmd", "cmd_add_vertice", "cmd_remove_vertice", 
                   "cmd_add_aresta", "cmd_remove_aresta", "cmd_atribuicao", 
                   "cmd_imprime", "cmd_outros", "atribuicao_peso", "atribuicao_criacao_aresta", 
                   "atribuicao_grafo", "imprime_estrutura", "imprime_grafo", 
                   "caminho_mais_curto", "imprime_caminho_mais_curto", "valor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    NUM_INT=23
    NUM_REAL=24
    IDENT=25
    CADEIA=26
    ESC_SEQ=27
    COMENTARIO=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(grammarGraphsLanguageParser.EOF, 0)

        def declaracao_grafo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGraphsLanguageParser.Declaracao_grafoContext)
            else:
                return self.getTypedRuleContext(grammarGraphsLanguageParser.Declaracao_grafoContext,i)


        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGraphsLanguageParser.CmdContext)
            else:
                return self.getTypedRuleContext(grammarGraphsLanguageParser.CmdContext,i)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = grammarGraphsLanguageParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35127300) != 0):
                self.state = 66
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 64
                    self.declaracao_grafo()
                    pass
                elif token in [19, 20, 25]:
                    self.state = 65
                    self.cmd()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(grammarGraphsLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_grafoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_simples(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Declaracao_simplesContext,0)


        def declaracao_complexa(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Declaracao_complexaContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_declaracao_grafo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_grafo" ):
                listener.enterDeclaracao_grafo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_grafo" ):
                listener.exitDeclaracao_grafo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_grafo" ):
                return visitor.visitDeclaracao_grafo(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_grafo(self):

        localctx = grammarGraphsLanguageParser.Declaracao_grafoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao_grafo)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.declaracao_simples()
                self.state = 74
                self.match(grammarGraphsLanguageParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.declaracao_complexa()
                self.state = 77
                self.match(grammarGraphsLanguageParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_simplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_declaracao_simples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_simples" ):
                listener.enterDeclaracao_simples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_simples" ):
                listener.exitDeclaracao_simples(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_simples" ):
                return visitor.visitDeclaracao_simples(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_simples(self):

        localctx = grammarGraphsLanguageParser.Declaracao_simplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao_simples)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(grammarGraphsLanguageParser.T__1)
            self.state = 82
            self.match(grammarGraphsLanguageParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_complexaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def grafo_info(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Grafo_infoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_declaracao_complexa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_complexa" ):
                listener.enterDeclaracao_complexa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_complexa" ):
                listener.exitDeclaracao_complexa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_complexa" ):
                return visitor.visitDeclaracao_complexa(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_complexa(self):

        localctx = grammarGraphsLanguageParser.Declaracao_complexaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao_complexa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(grammarGraphsLanguageParser.T__1)
            self.state = 85
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 86
            self.match(grammarGraphsLanguageParser.T__2)
            self.state = 87
            self.match(grammarGraphsLanguageParser.T__3)
            self.state = 88
            self.grafo_info()
            self.state = 89
            self.match(grammarGraphsLanguageParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Grafo_infoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_vertice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGraphsLanguageParser.Declaracao_verticeContext)
            else:
                return self.getTypedRuleContext(grammarGraphsLanguageParser.Declaracao_verticeContext,i)


        def declaracao_aresta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGraphsLanguageParser.Declaracao_arestaContext)
            else:
                return self.getTypedRuleContext(grammarGraphsLanguageParser.Declaracao_arestaContext,i)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_grafo_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrafo_info" ):
                listener.enterGrafo_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrafo_info" ):
                listener.exitGrafo_info(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrafo_info" ):
                return visitor.visitGrafo_info(self)
            else:
                return visitor.visitChildren(self)




    def grafo_info(self):

        localctx = grammarGraphsLanguageParser.Grafo_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_grafo_info)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==8:
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 91
                    self.declaracao_vertice()
                    pass
                elif token in [8]:
                    self.state = 92
                    self.declaracao_aresta()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vertice_ou_arestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertice(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.VerticeContext,0)


        def aresta(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.ArestaContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_vertice_ou_aresta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertice_ou_aresta" ):
                listener.enterVertice_ou_aresta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertice_ou_aresta" ):
                listener.exitVertice_ou_aresta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertice_ou_aresta" ):
                return visitor.visitVertice_ou_aresta(self)
            else:
                return visitor.visitChildren(self)




    def vertice_ou_aresta(self):

        localctx = grammarGraphsLanguageParser.Vertice_ou_arestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vertice_ou_aresta)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.vertice()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.aresta()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vertice_ou_aresta_simplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertice_sem_peso(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Vertice_sem_pesoContext,0)


        def aresta_declaracao_simples(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Aresta_declaracao_simplesContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_vertice_ou_aresta_simples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertice_ou_aresta_simples" ):
                listener.enterVertice_ou_aresta_simples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertice_ou_aresta_simples" ):
                listener.exitVertice_ou_aresta_simples(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertice_ou_aresta_simples" ):
                return visitor.visitVertice_ou_aresta_simples(self)
            else:
                return visitor.visitChildren(self)




    def vertice_ou_aresta_simples(self):

        localctx = grammarGraphsLanguageParser.Vertice_ou_aresta_simplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vertice_ou_aresta_simples)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.vertice_sem_peso()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.aresta_declaracao_simples()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_verticeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGraphsLanguageParser.VerticeContext)
            else:
                return self.getTypedRuleContext(grammarGraphsLanguageParser.VerticeContext,i)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_declaracao_vertice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_vertice" ):
                listener.enterDeclaracao_vertice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_vertice" ):
                listener.exitDeclaracao_vertice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_vertice" ):
                return visitor.visitDeclaracao_vertice(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_vertice(self):

        localctx = grammarGraphsLanguageParser.Declaracao_verticeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaracao_vertice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(grammarGraphsLanguageParser.T__5)
            self.state = 107
            self.vertice()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 108
                self.match(grammarGraphsLanguageParser.T__6)
                self.state = 109
                self.vertice()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerticeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertice_com_peso(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Vertice_com_pesoContext,0)


        def vertice_sem_peso(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Vertice_sem_pesoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_vertice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertice" ):
                listener.enterVertice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertice" ):
                listener.exitVertice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertice" ):
                return visitor.visitVertice(self)
            else:
                return visitor.visitChildren(self)




    def vertice(self):

        localctx = grammarGraphsLanguageParser.VerticeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vertice)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.vertice_com_peso()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.vertice_sem_peso()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vertice_sem_pesoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_vertice_sem_peso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertice_sem_peso" ):
                listener.enterVertice_sem_peso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertice_sem_peso" ):
                listener.exitVertice_sem_peso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertice_sem_peso" ):
                return visitor.visitVertice_sem_peso(self)
            else:
                return visitor.visitChildren(self)




    def vertice_sem_peso(self):

        localctx = grammarGraphsLanguageParser.Vertice_sem_pesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vertice_sem_peso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(grammarGraphsLanguageParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vertice_com_pesoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def valor(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.ValorContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_vertice_com_peso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertice_com_peso" ):
                listener.enterVertice_com_peso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertice_com_peso" ):
                listener.exitVertice_com_peso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVertice_com_peso" ):
                return visitor.visitVertice_com_peso(self)
            else:
                return visitor.visitChildren(self)




    def vertice_com_peso(self):

        localctx = grammarGraphsLanguageParser.Vertice_com_pesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vertice_com_peso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 124
            self.match(grammarGraphsLanguageParser.T__2)
            self.state = 125
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_arestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aresta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGraphsLanguageParser.ArestaContext)
            else:
                return self.getTypedRuleContext(grammarGraphsLanguageParser.ArestaContext,i)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_declaracao_aresta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_aresta" ):
                listener.enterDeclaracao_aresta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_aresta" ):
                listener.exitDeclaracao_aresta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_aresta" ):
                return visitor.visitDeclaracao_aresta(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_aresta(self):

        localctx = grammarGraphsLanguageParser.Declaracao_arestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declaracao_aresta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(grammarGraphsLanguageParser.T__7)
            self.state = 128
            self.aresta()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 129
                self.match(grammarGraphsLanguageParser.T__6)
                self.state = 130
                self.aresta()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aresta_declaracao_simples(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Aresta_declaracao_simplesContext,0)


        def aresta_declaracao_complexa(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Aresta_declaracao_complexaContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_aresta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAresta" ):
                listener.enterAresta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAresta" ):
                listener.exitAresta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAresta" ):
                return visitor.visitAresta(self)
            else:
                return visitor.visitChildren(self)




    def aresta(self):

        localctx = grammarGraphsLanguageParser.ArestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_aresta)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.aresta_declaracao_simples()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.aresta_declaracao_complexa()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aresta_declaracao_simplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGraphsLanguageParser.IDENT)
            else:
                return self.getToken(grammarGraphsLanguageParser.IDENT, i)

        def direcao(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.DirecaoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_aresta_declaracao_simples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAresta_declaracao_simples" ):
                listener.enterAresta_declaracao_simples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAresta_declaracao_simples" ):
                listener.exitAresta_declaracao_simples(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAresta_declaracao_simples" ):
                return visitor.visitAresta_declaracao_simples(self)
            else:
                return visitor.visitChildren(self)




    def aresta_declaracao_simples(self):

        localctx = grammarGraphsLanguageParser.Aresta_declaracao_simplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_aresta_declaracao_simples)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(grammarGraphsLanguageParser.T__8)
            self.state = 143
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 144
            self.direcao()
            self.state = 145
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 146
            self.match(grammarGraphsLanguageParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aresta_declaracao_complexaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGraphsLanguageParser.IDENT)
            else:
                return self.getToken(grammarGraphsLanguageParser.IDENT, i)

        def direcao(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.DirecaoContext,0)


        def valor(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.ValorContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_aresta_declaracao_complexa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAresta_declaracao_complexa" ):
                listener.enterAresta_declaracao_complexa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAresta_declaracao_complexa" ):
                listener.exitAresta_declaracao_complexa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAresta_declaracao_complexa" ):
                return visitor.visitAresta_declaracao_complexa(self)
            else:
                return visitor.visitChildren(self)




    def aresta_declaracao_complexa(self):

        localctx = grammarGraphsLanguageParser.Aresta_declaracao_complexaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_aresta_declaracao_complexa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(grammarGraphsLanguageParser.T__8)
            self.state = 149
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 150
            self.direcao()
            self.state = 151
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 152
            self.match(grammarGraphsLanguageParser.T__6)
            self.state = 153
            self.valor()
            self.state = 154
            self.match(grammarGraphsLanguageParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirecaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_direcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirecao" ):
                listener.enterDirecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirecao" ):
                listener.exitDirecao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirecao" ):
                return visitor.visitDirecao(self)
            else:
                return visitor.visitChildren(self)




    def direcao(self):

        localctx = grammarGraphsLanguageParser.DirecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_direcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd_add_vertice(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Cmd_add_verticeContext,0)


        def cmd_add_aresta(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Cmd_add_arestaContext,0)


        def cmd_atribuicao(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Cmd_atribuicaoContext,0)


        def cmd_imprime(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Cmd_imprimeContext,0)


        def cmd_remove_vertice(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Cmd_remove_verticeContext,0)


        def cmd_remove_aresta(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Cmd_remove_arestaContext,0)


        def cmd_outros(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Cmd_outrosContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd" ):
                return visitor.visitCmd(self)
            else:
                return visitor.visitChildren(self)




    def cmd(self):

        localctx = grammarGraphsLanguageParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cmd)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.cmd_add_vertice()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.cmd_add_aresta()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.cmd_atribuicao()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.cmd_imprime()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.cmd_remove_vertice()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.cmd_remove_aresta()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 164
                self.cmd_outros()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_add_verticeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def vertice(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.VerticeContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd_add_vertice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_add_vertice" ):
                listener.enterCmd_add_vertice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_add_vertice" ):
                listener.exitCmd_add_vertice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_add_vertice" ):
                return visitor.visitCmd_add_vertice(self)
            else:
                return visitor.visitChildren(self)




    def cmd_add_vertice(self):

        localctx = grammarGraphsLanguageParser.Cmd_add_verticeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cmd_add_vertice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 168
            self.match(grammarGraphsLanguageParser.T__13)
            self.state = 169
            self.vertice()
            self.state = 170
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 171
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_remove_verticeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def vertice_sem_peso(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Vertice_sem_pesoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd_remove_vertice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_remove_vertice" ):
                listener.enterCmd_remove_vertice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_remove_vertice" ):
                listener.exitCmd_remove_vertice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_remove_vertice" ):
                return visitor.visitCmd_remove_vertice(self)
            else:
                return visitor.visitChildren(self)




    def cmd_remove_vertice(self):

        localctx = grammarGraphsLanguageParser.Cmd_remove_verticeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cmd_remove_vertice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 174
            self.match(grammarGraphsLanguageParser.T__14)
            self.state = 175
            self.vertice_sem_peso()
            self.state = 176
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 177
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_add_arestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def aresta(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.ArestaContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd_add_aresta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_add_aresta" ):
                listener.enterCmd_add_aresta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_add_aresta" ):
                listener.exitCmd_add_aresta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_add_aresta" ):
                return visitor.visitCmd_add_aresta(self)
            else:
                return visitor.visitChildren(self)




    def cmd_add_aresta(self):

        localctx = grammarGraphsLanguageParser.Cmd_add_arestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cmd_add_aresta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 180
            self.match(grammarGraphsLanguageParser.T__15)
            self.state = 181
            self.aresta()
            self.state = 182
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 183
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_remove_arestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def aresta_declaracao_simples(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Aresta_declaracao_simplesContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd_remove_aresta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_remove_aresta" ):
                listener.enterCmd_remove_aresta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_remove_aresta" ):
                listener.exitCmd_remove_aresta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_remove_aresta" ):
                return visitor.visitCmd_remove_aresta(self)
            else:
                return visitor.visitChildren(self)




    def cmd_remove_aresta(self):

        localctx = grammarGraphsLanguageParser.Cmd_remove_arestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_cmd_remove_aresta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 186
            self.match(grammarGraphsLanguageParser.T__16)
            self.state = 187
            self.aresta_declaracao_simples()
            self.state = 188
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 189
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_atribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao_peso(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Atribuicao_pesoContext,0)


        def atribuicao_criacao_aresta(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Atribuicao_criacao_arestaContext,0)


        def atribuicao_grafo(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Atribuicao_grafoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_atribuicao" ):
                listener.enterCmd_atribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_atribuicao" ):
                listener.exitCmd_atribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_atribuicao" ):
                return visitor.visitCmd_atribuicao(self)
            else:
                return visitor.visitChildren(self)




    def cmd_atribuicao(self):

        localctx = grammarGraphsLanguageParser.Cmd_atribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cmd_atribuicao)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.atribuicao_peso()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.atribuicao_criacao_aresta()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.atribuicao_grafo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_imprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imprime_estrutura(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Imprime_estruturaContext,0)


        def imprime_grafo(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Imprime_grafoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd_imprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_imprime" ):
                listener.enterCmd_imprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_imprime" ):
                listener.exitCmd_imprime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_imprime" ):
                return visitor.visitCmd_imprime(self)
            else:
                return visitor.visitChildren(self)




    def cmd_imprime(self):

        localctx = grammarGraphsLanguageParser.Cmd_imprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_cmd_imprime)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.imprime_estrutura()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.imprime_grafo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_outrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caminho_mais_curto(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Caminho_mais_curtoContext,0)


        def imprime_caminho_mais_curto(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Imprime_caminho_mais_curtoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_cmd_outros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_outros" ):
                listener.enterCmd_outros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_outros" ):
                listener.exitCmd_outros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd_outros" ):
                return visitor.visitCmd_outros(self)
            else:
                return visitor.visitChildren(self)




    def cmd_outros(self):

        localctx = grammarGraphsLanguageParser.Cmd_outrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_cmd_outros)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.caminho_mais_curto()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.imprime_caminho_mais_curto()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atribuicao_pesoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def vertice_ou_aresta_simples(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.Vertice_ou_aresta_simplesContext,0)


        def valor(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.ValorContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_atribuicao_peso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao_peso" ):
                listener.enterAtribuicao_peso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao_peso" ):
                listener.exitAtribuicao_peso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao_peso" ):
                return visitor.visitAtribuicao_peso(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao_peso(self):

        localctx = grammarGraphsLanguageParser.Atribuicao_pesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_atribuicao_peso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 205
            self.match(grammarGraphsLanguageParser.T__17)
            self.state = 206
            self.vertice_ou_aresta_simples()
            self.state = 207
            self.match(grammarGraphsLanguageParser.T__2)
            self.state = 208
            self.valor()
            self.state = 209
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atribuicao_criacao_arestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGraphsLanguageParser.IDENT)
            else:
                return self.getToken(grammarGraphsLanguageParser.IDENT, i)

        def vertice_sem_peso(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGraphsLanguageParser.Vertice_sem_pesoContext)
            else:
                return self.getTypedRuleContext(grammarGraphsLanguageParser.Vertice_sem_pesoContext,i)


        def direcao(self):
            return self.getTypedRuleContext(grammarGraphsLanguageParser.DirecaoContext,0)


        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_atribuicao_criacao_aresta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao_criacao_aresta" ):
                listener.enterAtribuicao_criacao_aresta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao_criacao_aresta" ):
                listener.exitAtribuicao_criacao_aresta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao_criacao_aresta" ):
                return visitor.visitAtribuicao_criacao_aresta(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao_criacao_aresta(self):

        localctx = grammarGraphsLanguageParser.Atribuicao_criacao_arestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_atribuicao_criacao_aresta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 212
            self.match(grammarGraphsLanguageParser.T__17)
            self.state = 213
            self.vertice_sem_peso()
            self.state = 214
            self.direcao()
            self.state = 215
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 216
            self.match(grammarGraphsLanguageParser.T__17)
            self.state = 217
            self.vertice_sem_peso()
            self.state = 218
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atribuicao_grafoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGraphsLanguageParser.IDENT)
            else:
                return self.getToken(grammarGraphsLanguageParser.IDENT, i)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_atribuicao_grafo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao_grafo" ):
                listener.enterAtribuicao_grafo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao_grafo" ):
                listener.exitAtribuicao_grafo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao_grafo" ):
                return visitor.visitAtribuicao_grafo(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao_grafo(self):

        localctx = grammarGraphsLanguageParser.Atribuicao_grafoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_atribuicao_grafo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 221
            self.match(grammarGraphsLanguageParser.T__2)
            self.state = 222
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 223
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Imprime_estruturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_imprime_estrutura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprime_estrutura" ):
                listener.enterImprime_estrutura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprime_estrutura" ):
                listener.exitImprime_estrutura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprime_estrutura" ):
                return visitor.visitImprime_estrutura(self)
            else:
                return visitor.visitChildren(self)




    def imprime_estrutura(self):

        localctx = grammarGraphsLanguageParser.Imprime_estruturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_imprime_estrutura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(grammarGraphsLanguageParser.T__18)
            self.state = 226
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 227
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 228
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Imprime_grafoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(grammarGraphsLanguageParser.IDENT, 0)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_imprime_grafo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprime_grafo" ):
                listener.enterImprime_grafo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprime_grafo" ):
                listener.exitImprime_grafo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprime_grafo" ):
                return visitor.visitImprime_grafo(self)
            else:
                return visitor.visitChildren(self)




    def imprime_grafo(self):

        localctx = grammarGraphsLanguageParser.Imprime_grafoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_imprime_grafo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(grammarGraphsLanguageParser.T__19)
            self.state = 231
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 232
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 233
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Caminho_mais_curtoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGraphsLanguageParser.IDENT)
            else:
                return self.getToken(grammarGraphsLanguageParser.IDENT, i)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_caminho_mais_curto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaminho_mais_curto" ):
                listener.enterCaminho_mais_curto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaminho_mais_curto" ):
                listener.exitCaminho_mais_curto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaminho_mais_curto" ):
                return visitor.visitCaminho_mais_curto(self)
            else:
                return visitor.visitChildren(self)




    def caminho_mais_curto(self):

        localctx = grammarGraphsLanguageParser.Caminho_mais_curtoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_caminho_mais_curto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 236
            self.match(grammarGraphsLanguageParser.T__20)
            self.state = 237
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 238
            self.match(grammarGraphsLanguageParser.T__6)
            self.state = 239
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 240
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 241
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Imprime_caminho_mais_curtoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGraphsLanguageParser.IDENT)
            else:
                return self.getToken(grammarGraphsLanguageParser.IDENT, i)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_imprime_caminho_mais_curto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprime_caminho_mais_curto" ):
                listener.enterImprime_caminho_mais_curto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprime_caminho_mais_curto" ):
                listener.exitImprime_caminho_mais_curto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprime_caminho_mais_curto" ):
                return visitor.visitImprime_caminho_mais_curto(self)
            else:
                return visitor.visitChildren(self)




    def imprime_caminho_mais_curto(self):

        localctx = grammarGraphsLanguageParser.Imprime_caminho_mais_curtoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_imprime_caminho_mais_curto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 244
            self.match(grammarGraphsLanguageParser.T__21)
            self.state = 245
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 246
            self.match(grammarGraphsLanguageParser.T__6)
            self.state = 247
            self.match(grammarGraphsLanguageParser.IDENT)
            self.state = 248
            self.match(grammarGraphsLanguageParser.T__9)
            self.state = 249
            self.match(grammarGraphsLanguageParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(grammarGraphsLanguageParser.NUM_INT, 0)

        def NUM_REAL(self):
            return self.getToken(grammarGraphsLanguageParser.NUM_REAL, 0)

        def getRuleIndex(self):
            return grammarGraphsLanguageParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = grammarGraphsLanguageParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





