grammar grammarGraphsLanguage;

// Números
// Como visto em aula, primeiro precisamos testar para inteiros, depois para real
NUM_INT	: /*('+'|'-')?*/('0'..'9')+
 	;
NUM_REAL : /*('+'|'-')?*/('0'..'9')+ ('.' ('0'..'9')+)?
 	;

// Identificadores
IDENT : ('a'..'z'|'A'..'Z' | '_') ('_' | 'a'..'z'|'A'..'Z'|'0'..'9')*
	;

// Cadeia de caracteres
CADEIA 	: '"' ( ESC_SEQ | ~('"'|'\\' | '\n') )* '"'
	;

ESC_SEQ	: '\\"' | '\\n';

// Comentários são identificados por '#'
COMENTARIO
    :   '#' ~('\r' |'\n')* ('\n' | EOF) -> skip
    ;

// Espaços em branco são ignorados.
WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;

// Definições das regras sintáticas, disponíveis na apostila Gramática_LA

programa : ( declaracao_grafo | cmd )* EOF;
declaracao_grafo : declaracao_simples ';'
		| declaracao_complexa ';'
	;

// Comandos gerais
declaracao_simples : 'grafo' IDENT ;
declaracao_complexa : 'grafo' IDENT '=' '{' grafo_info '}' ;
grafo_info : ( declaracao_vertice | declaracao_aresta )* ;
vertice_ou_aresta : vertice | aresta ;
vertice_ou_aresta_simples : vertice_sem_peso | aresta_declaracao_simples ;

// vertices
declaracao_vertice : 'vertice' vertice (',' vertice)* ';' ;
vertice : vertice_com_peso | vertice_sem_peso ;
vertice_sem_peso : IDENT ;
vertice_com_peso: IDENT '=' valor ;

//arestas
declaracao_aresta : 'aresta' aresta (',' aresta) * ';' ;
aresta : aresta_declaracao_simples | aresta_declaracao_complexa ;
aresta_declaracao_simples : '(' IDENT direcao IDENT ')' ;
aresta_declaracao_complexa : '(' IDENT direcao IDENT ',' valor ')' ;
direcao : '>' | '<' | '<>' ;

// Comandos
cmd : cmd_add_vertice | cmd_add_aresta | cmd_atribuicao | cmd_imprime | cmd_remove_vertice | cmd_remove_aresta | cmd_outros;
cmd_add_vertice : IDENT '.adiciona_vertice(' vertice ')' ';' ;
cmd_remove_vertice : IDENT '.remove_vertice(' vertice_sem_peso ')' ';' ;
cmd_add_aresta : IDENT '.adiciona_aresta(' aresta ')' ';' ;
cmd_remove_aresta : IDENT '.remove_aresta(' aresta_declaracao_simples ')' ';' ;
cmd_atribuicao : atribuicao_peso
        | atribuicao_criacao_aresta
        | atribuicao_grafo
    ;

cmd_imprime : imprime_estrutura
        | imprime_grafo
    ;
cmd_outros : caminho_mais_curto | imprime_caminho_mais_curto ;

// Atribuicoes
atribuicao_peso : IDENT '.' vertice_ou_aresta_simples '=' valor ';' ;
atribuicao_criacao_aresta : IDENT '.' vertice_sem_peso direcao IDENT '.' vertice_sem_peso ';' ;
atribuicao_grafo : IDENT '=' IDENT ';' ;


// Impressoes
imprime_estrutura : 'imprime_estrutura(' IDENT ')' ';' ;
imprime_grafo : 'imprime_grafo(' IDENT ')' ';' ;

// Outros comandos para grafos
caminho_mais_curto : IDENT '.caminho_mais_curto(' IDENT ',' IDENT ')' ';' ;
imprime_caminho_mais_curto : IDENT '.imprime_caminho_mais_curto(' IDENT ',' IDENT ')' ';' ;

// outros
valor : NUM_INT | NUM_REAL ;