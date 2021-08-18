grammar LCC;

start: (statement | funclist)?;

funclist: funcdef (funcdef | funclist);

funcdef: DEF IDENT OPEN_PAREN paramlist CLOSE_PAREN OPEN_BRACE statelist CLOSE_BRACE;

paramlist: (types IDENT COMMA paramlist | types IDENT)?;

statement: (
    ((vardecl | atribstat | printstat | readstat | returnstat) SEMI_COLON) |
    ifstat |
    forstat |
    OPEN_BRACE statelist CLOSE_BRACE |
    BREAK SEMI_COLON |
    SEMI_COLON
);

vardecl: types IDENT (OPEN_BRACK INT CLOSE_BRACK)*;

atribstat : lvalue ASSIGN (expression | allocexpression | funccall);

funccall: IDENT OPEN_PAREN paramlistcall CLOSE_PAREN;

paramlistcall: (IDENT COMMA paramlistcall | IDENT)?;

printstat: PRINT expression;

readstat: READ lvalue;

returnstat: RETURN;

ifstat: IF OPEN_PAREN expression CLOSE_PAREN statement (ELSE statement)?;

forstat: FOR OPEN_PAREN atribstat SEMI_COLON expression SEMI_COLON atribstat CLOSE_PAREN statement;

statelist: statement (statelist)?;

allocexpression: NEW types (OPEN_BRACK numexpression CLOSE_BRACK)+;

expression: numexpression ((LESS_THAN | GREATHER_THAN | LESS_THAN_OR_EQUAL | GREATHER_THAN_OR_EQUAL | EQUALS | DIFFERENT) numexpression)?;

numexpression: term ((PLUS | MINUS) term)*; 

term: unaryexpr ((MULTIPLY | DIVIDE | MOD) unaryexpr)*;

unaryexpr: ((PLUS | MINUS))? factor;

factor: (INT_CONSTANT | FLOAT_CONSTANT | STRING_CONSTANT | NULL | lvalue | OPEN_PAREN numexpression CLOSE_PAREN);

lvalue: IDENT(OPEN_BRACK INT CLOSE_BRACK)*;

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
NULL: 'NULL';
LESS_THAN: '<';
GREATHER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATHER_THAN_OR_EQUAL: '>=';
EQUALS: '==';
DIFFERENT: '!=';

// Regex
IDENT : [a-zA-Z][a-zA-Z0-9]*;
INT_CONSTANT : [0-9]+;
FLOAT_CONSTANT: '-'?[0-9]*.?[0-9]+;
STRING_CONSTANT : [a-zA-Z][a-zA-Z0-9]*;
WS : [ \r\n\t]+ -> skip;