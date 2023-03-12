grammar MT22;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options{
	language=Python3;
}

program:  (var_decl SEMI | func_decl)+ EOF ;

var_decl: (ID COMMA var_decl COMMA expr) 
			| ID COLON arr_type list_type EQ expr
			| ID (COMMA ID)* COLON arr_type list_type
			| ID EQ expr;
arr_type: (ARRAY LSB INT_LIT (COMMA INT_LIT)* RSB OF)?;
list_type: INT | FLOAT | STR | BOOLEAN | AUTO | VOID;

para: INHERIT? OUT? ID COLON arr_type list_type;
para_list: (para (COMMA para)*)?;
func_decl: ID COLON FUNC arr_type list_type LB para_list RB (INHERIT ID)? block_stmt;
func_call: ID LB expr_list? RB;

stmt: LB expr RB ? ';'
   | if_stmt 
	| for_stmt 
	| while_stmt 
	| do_while_stmt 
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt
	| block_stmt
	| expr SEMI;
block_stmt: LCB (stmt | var_decl SEMI)* RCB;
if_stmt: IF LB expr RB stmt (ELSE stmt)?;
for_stmt: FOR LB ((ID| id_arr) EQ expr) (COMMA expr) (COMMA expr) RB stmt
         |FOR LB (expr)? COMMA expr (COMMA expr)  RB stmt;
while_stmt: WHILE expr stmt?;
do_while_stmt: DO block_stmt WHILE LB expr RB SEMI;
break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;
return_stmt: RETURN SEMI
			| RETURN expr SEMI;
call_stmt: func_call SEMI;


/********************* BEGIN EXPRESSIONS ***********************/
expr_list: expr (COMMA expr)*;
expr: relation_expr '::' relation_expr | relation_expr;
relation_expr: logic_expr (EQEQ | NOTEQ | LT | GT | LTEQ | GTEQ) logic_expr | logic_expr;
logic_expr: logic_expr (AND | OR) add_expr | add_expr;
add_expr: add_expr (ADD | SUB) mul_expr | mul_expr;
mul_expr: mul_expr (MUL | DIV | MOD) not_expr | not_expr;
not_expr: NOT not_expr | sign_expr;
sign_expr: SUB sign_expr | exp8;
exp8: exp9 LSB expr RSB | exp9;
exp9: LB expr RB | operand;
operand: INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT | ID | array | var_decl | func_call | index_operators;
index_operators: ID LSB expr_list RSB ;

/********************* END EXPRESSIONS ***********************/

/********************* LITERALS **********************/
fragment CHARLIT: ~[\b\t\f\r\n"\\] | ESCAPE_SEQUENCE;
fragment DECPART: '.' [0-9]*;
fragment DIGIT: [0-9];
fragment DoubleQuote: '"';
fragment ESCAPE_SEQUENCE: '\\' [bfrnt"\\];
fragment EXPPART: [eE][+-]? [0-9]+;
fragment NonDigit: [a-zA-Z_];
fragment NonZDigit: [1-9];

INT_LIT: ( (NonZDigit DIGIT*) ('_'? DIGIT)* | '0' )
	{
		self.text = self.text.replace("_","")
	};

FLOAT_LIT:( INT_LIT DECPART 
		| INT_LIT DECPART? EXPPART
		| DECPART EXPPART )
	{self.text = self.text.replace("_","")};

BOOL_LIT: TRUE | FALSE;

STRING_LIT: DoubleQuote CHARLIT* DoubleQuote
	{
		self.text = self.text[1:-1]
	}; 

array: LCB literal_element RCB;
literal_element: (literal (COMMA literal)*?)?;
literal: expr | array;

/********************** TYPES  ************************/
BOOL: 'bool';
/******************** SEPARATORS **********************/
LB: '(' ;
RB: ')' ;
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LCB: '{';
RCB: '}';

/********************* KEYWORDS **********************/
ARRAY: 'array';
AUTO: 'auto';
BOOLEAN: 'boolean';
BREAK: 'break';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNC: 'function';
IF: 'if';
INHERIT: 'inherit';
INT: 'integer';
OF: 'of';
OUT: 'out';
RETURN: 'return';
STR: 'string';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';

/******************** IDENTIFIERS **********************/
ID: [a-zA-Z_][a-zA-Z0-9_]*;
id_arr: ID (LSB (INT_LIT | ID) (COMMA (INT_LIT | ID))* RSB)+;
/********************* OPERATORS **********************/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '=';
NOTEQ: '!=';
LT: '<';
LTEQ: '<=';
GT: '>';
GTEQ: '>=';
COLONCOLON: '::';
EQEQ: '==';

/********************* COMMENTS ***********************/
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
BlockComment: '/*' .*? '*/' -> skip;
LINE_CMT: ('/'  ~[\r\n]*) -> skip;

UNCLOSE_STRING: '"' CHARLIT* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};


ILLEGAL_ESCAPE: '"' CHARLIT* ('\\' ~([bfnrt\\] | '\''))
{self.text = self.text.replace('"','',1)};
ERROR_CHAR: (. | '0' DIGIT+) {raise ErrorToken(self.text)};
