import ply.yacc as yacc
from QCASQ_Lexer import *
from Function_Dir import *


class QCASQ_Parser:
    __error = False
    tokens = QCASQ_Lexer.tokens

    # initialize function directory
    funct_dir = Function_Dir()

    # Definition of grammatic rules
    def p_program(self, p):
        '''
        program     : PROGRAM ID save_program SEMICOLON altprogram
        altprogram  : class altprogram
                    | var altprogram
                    | function altprogram
                    | main
        '''
        pass

    # Add the program name to the dictionary
    def p_save_program(self, p):
        '''
        save_program :
        '''
        self.funct_dir.add_to_dictionary(p[-1])
        pass

    def p_main(self, p):
        '''
        main    : MAIN save_main OPENPAREN CLOSEPAREN OPENCURLY altmain
        altmain : var altmain
                | estatuto altmain
                | CLOSECURLY
        '''
        pass

    # Add the main to function dictionary
    def p_save_main(self, p):
        '''
        save_main :
        '''
        self.funct_dir.add_to_dictionary(p[-1])
        pass

    def p_class(self, p):
        '''
        class     : CLASS ID altclass save_class OPENCURLY alt2class
        altclass  : TWODOTS ID
                  | empty
        alt2class : var alt2class
                  | function alt2class
                  | constructor CLOSECURLY SEMICOLON
        '''
        # saves the inheritance type of the class
        if p[1] == ":":
            p[0] = p[2]
        pass

    # Add the class and its inheritance to the dictionary
    def p_save_class(self, p):
        '''
        save_class :
        '''
        self.funct_dir.add_to_dictionary(p[-2], p[-1])
        pass

    def p_constructor(self, p):
        '''
        constructor : CONSTRUCTOR save_constructor OPENPAREN altconst CLOSEPAREN OPENCURLY alt2const
        altconst    : params altconst
                    | empty
        alt2const   : var alt2const
                    | estatuto alt2const
                    | CLOSECURLY
        '''
        pass

    # Add the construction to the dictionary
    def p_save_constructor(self, p):
        '''
        save_constructor :
        '''
        self.funct_dir.add_to_dictionary(p[-1])
        pass

    def p_var(self, p):
        '''
        var : VAR listids TWODOTS type SEMICOLON
        '''
        pass

    def p_listids(self, p):
        '''
        listids      : ID listidsalty
        listidsalty : COMMA listids
                    | OPENBRACKET CTEINT CLOSEBRACKET listidsaltz
                    | empty
        listidsaltz : COMMA listids
                    | OPENBRACKET CTEINT CLOSEBRACKET listidsaltp
                    | empty
        listidsaltp : COMMA listids
                    | empty
        '''
        pass

    def p_function(self, p):
        '''
        function : FUNC ID OPENPAREN altfunc CLOSEPAREN alt2func save_function OPENCURLY alt3func
        altfunc  : params
                 | empty
        alt2func : TWODOTS type
                 | empty
        alt3func : var alt3func
                 | estatuto alt3func
                 | CLOSECURLY
        '''
        if p[1] == ":":
            p[0] = p[2]
        if p[1] == "":
            p[0] = ""
        pass

    # Add function name and type to the dictionary
    def p_save_function(self, p):
        '''
        save_function :
        '''
        # Saving function with their type
        self.funct_dir.add_to_dictionary(p[-5], p[-1])
        pass

    def p_params(self, p):
        '''
        params      : ID TWODOTS type altparams
        altparams   : COMMA ID TWODOTS type altparams
                    | empty
        '''
        pass

    def p_callfunc(self, p):
        '''
        callfunc    : ID OPENPAREN altcall CLOSEPAREN
        altcall     : expresion alt2call
                    | empty
        alt2call   : COMMA altcall
                    | empty
        '''
        pass

    def p_type(self, p):
        '''
        type : INT
             | FLOAT
             | STRING
             | ID
             | BOOL
        '''
        p[0] = p[1]
        pass

    def p_estatuto(self, p):
        '''
        estatuto : assign
                | condition
                | write
                | read
                | return
                | voidcall
                | while
        '''
        pass

    def p_voidcall(self, p):
        '''
        voidcall : ID OPENPAREN CLOSEPAREN
                | ID OPENPAREN expresion altcall
        altcall : COMMA expresion altcall
                | CLOSEPAREN SEMICOLON
        '''
        pass

    def p_while(self, p):
        '''
        while    : WHILE OPENPAREN expresion CLOSEPAREN OPENCURLY altwhile
        altwhile : estatuto altwhile
                | CLOSECURLY
        '''
        pass

    def p_varcall(self, p):
        '''
        varcall : varcte
                | varcomplicated
        '''

    def p_varcte(self, p):
        '''
        varcte : TRUE
                | FALSE
              | CTEFLOAT
             | CTESTRING
             | CTEINT
        '''
        pass

    def p_varcomplicated(self, p):
        '''
        varcomplicated : varcomp1
                        | callfunc
        varcomp1        : ID varcomp2
        varcomp2        : DOT varcomp3
                        | empty
        varcomp3        : varcomp1
                        | callfunc
        '''
        pass

    def p_expresion(self, p):
        '''
        expresion       : exp altexpresion
        altexpresion    : altexpresion2 exp
                        | empty
        altexpresion2   : SAMEAS
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
        exp     : termino
                | termino altexp
        altexp  : SUM termino altexp
                | SUBTRACT termino altexp
                | empty
        '''
        pass

    def p_termino(self, p):
        '''
        termino     : factor
                    | factor alttermino
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
        write : OUTPUT OPENPAREN varcall altwrite
                | OUTPUT OPENPAREN expresion altwrite
        altwrite : COMMA varcall altwrite
                | COMMA expresion altwrite
                | CLOSEPAREN SEMICOLON
        '''
        pass

    def p_factor(self, p):
        '''
        factor : OPENPAREN expresion CLOSEPAREN  
                | SUM varcall
                | SUBTRACT varcall
                | varcall
        '''
        pass

    def p_condition(self, p):
        '''
        condition : IF OPENPAREN expresion CLOSEPAREN OPENCURLY altcondition
                    | IF OPENPAREN expresion CLOSEPAREN  OPENCURLY  altcondition ELSE OPENCURLY altcondition
        altcondition : estatuto altcondition
                    | CLOSECURLY
        '''
        pass

    def p_assign(self, p):
        '''
        assign : ID assign1 EQUALS expresion SEMICOLON
        assign1 : DOT ID assign1
                | empty
        '''
        pass

    def p_return(self, p):
        '''
        return  : RETURN expresion SEMICOLON
        '''
        pass

    def p_empty(self, p):
        '''
        empty :
        '''
        p[0] = ""
        pass

    def p_error(self, p):
        self.__error = True
        print('\n gramatica no apropiada', p)

    # constructor
    def __init__(self, lexer):

        self.parser = yacc.yacc(module=self, debug=True)  # To use debug add debug = True
        self.lexer = lexer

    def get_error(self):
        return self.__error
