from antlr4 import *
from lexer.grammarGraphsLanguageLexer import grammarGraphsLanguageLexer
from lexer.grammarGraphsLanguageParser import grammarGraphsLanguageParser
from lexer.grammarGraphsLanguageListener import grammarGraphsLanguageListener
from errors import LexerErrorHandler
from errors import ParserErrorHandler
from graphs_semantico import GraphsSemantico

"""
    Classe responsável por analisar o arquivo de entrada e gerar o arquivo de saída
    com os tokens encontrados.

    O método error_handling é chamado quando um erro léxico é encontrado. Ele recebe
    o token que causou o erro e escreve no arquivo de saída a mensagem de erro
    correspondente.

    O método analyse_file recebe o arquivo de entrada e o arquivo de saída e chama
    o analisador léxico para cada token do arquivo de entrada. Quando o token EOF
    é encontrado, o loop é encerrado.

    Exemplo de uso:
    ```
    lexer = AlgumaLexerAnalyzer()
    lexer.analyse_file("input_file.txt", "output_file.txt")
    ```

    O analisador léxico tem sua lógica implementado em dist/AlgumaLexer.py, criada pelo
    ANTLR, utilizando a gramática definida em AlgumaLexer.g4.

    O arquivo AlgumaLexer.py é gerado automaticamente pelo ANTLR, não deve ser alterado.
    
"""


class GraphsLexerAnalyzer():

    # Função para mudar os error handlers do lexer e parser
    # criados no arquivo error_handling.py
    def change_error_handlers(self):
        self.la_lexer.removeErrorListeners()
        self.la_lexer.addErrorListener(LexerErrorHandler())

        self.parser.removeErrorListeners()
        self.parser.addErrorListener(ParserErrorHandler())

    def write_error(self, error):
        self.output_stream.write(f"Linha {error['line']}: {error['message']}\n")

    def write_code(self, code):
        self.output_stream.write(code + "\n")

    def analyse_file(self, input_file):
        self.input_stream = FileStream(input_file, encoding='utf-8')
        self.la_lexer = grammarGraphsLanguageLexer(self.input_stream)

        # Aqui definimos o Parser do nosso compilador
        tokens = CommonTokenStream(self.la_lexer)
        self.parser = grammarGraphsLanguageParser(tokens)
        graphs_semantico = GraphsSemantico()

        self.change_error_handlers()

        tree = self.parser.programa()
        graphs_semantico.visitPrograma(tree)
