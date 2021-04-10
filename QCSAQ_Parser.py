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