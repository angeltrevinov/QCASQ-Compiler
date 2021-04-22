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
        program     : PROGRAM ID SEMICOLON altprogram
        altprogram  : class altprogram
                    | var altprogram
                    | function altprogram
                    | main
        '''
        # Adding program name to dictionary
        for index, element in enumerate(p):
            if element == ';':
                self.funct_dir.add_to_dictionary(p[index-1])
                #self.funct_dir.get_Dictionary() # printing to see dictionary
        pass

    def p_main(self, p):
        '''
        main    : MAIN OPENPAREN CLOSEPAREN OPENCURLY altmain
        altmain : var altmain
                | estatuto altmain
                | CLOSECURLY
        '''
        # adding main to dictionary
        for element in p:
            if element == 'main':
                self.funct_dir.add_to_dictionary(element)
        pass

    def p_class(self, p):
        '''
        class     : CLASS ID altclass OPENCURLY alt2class
        altclass  : TWODOTS ID
                  | empty
        alt2class : var alt2class
                  | function alt2class
                  | constructor CLOSECURLY SEMICOLON
        '''
        # adding classes
        for index, element in enumerate(p):
            if element == 'class':
                self.funct_dir.add_to_dictionary(p[index + 1])
        pass

    def p_constructor(self, p):
        '''
        constructor : CONSTRUCTOR OPENPAREN altconst CLOSEPAREN OPENCURLY alt2const
        altconst    : params altconst
                    | empty
        alt2const   : var alt2const
                    | estatuto alt2const
                    | CLOSECURLY
        '''
        # adding constructor
        # TODO: breaks when there are 2 or more classes
        for element in p:
            if element == 'constructor':
                self.funct_dir.add_to_dictionary(element)
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
        function : FUNC ID OPENPAREN altfunc CLOSEPAREN alt2func OPENCURLY alt3func
        altfunc  : params
                 | empty
        alt2func : TWODOTS type
                 | empty
        alt3func : var alt3func
                 | estatuto alt3func
                 | CLOSECURLY
        '''
        # Add functions to dictionary
        # TODO: Save type
        for index, element in enumerate(p):
            if element == 'func':
                self.funct_dir.add_to_dictionary(p[index + 1])
                self.funct_dir.get_Dictionary()
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
        for element in p:
            if element is not None:
                print(element)
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
