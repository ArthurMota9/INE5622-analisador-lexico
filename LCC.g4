grammar LCC;

start : (statement | funclist)?;

funclist : funcdef (funcdef | funclist);

funcdef : DEF IDENT openParantheses paramlist closeParantheses openBraces statelist closeBraces;

paramlist : (types IDENT comma paramlist | types IDENT)?;

statement : (
    vardecl semicolon |
    atribstat semicolon |
    printstat semicolon |
    readstat semicolon |
    returnstat semicolon |
    ifstat |
    forstat |
    openBraces statelist closeBraces |
    BREAK semicolon |
    semicolon
);

vardecl : types IDENT(openBrackets INT_CONSTANT closeBrackets)*?;

atribstat : lvalue assignment (expression | allocexpression | funccall);

funccall : IDENT openParantheses paramlistcall closeParantheses;

paramlistcall : (IDENT comma paramlistcall | IDENT)?;

printstat : PRINT expression;

readstat : READ lvalue;

returnstat : RETURN;

ifstat : IF openParantheses expression closeParantheses statement (ELSE statement)?;

forstat : FOR openParantheses atribstat semicolon expression semicolon atribstat closeParantheses statement;

statelist : statement (statelist)?;

allocexpression : NEW types (openBrackets numexpression closeBrackets)+;

expression : numexpression ((lessThan | greatherThan | lessThanOrEqual | greatherThanOrEqual | equal | different) numexpression)?;

numexpression : term ((plus | minus) term)*? ; 

term : unaryexpr ((multiply | divide | percent) unaryexpr)*?;

unaryexpr : ((plus | minus))? factor;

factor : (INT_CONSTANT | FLOAT_CONSTANT | STRING_CONSTANT | NULL | lvalue | openParantheses numexpression closeParantheses);

lvalue : IDENT(openBrackets numexpression closeBrackets)*?;

types : INT | FLOAT | STRING;

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
openParantheses: '(';
closeParantheses: ')';
openBraces: '{';
closeBraces: '}';
openBrackets: '[';
closeBrackets: ']';
comma: ',';
semicolon: ';';
assignment: '=';
plus: '+';
minus: '-';
multiply: '*';
divide: '/';
percent: '%';
NULL: 'null';
lessThan: '<';
greatherThan: '>';
lessThanOrEqual: '<=';
greatherThanOrEqual: '>=';
equal: '==';
different: '!=';

// Regex
IDENT : [a-zA-Z][a-zA-Z0-9]*;
INT_CONSTANT : '-'?[0-9]+;
FLOAT_CONSTANT: '-'?[0-9]*.?[0-9]+;
STRING_CONSTANT : [a-zA-Z][a-zA-Z0-9]*;
WS : [ \r\n\t]+ -> skip;