grammar LCC;

start: (statement | funclist)? EOF;

funclist: funcdef (funcdef | funclist);

funcdef: DEF IDENT '(' paramlist ')' '{' statelist '}';

paramlist: (types IDENT ',' paramlist | types IDENT)?;

statement:
    vardecl ';' | 
    atribstat ';' | 
    printstat ';' | 
    readstat ';' | 
    returnstat ';' |
    ifstat |
    forstat |
    '{' statelist '}' |
    BREAK ';' |
    ';'
;

vardecl: types IDENT '['INT_CONSTANT']' | types IDENT;

atribstat : lvalue '=' (expression | allocexpression | funccall);

funccall: IDENT '(' paramlistcall ')';

paramlistcall: (IDENT ',' paramlistcall | IDENT)?;

printstat: PRINT expression;

readstat: READ lvalue;

returnstat: RETURN;

ifstat: IF '(' expression ')' statement (ELSE statement)?;

forstat: FOR '(' atribstat ';' expression ';' atribstat ')' statement;

statelist: statement (statelist)?;

allocexpression: NEW types ('[' numexpression ']')+;

expression: numexpression (('<' | '>' | '<=' | '>=' | '==' | '!=') numexpression)?;

numexpression: term (('+' | '-') term)*; 

term: unaryexpr (('*' | '/' | '%') unaryexpr)*;

unaryexpr: (('+' | '-'))? factor;

factor: (INT_CONSTANT | FLOAT_CONSTANT | STRING_CONSTANT | NULL | lvalue | '(' numexpression ')');

lvalue: IDENT '['INT_CONSTANT']' | IDENT;

types: INT | FLOAT | STRING;

// Tokens
DEF: 'def';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
BREAK: 'break';
PRINT: 'print';
READ: 'read';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
FOR: 'for';
NEW: 'new';
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
COMMA: ',';
SEMI_COLON : ';';
ASSIGN : '=';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MOD: '%';
NULL: 'null';
LESS_THAN: '<';
GREATHER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATHER_THAN_OR_EQUAL: '>=';
EQUALS: '==';
DIFFERENT: '!=';

// Regex
IDENT : [a-zA-Z][a-zA-Z0-9]*;
INT_CONSTANT : [0-9]+;
FLOAT_CONSTANT: [0-9]*.?[0-9]+;
STRING_CONSTANT : [a-zA-Z][a-zA-Z0-9]*;
WS : [ \r\n\t]+ -> skip;