from antlr4.error.ErrorListener import ErrorListener

"""
    De acordo com a documentação, criar uma classe que herda de ErrorListener
    e sobrescrever o método syntaxError é a forma recomendada de tratar erros
    léxicos e sintáticos no ANTLR.
"""

class LexerErrorHandler(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Parser da mensagem de erro para pegarmos a informação do símbolo que representa o erro
        error_symbol = str(e).split("(")[1][1]

        raise Exception(f'Sintatic Error. Unrecognized symbol in line {line}. Symbol: {error_symbol}') from None

class ParserErrorHandler(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Pegamos o valor do símbolo que causou o erro
        symbol = offendingSymbol.text
        if symbol == '<EOF>':
            symbol = 'EOF'

        raise Exception(f'Sintatic Error. Unrecognized symbol in line {line}. Symbol: {symbol}') from None

class GraphAlreadyDeclared(Exception):
    def __init__(self, graph, line=None):
        self.graph = graph
        if not line:
            self.message = f"Semantic Error. GraphAlreadyDeclaredError: Graph {graph} already declared"
        else:
            self.message = f"Semantic Error. GraphAlreadyDeclaredError: Graph {graph} already declared at line {line}"

    def __str__(self):
        return self.message

class GraphNotDeclared(Exception):
    def __init__(self, graph, line=None):
        self.graph = graph
        if not line:
            self.message = f"Semantic Error. GraphNotDeclaredError: Graph {graph} not declared"
        else:
            self.message = f"Semantic Error. GraphNotDeclaredError: Graph {graph} not declared at line {line}"

    def __str__(self):
        return self.message

class VertexNotDeclared(Exception):
    def __init__(self, vertex, line=None):
        self.vertex = vertex
        if not line:
            self.message = f"Semantic Error. VertexNotDeclaredError: Vertex {vertex} not declared"
        else:
            self.message = f"Semantic Error. VertexNotDeclaredError: Vertex {vertex} not declared at line {line}"

    def __str__(self):
        return self.message

class VertexContainsEdge(Exception):
    def __init__(self, vertex, line=None):
        self.vertex = vertex
        if not line:
            self.message = f"Semantic Error. VertexContainsEdge: Vertex {vertex} contains edge"
        else:
            self.message = f"Semantic Error. VertexContainsEdge: Vertex {vertex} contains edge at line {line}"

    def __str__(self):
        return self.message

class EdgeNotDeclared(Exception):
    def __init__(self, edge, line=None):
        self.edge = edge
        if not line:
            self.message = f"Semantic Error. EdgeNotDeclared: Edge {edge} not declared"
        else:
            self.message = f"Semantic Error. EdgeNotDeclared: Edge {edge} not declared at line {line}"

    def __str__(self):
        return self.message
