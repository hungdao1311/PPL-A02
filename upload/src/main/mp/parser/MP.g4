grammar MP;
//ID : 1611384 - Dao Manh Hung
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program : decl+ EOF;

decl : var_dec | func_dec | procedure_dec;

var_dec : VAR var_dec_list SM; //variable declaration

var_dec_list : one_var_dec SM var_dec_list
             | one_var_dec;

one_var_dec: id_list COLON main_type;

id_list : ID CM id_list
        | ID;


main_type : (primitive_type | array_dec);

primitive_type : (BOOLEAN | INTEGER | REAL | STRING);

array_dec : ARRAY LSB array_bound DOTDOT array_bound RSB OF primitive_type;

array_bound: MINUS? INT_LIT;

func_dec : FUNCTION ID LB var_dec_list? RB COLON main_type SM var_dec? compound_stmt; //function declaration

procedure_dec : PROCEDURE ID LB var_dec_list? RB SM var_dec? compound_stmt
              ;//procedure declaration

exp_element : (STRING_LIT | INT_LIT | FLOAT_LIT | BOOL_LIT | ID | invo_exp | index_exp);

invo_exp : ID LB exp_list? RB;

index_exp : (STRING_LIT | INT_LIT | FLOAT_LIT | BOOL_LIT | ID | invo_exp | LB exp RB) (LSB exp RSB)
          | index_exp LSB exp RSB;

exp_list : exp CM exp_list
         | exp;

exp : exp (ANDTHEN | ORELSE) exp1
    | exp1;

exp1: exp2 ( EQUAL | NOT_EQUAL | LT | LE | GT | GE) exp2
    | exp2;

exp2: exp2 (PLUS | MINUS | OR) exp3
    | exp3;

exp3: exp3 (DIVIDE | MULTIPLE | DIV | MOD | AND) exp4
    | exp4;

exp4: (NOT | MINUS) exp4
    | exp5;

exp5: exp_element
    | LB exp RB;

stmt : (assign_stmt | if_stmt | while_stmt | return_stmt | for_stmt | break_stmt | continue_stmt                  //statements
     | compound_stmt | with_stmt | call_stmt );

assign_stmt : lhs ASSIGN assign_stmt1;

lhs : ID | index_exp ;

assign_stmt1 : exp SM
             | assign_stmt;

if_stmt : IF exp THEN stmt (ELSE stmt)?;

while_stmt : WHILE exp DO stmt;

for_stmt : FOR ID ASSIGN exp (TO | DOWNTO) exp DO stmt;

break_stmt : BREAK SM;

continue_stmt : CONTINUE SM;

return_stmt : RETURN exp? SM;

compound_stmt : BEGIN stmt_list END;

stmt_list : stmt stmt_list
          |;

with_stmt : WITH var_dec_list SM DO stmt;

call_stmt : ID LB exp_list? RB SM;

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

ANDTHEN: A N D ' ' T H E N;

ORELSE: O R ' ' E L S E;

WITH: W I T H;

BOOL_LIT: TRUE | FALSE;

BREAK: B R E A K;

CONTINUE: C O N T I N U E;

FOR: F O R;

TO: T O;

DOWNTO: D O W N T O;

DO: D O;

IF: I F;

THEN: T H E N;

ELSE: E L S E;

RETURN: R E T U R N;

WHILE: W H I L E;

BEGIN: B E G I N;

END: E N D;

FUNCTION: F U N C T I O N;

PROCEDURE: P R O C E D U R E;

VAR: V A R;

TRUE: T R U E;

FALSE: F A L S E;

ARRAY: A R R A Y;

OF: O F;

REAL: R E A L;

BOOLEAN: B O O L E A N;

INTEGER: I N T E G E R;

STRING: S T R I N G;

NOT: N O T;

AND: A N D;

OR: O R;

DIV: D I V;

MOD: M O D;

PLUS: '+';

MINUS: '-';

DIVIDE: '/';

MULTIPLE: '*';

NOT_EQUAL: '<>';

LT: '<';

LE: '<=';

EQUAL: '=';

GT: '>';

GE: '>=';

LB: '(';

RB: ')';

LSB: '[';

RSB: ']';

SM: ';';

DOTDOT: '..';

COLON: ':';

ASSIGN: COLON EQUAL;

CM: ',';

STRING_LIT: '"' (STRING_CHAR)* '"' {self.text = self.text[1:-1]};

ILLEGAL_ESCAPE: '"' STRING_CHAR* '\\'~[bfrnt'"\\] {raise IllegalEscape(self.text[1:])};

UNCLOSED_STRING: '"'STRING_CHAR* {raise UncloseString(self.text[1:])};

ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS : [ \t\r\n]+ -> skip ;

COMMENT_1: '(*' (.)*? '*)' -> skip;

COMMENT_2: '{' (.)*? '}' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

fragment DIGIT: [0-9];

fragment EXPONENT: E (MINUS)?DIGIT+;

fragment STRING_CHAR: (~["\\\r\n] | ESCAPE_SEQUENCES) ;

fragment ESCAPE_SEQUENCES: '\\'[bfrnt'"\\];

INT_LIT: DIGIT+;

FLOAT_LIT: DIGIT+('.'DIGIT* (EXPONENT)?|EXPONENT)
         | '.'DIGIT+ (EXPONENT)?;



ERROR_CHAR: . {raise ErrorToken(self.text)};

