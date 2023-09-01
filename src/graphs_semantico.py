# Generated from grammarGraphsLanguage.g4 by ANTLR 4.13.0
import sys
sys.tracebacklimit = 0

from antlr4 import *
from errors import GraphNotDeclared, GraphAlreadyDeclared, VertexNotDeclared, EdgeNotDeclared, VertexContainsEdge
from lexer.grammarGraphsLanguageVisitor import grammarGraphsLanguageVisitor
from lexer.grammarGraphsLanguageParser import grammarGraphsLanguageParser
from sym_table import SymTable
from graphs_utils import pretty_print
from graph_drawer import GraphDrawer

# This class defines a complete generic visitor for a parse tree produced by grammarGraphsLanguageParser.

class GraphsSemantico(grammarGraphsLanguageVisitor):

    def __init__(self):
        self.sym_table = SymTable()

    def try_catch_sym_table_calls(self, ctx, func, *args):
        try:
            return func(*args)
        except GraphNotDeclared as e:
            raise GraphNotDeclared(e.graph, ctx.start.line) from None
        except GraphAlreadyDeclared as e:
            raise GraphAlreadyDeclared(e.graph, ctx.start.line) from None
        except VertexNotDeclared as e:
            raise VertexNotDeclared(e.vertex, ctx.start.line) from None
        except EdgeNotDeclared as e:
            raise EdgeNotDeclared(e.edge, ctx.start.line) from None
        except VertexContainsEdge as e:
            raise VertexContainsEdge(e.vertex, ctx.start.line) from None
        except Exception as e:
            raise Exception(f"Linha {ctx.start.line}: {e}")

    # Visit a parse tree produced by grammarGraphsLanguageParser#programa.
    def visitPrograma(self, ctx:grammarGraphsLanguageParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#declaracao_simples.
    def visitDeclaracao_simples(self, ctx:grammarGraphsLanguageParser.Declaracao_simplesContext):

        self.try_catch_sym_table_calls(ctx, self.sym_table.add_graph, ctx.IDENT())

        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#declaracao_complexa.
    def visitDeclaracao_complexa(self, ctx:grammarGraphsLanguageParser.Declaracao_complexaContext):
        self.try_catch_sym_table_calls(ctx, self.sym_table.add_graph, ctx.IDENT())
        self.sym_table.graph_context = ctx.IDENT().getText()

        self.visitGrafo_info(ctx.grafo_info())

        self.sym_table.graph_context = None

        return 0


    # Visit a parse tree produced by grammarGraphsLanguageParser#grafo_info.
    def visitGrafo_info(self, ctx:grammarGraphsLanguageParser.Grafo_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#vertice.
    def visitVertice_sem_peso(self, ctx:grammarGraphsLanguageParser.Vertice_sem_pesoContext):
        self.try_catch_sym_table_calls(ctx, self.sym_table.add_vertex, ctx.IDENT().getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammarGraphsLanguageParser#vertice_com_peso.
    def visitVertice_com_peso(self, ctx:grammarGraphsLanguageParser.Vertice_com_pesoContext):
        ident = ctx.IDENT().getText()
        weight = ctx.valor().getText()

        self.try_catch_sym_table_calls(ctx, self.sym_table.add_vertex, ident, weight)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarGraphsLanguageParser#aresta_declaracao.
    def visitAresta_declaracao_simples(self, ctx:grammarGraphsLanguageParser.Aresta_declaracao_simplesContext):
        vertex1 = ctx.IDENT()[0].getText()
        vertex2 = ctx.IDENT()[1].getText()
        direction = ctx.direcao().getText()

        self.try_catch_sym_table_calls(ctx, self.sym_table.add_edge, vertex1, vertex2, direction, None)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammarGraphsLanguageParser#aresta_declaracao_complexa.
    def visitAresta_declaracao_complexa(self, ctx:grammarGraphsLanguageParser.Aresta_declaracao_complexaContext):
        vertex1 = ctx.IDENT()[0].getText()
        vertex2 = ctx.IDENT()[1].getText()
        direction = ctx.direcao().getText()
        weight = ctx.valor().getText()

        self.try_catch_sym_table_calls(ctx, self.sym_table.add_edge, vertex1, vertex2, direction, weight)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_add_vertice.
    def visitCmd_add_vertice(self, ctx:grammarGraphsLanguageParser.Cmd_add_verticeContext):
        ident = ctx.IDENT().getText()

        self.sym_table.graph_context = ident

        self.visitChildren(ctx)

        self.sym_table.graph_context = None

        return 0

    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_remove_vertice.
    def visitCmd_remove_vertice(self, ctx:grammarGraphsLanguageParser.Cmd_remove_verticeContext):
        ident = ctx.IDENT().getText()

        self.sym_table.graph_context = ident

        self.try_catch_sym_table_calls(ctx, self.sym_table.remove_vertex, ctx.vertice_sem_peso().getText())

        self.sym_table.graph_context = None

        return 0

    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_add_aresta.
    def visitCmd_add_aresta(self, ctx:grammarGraphsLanguageParser.Cmd_add_arestaContext):
        ident = ctx.IDENT().getText()

        self.sym_table.graph_context = ident

        self.visitChildren(ctx)

        self.sym_table.graph_context = None

        return 0

    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_remove_aresta.
    def visitCmd_remove_aresta(self, ctx:grammarGraphsLanguageParser.Cmd_remove_arestaContext):
        vertex1 = ctx.aresta_declaracao_simples().IDENT()[0].getText()
        vertex2 = ctx.aresta_declaracao_simples().IDENT()[1].getText()
        direction = ctx.aresta_declaracao_simples().direcao().getText()

        ident = ctx.IDENT().getText()

        self.sym_table.graph_context = ident

        self.try_catch_sym_table_calls(ctx, self.sym_table.remove_edge, vertex1, vertex2, direction)

        self.sym_table.graph_context = None

        return 0


    # Visit a parse tree produced by grammarGraphsLanguageParser#cmd_atribuicao.
    def visitCmd_atribuicao(self, ctx:grammarGraphsLanguageParser.Cmd_atribuicaoContext):
        self.visitChildren(ctx)

    # Visit a parse tree produced by grammarGraphsLanguageParser#atribuicao_peso.
    def visitAtribuicao_peso(self, ctx:grammarGraphsLanguageParser.Atribuicao_pesoContext):
        ident = ctx.IDENT().getText()
        value = ctx.valor().getText()
        vertex_or_edge = ctx.vertice_ou_aresta_simples()

        self.sym_table.graph_context = ident

        if hasattr(vertex_or_edge, "vertice_sem_peso") \
            and vertex_or_edge.vertice_sem_peso() is not None:
            self.try_catch_sym_table_calls(ctx, self.sym_table.add_vertex, ident, value)
        else:
            edge = vertex_or_edge.aresta_declaracao_simples()
            vertex1 = edge.IDENT()[0].getText()
            vertex2 = edge.IDENT()[1].getText()
            direction = edge.direcao().getText()

            self.try_catch_sym_table_calls(ctx, self.sym_table.add_edge, vertex1, vertex2, direction, value)

        self.sym_table.graph_context = None

        return None

    # Visit a parse tree produced by grammarGraphsLanguageParser#atribuicao_criacao_aresta.
    def visitAtribuicao_criacao_aresta(self, ctx:grammarGraphsLanguageParser.Atribuicao_criacao_arestaContext):
        graph1 = ctx.IDENT()[0].getText()
        graph2 = ctx.IDENT()[1].getText()
        vertex1 = ctx.vertice_sem_peso()[0].getText()
        vertex2 = ctx.vertice_sem_peso()[1].getText()
        direction = ctx.direcao().getText()

        if graph1 != graph2:
            self.try_catch_sym_table_calls(ctx, self.sym_table.join_graph, graph1, graph2, vertex1, vertex2, direction)

        else:
            self.sym_table.graph_context = graph1

            self.try_catch_sym_table_calls(ctx, self.sym_table.add_vertex, vertex1, None)

            self.sym_table.graph_context = None

        return None

    # Visit a parse tree produced by grammarGraphsLanguageParser#atribuicao_grafo.
    def visitAtribuicao_grafo(self, ctx:grammarGraphsLanguageParser.Atribuicao_grafoContext):
        graph1 = ctx.IDENT()[0].getText()
        graph2 = ctx.IDENT()[1].getText()

        self.try_catch_sym_table_calls(ctx, self.sym_table._move_graph2_to_graph1, graph1, graph2)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammarGraphsLanguageParser#imprime_estrutura.
    def visitImprime_estrutura(self, ctx:grammarGraphsLanguageParser.Imprime_estruturaContext):
        ident = ctx.IDENT().getText()
        if not self.sym_table.graph_exists(ident):
            raise GraphNotDeclared(ident, ctx.start.line)
        else:
            pretty_print(self.sym_table.graphs[ident])
        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammarGraphsLanguageParser#imprime_grafo.
    def visitImprime_grafo(self, ctx:grammarGraphsLanguageParser.Imprime_grafoContext):
        graph_drawer = GraphDrawer()
        if not self.sym_table.graph_exists(ctx.IDENT().getText()):
            raise GraphNotDeclared(ctx.IDENT().getText(), ctx.start.line)

        graph_drawer.draw(self.sym_table.graphs[ctx.IDENT().getText()])
        return self.visitChildren(ctx)

    # Visit a parse tree produced by grammarGraphsLanguageParser#caminho_mais_curto.
    def visitCaminho_mais_curto(self, ctx:grammarGraphsLanguageParser.Caminho_mais_curtoContext):
        graph = ctx.IDENT()[0].getText()
        vertex1 = ctx.IDENT()[1].getText()
        vertex2 = ctx.IDENT()[2].getText()
        self.sym_table.graph_context = graph

        if not self.sym_table.graph_exists(graph):
            raise GraphNotDeclared(graph, ctx.start.line)
        if not self.sym_table._vertex_exists(vertex1):
            raise VertexNotDeclared(vertex1, ctx.start.line)
        if not self.sym_table._vertex_exists(vertex2):
            raise VertexNotDeclared(vertex2, ctx.start.line)

        graph_drawer = GraphDrawer()
        graph_drawer.create_graph(self.sym_table.graphs[graph])

        shortest_path = graph_drawer.shortest_path(vertex1, vertex2)
        if shortest_path is not None:
            print(f"Caminho mais curto: {shortest_path}")
        else:
            print("Não existe caminho entre os vértices")

        self.sym_table.graph_context = None

    # Visit a parse tree produced by grammarGraphsLanguageParser#imprime_caminho_mais_curto.
    def visitImprime_caminho_mais_curto(self, ctx:grammarGraphsLanguageParser.Imprime_caminho_mais_curtoContext):
        graph = ctx.IDENT()[0].getText()
        vertex1 = ctx.IDENT()[1].getText()
        vertex2 = ctx.IDENT()[2].getText()
        self.sym_table.graph_context = graph

        if not self.sym_table.graph_exists(graph):
            raise GraphNotDeclared(graph, ctx.start.line)
        if not self.sym_table._vertex_exists(vertex1):
            raise VertexNotDeclared(vertex1, ctx.start.line)
        if not self.sym_table._vertex_exists(vertex2):
            raise VertexNotDeclared(vertex2, ctx.start.line)

        graph_drawer = GraphDrawer()
        graph_drawer.create_graph(self.sym_table.graphs[graph])

        graph_drawer.draw_shortest_path(vertex1, vertex2)

        return self.visitChildren(ctx)