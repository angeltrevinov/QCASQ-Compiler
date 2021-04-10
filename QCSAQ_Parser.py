import ply.yacc as yacc
from QCASQ_Lexer import *

class QCASQ_Parser:
    __error = False
    tokens = QCASQ_Lexer.tokens

    # Definition of grammatic rules
    def p_program(self, p):
        '''
        program : PROGRAM ID SEMICOLON altprogram
        '''
        pass

    def p_altprogram(self, p):
        '''
        altprogram : class altprogram
                   | var altprogram
                   | function altprogram
                   | main
        '''
        pass

    def p_main(self, p):
        '''
        main : MAIN OPENPAREN CLOSEPAREN OPENCURLY altmain
        '''
        pass

    def p_altmain(self, p):
        '''
        altmain : estatuto altmain
                | CLOSECURLY
        '''
        pass

    def p_class(self, p):
        '''
        class : CLASS ID altclass OPENCURLY alt2class
        '''
        pass

    def p_altclass(self, p):
        '''
        altclass : TWODOTS ID
                 | empty
        '''
        pass

    def p_alt2class(self, p):
        '''
        alt2class : var alt2class
                  | function alt2class
                  | constructor CLOSECURLY SEMICOLON
        '''
        pass

    def p_constructor(self, p):
        '''
        constructor : CONSTRUCTOR OPENPAREN altconst CLOSEPAREN OPENCURLY alt2const
        '''
        pass

    def p_altconst(self, p):
        '''
        altconst : params altconst
                 | empty
        '''
        pass

    def p_alt2const(self, p):
        '''
        alt2const : estatuto alt2const
                 | CLOSECURLY
        '''
        pass

    def p_var(self, p):
        '''
        var : VAR listids TWODOTS type SEMICOLON
        '''
        pass

    def p_listids(self, p):
        '''
        listids : ID listidsalty
        '''
        pass

    def p_listidsalty(self, p):
        '''
        listidsalty : COMMA listids
                    | OPENBRACKET INT CLOSEBRACKET listidsaltz
                    | empty
        '''
        pass

    def p_listidsaltz(self, p):
        '''
        listidsaltz : COMMA listids
                    | OPENBRACKET INT CLOSEBRACKET listidsaltp
                    | empty
        '''
        pass

    def p_listidsaltp(self, p):
        '''
        listidsaltp : COMMA listids
                    | empty
        '''
        pass

    def p_function(self, p):
        '''
        function : FUNC ID OPENPAREN altfunc CLOSEPAREN alt2func OPENCURLY alt3func
        '''
        pass

    def p_altfunc(self, p):
        '''
        altfunc : params
                | empty
        '''
        pass

    def p_alt2func(self, p):
        '''
        alt2func : TWODOTS type
                 | empty
        '''
        pass

    def p_alt3func(self, p):
        '''
        alt3func : var alt3func
                 | estatuto alt3func
                 | CLOSECURLY
        '''
        pass

    def p_params(self, p):
        '''
        params : ID TWODOTS type altparams
        '''
        pass

    def p_altparams(self, p):
        '''
        altparams : COMMA ID TWODOTS type altparams
                | empty
        '''
        pass

    def p_callfunc(self, p):
        '''
        callfunc : ID OPENPAREN altcall
        '''
        pass

    def p_altcall(self, p):
        '''
        altcall : varcte alt2call 
                | CLOSEPAREN
        '''
        pass

    def p_alt2call(self, p):
        '''
        alt2call : COMMA varcte alt2call
                 | CLOSEPAREN
        '''
        pass

    def p_type(self, p):
        '''
        type : INT
             | FLOAT
             | STRING
             | ID
        '''
        pass

    def p_estatuto(self, p):
        '''
        estatuto : assign
                | condition
                | write
                | read
        '''
        pass

    def p_varcte(self, p):
        '''
        varcte : ID
              | CTEFLOAT
             | CTESTRING
             | CTEINT
        '''
        pass

    def p_expresion(self, p):
        '''
        expresion : exp altexpresion exp
        '''
        pass

    def p_altexpresion(self, p):
        '''
        altexpresion : SAMEAS
                    | BIGGERTHAN
                    | BIGGEREQUALSTHAN
                    | SMALLTHAN
                    | SMALLEQUALSTHAN
                    | DIFFERENTTHAN
                    | AND
                    | OR
        '''
        pass

    def p_exp(self, p):
        '''
        exp : termino 
            | termino altexp
        '''
        pass

    def p_altexp(self, p):
        '''
        altexp  : SUM termino altexp
                | SUBTRACT termino altexp
                | empty
        '''
        pass

    def p_termino(self, p):
        '''
        termino : factor 
                | factor alttermino
        '''
        pass

    def p_alttermino(self, p):
        '''
        alttermino : TIMES factor alttermino
                    | DIV factor alttermino
                    | empty
        '''
        pass

    def p_read(self, p):
        '''
        read : INPUT OPENPAREN ID CLOSEPAREN SEMICOLON
        '''
        pass

    def p_write(self, p):
        '''
        write : OUTPUT OPENPAREN varcte altwrite
                | OUTPUT OPENPAREN expresion altwrite
        '''
        pass

    def p_altwrite(self, p):
        '''
        altwrite : COMMA varcte altwrite
                | COMMA expresion altwrite
                | CLOSEPAREN SEMICOLON
        '''
        pass

    def p_factor(self, p):
        '''
        factor : OPENPAREN expresion CLOSEPAREN  
                | SUM varcte
                | SUBTRACT varcte
                | varcte
        '''
        pass

    def p_condition(self, p):
        '''
        condition : IF OPENPAREN expresion CLOSEPAREN OPENCURLY altcondition
                    | IF OPENPAREN expresion CLOSEPAREN  OPENCURLY  altcondition ELSE OPENCURLY altcondition
        '''
        pass

    def p_altcondition(self, p):
        '''
        altcondition : estatuto altcondition
                    | CLOSECURLY
        '''
        pass

    def p_assign(self, p):
        '''
        assign : ID EQUALS expresion SEMICOLON 
                | ID EQUALS expresion altassign
        '''
        pass

    def p_altassign(self, p):
        '''
        altassign : callfunc altassign
                    | exp altassign 
                    | exp varcte altassign
                    | SEMICOLON
        '''
        pass

    def p_empty(self, p):
        '''
        empty :
        '''
        pass

    def p_error(self, p):
        self.__error = True
        print('\n gramatica no apropiada \n')

    # constructor
    def __init__(self, lexer):
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer

    def get_error(self):
        return self.__error