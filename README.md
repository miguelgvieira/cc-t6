# Resumo

Esse repositório contém um compilador, desenvolvido na disciplina de Construção de Compiladores, ofertada pelo Departamento de Computação da UFSCar.

O principal objetivo desse compilador é criar uma linguagem para fácil interpretação e criação de grafos, assim como desenha-los na tela e imprimir sua estrutura.

O compilador foi feito utilizando Python3 com auxílio do projeto [Antlr](https://www.antlr.org/).

# Aluno

- Miguel Gonçalves Vieira, RA: 609790

# Instalação

Para utilizar o compilador de grafos, recomenda-se utilizar um ambiente virtual para instalar os pacotes necessários, para não interferir com outros projetos. Foi utilizado o Python 3.11.3 para desenvolvimento.

```
python3 -m venv {virtual-env-name}
source {virtual-env-name}/bin/activate
```

Para instalar os pacotes necessários para rodar o programa, execute o comando:

```
pip3 install -r src/requirements.txt
````

# Rodando

Para executar o programa, basta executar o arquivo `src/main.py` passando como argumento o arquivo de entrada para ser analisado. O compilador irá processar o arquivo e retornar o resultado desejado. Se algum comando de impressão for passado, ele irá imprimir no terminal o resultado, ou abrirá uma nova janela com os grafos representados lá.

Exemplo:
```
python3 src/main.py src/entrada/run_1_create_multiple_graphs_and_print.graph
```

# Comandos Aceitos pelo Compilador


## Criação de grafos
```
grafo {nome_do_grafo}; # Cria um grafo com o nome desejado.

grafo {nome_do_grafo}{
    vertice {nome_vertice},...; Cria os vértices dentro do grafo. Mais de um argumento pode ser passado, separados por ,.

    vertice {nome_vertice}={peso},...; Cria os vértices dentro do grafo, passando um peso para esse vértice. Mais de um argumento pode ser passado, separados por ,.

    vertice ({vertice1} {direcao} {vertice_2}),...; Cria arestas no grafo. A direção é indicada por '>', '<'. '<>'. Multiplos argumenntos podem ser passados.

    vertice ({vertice1} {direcao} {vertice_2}, {peso}),...; Cria arestas no grafo, sendo que essa aresta terá o peso passado no argumento. A direção é indicada por '>', '<'. '<>'. Multiplos argumenntos podem ser passados.

}; # Cria um grafo com o nome desejado e com componentes dentro dele já definidos.

```
## Criação de arestas/vértices nos grafos
```
{nome_do_grafo}.adiciona_vertice({nome_vertice}); Cria um vértice com o nome passado dentro do grafo.

{nome_do_grafo}.adiciona_vertice({nome_vertice}={peso}); Cria um vértice com o nome passado dentro do grafo, e o peso desse vértice.

{nome_do_grafo}.adiciona_aresta({vertice1} {direcao} {vertice2}); Cria uma aresta entre os dois vértices passados, com a direção indicada.

{nome_do_grafo}.adiciona_aresta(({vertice1} {direcao} {vertice2}, {peso})); Cria uma aresta com peso entre os dois vértices passados.


```
## Remoção de arestas/vértices nos grafos
```
{nome_do_grafo}.remove_vertice({nome_vertice}); Remove o vértice com o nome passado dentro do grafo.

{nome_do_grafo}.remove_aresta({vertice1} {direcao} {vertice2}); Remove a aresta entre os dois vértices passados, com a direção indicada.
```

## Comandos
```
{nome_do_grafo}.{nome_vertice} = {peso}; Adiciona peso para o vértice.

{nome_do_grafo}.({vertice1} {direcao} {vertice2}) = {peso}; Adiciona peso para a aresta.

{nome_do_grafo}.{vertice1} {direcao} {nome_do_grafo}.{vertice2}; Cria uma nova aresta entre esses dois vértices. Pode ser usado para unir dois grafos diferentes.

{grafo1} = {grafo2}; Copia todas as informações entre os grafos 1 e 2.

imprime_estrutura({nome_do_grafo}); Imprime toda a estrutura do grafo desejado.

imprime_grafo({nome_do_grafo}); Desenha na tela o grafo desejado.

{nome_grafo}.caminho_mais_curto({vertice1, vertice2}); Acha o caminho mais curto entre os dois vértices passados e retorna em forma de lista.

{nome_grafo}.imprime_caminho_mais_curto({vertice1, vertice2}); Acha o caminho mais curto entre os dois vértices passados e desenha na tela esse caminho mais curto.
```

