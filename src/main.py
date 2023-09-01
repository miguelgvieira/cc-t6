import os
import sys
from graphs_lexer import GraphsLexerAnalyzer

""" Main function do nosso analisador léxico e sintático
    Recebe o arquivo de entrada como argumento.

    Exemplo de uso:
    ```
    $ python3 main.py input/arquivo_teste1.graph
    ```

    Onde input/arquivo_teste1.txt é o arquivo de entrada.

    O analisador léxico tem sua lógica implementado em lexical_compiler/graphs_lexer.py
"""

def main(args):
    # Verifica se os argumentos foram passados corretamente
    if len(args) != 1:
        print("Usage: python3 main.py input/file.graph")
        sys.exit(1)

    # Verifica se o arquivo de entrada existe
    if not os.path.isfile(args[0]):
        print(args[0])
        print("Input file does not exist")
        sys.exit(1)

    # Instancia o analisador léxico
    alguma_lexer = GraphsLexerAnalyzer()

    # Roda o compilador no arquivo de entrada.
    alguma_lexer.analyse_file(args[0])

if __name__ == '__main__':
    # main(["input", "output"])
    main(sys.argv[1:])
