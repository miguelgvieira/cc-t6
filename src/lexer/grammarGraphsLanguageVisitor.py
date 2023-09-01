# Generated from grammarGraphsLanguage.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .grammarGraphsLanguageParser import grammarGraphsLanguageParser
else:
    from grammarGraphsLanguageParser import grammarGraphsLanguageParser

# This class defines a complete generic visitor for a parse tree produced by grammarGraphsLanguageParser.

class grammarGraphsLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarGraphsLanguageParser#programa.
    def visitPrograma(self, ctx:grammarGraphsLanguageParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#declaracao_grafo.
    def visitDeclaracao_grafo(self, ctx:grammarGraphsLanguageParser.Declaracao_grafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#declaracao_simples.
    def visitDeclaracao_simples(self, ctx:grammarGraphsLanguageParser.Declaracao_simplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#declaracao_complexa.
    def visitDeclaracao_complexa(self, ctx:grammarGraphsLanguageParser.Declaracao_complexaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#grafo_info.
    def visitGrafo_info(self, ctx:grammarGraphsLanguageParser.Grafo_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#vertice_ou_aresta.
    def visitVertice_ou_aresta(self, ctx:grammarGraphsLanguageParser.Vertice_ou_arestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#vertice_ou_aresta_simples.
    def visitVertice_ou_aresta_simples(self, ctx:grammarGraphsLanguageParser.Vertice_ou_aresta_simplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#declaracao_vertice.
    def visitDeclaracao_vertice(self, ctx:grammarGraphsLanguageParser.Declaracao_verticeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#vertice.
    def visitVertice(self, ctx:grammarGraphsLanguageParser.VerticeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#vertice_sem_peso.
    def visitVertice_sem_peso(self, ctx:grammarGraphsLanguageParser.Vertice_sem_pesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#vertice_com_peso.
    def visitVertice_com_peso(self, ctx:grammarGraphsLanguageParser.Vertice_com_pesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#declaracao_aresta.
    def visitDeclaracao_aresta(self, ctx:grammarGraphsLanguageParser.Declaracao_arestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#aresta.
    def visitAresta(self, ctx:grammarGraphsLanguageParser.ArestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#aresta_declaracao_simples.
    def visitAresta_declaracao_simples(self, ctx:grammarGraphsLanguageParser.Aresta_declaracao_simplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#aresta_declaracao_complexa.
    def visitAresta_declaracao_complexa(self, ctx:grammarGraphsLanguageParser.Aresta_declaracao_complexaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#direcao.
    def visitDirecao(self, ctx:grammarGraphsLanguageParser.DirecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd.
    def visitCmd(self, ctx:grammarGraphsLanguageParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_add_vertice.
    def visitCmd_add_vertice(self, ctx:grammarGraphsLanguageParser.Cmd_add_verticeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_remove_vertice.
    def visitCmd_remove_vertice(self, ctx:grammarGraphsLanguageParser.Cmd_remove_verticeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_add_aresta.
    def visitCmd_add_aresta(self, ctx:grammarGraphsLanguageParser.Cmd_add_arestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_remove_aresta.
    def visitCmd_remove_aresta(self, ctx:grammarGraphsLanguageParser.Cmd_remove_arestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_atribuicao.
    def visitCmd_atribuicao(self, ctx:grammarGraphsLanguageParser.Cmd_atribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_imprime.
    def visitCmd_imprime(self, ctx:grammarGraphsLanguageParser.Cmd_imprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_outros.
    def visitCmd_outros(self, ctx:grammarGraphsLanguageParser.Cmd_outrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#atribuicao_peso.
    def visitAtribuicao_peso(self, ctx:grammarGraphsLanguageParser.Atribuicao_pesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#atribuicao_criacao_aresta.
    def visitAtribuicao_criacao_aresta(self, ctx:grammarGraphsLanguageParser.Atribuicao_criacao_arestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#atribuicao_grafo.
    def visitAtribuicao_grafo(self, ctx:grammarGraphsLanguageParser.Atribuicao_grafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#imprime_estrutura.
    def visitImprime_estrutura(self, ctx:grammarGraphsLanguageParser.Imprime_estruturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#imprime_grafo.
    def visitImprime_grafo(self, ctx:grammarGraphsLanguageParser.Imprime_grafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#caminho_mais_curto.
    def visitCaminho_mais_curto(self, ctx:grammarGraphsLanguageParser.Caminho_mais_curtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#imprime_caminho_mais_curto.
    def visitImprime_caminho_mais_curto(self, ctx:grammarGraphsLanguageParser.Imprime_caminho_mais_curtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#valor.
    def visitValor(self, ctx:grammarGraphsLanguageParser.ValorContext):
        return self.visitChildren(ctx)



del grammarGraphsLanguageParser