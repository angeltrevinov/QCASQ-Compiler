import sys
import ply.yacc as yacc
from LexYacc.QCASQ_Lexer import QCASQ_Lexer
from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.QuadruplesManager import QuadrupleManager


class QCASQ_Parser:
    __error = False
    __stack_vars = []  # this is to store if multiple vars came as a list, so we can also add their type
    __stack_params = []  # to save the params in their corresponding function directory
    tokens = QCASQ_Lexer.tokens

    # initialize function director
    funct_dir = Function_Dir()
    quads = QuadrupleManager()

    # --------- Definition of grammatical rules ------------
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
        ''' save_program : '''
        self.funct_dir.add_to_dictionary(p[-1])
        self.funct_dir.add_to_scope(p[-1])
        pass

    def p_main(self, p):
        '''
        main    : MAIN save_main OPENPAREN CLOSEPAREN OPENCURLY altmain
        altmain : var altmain
                | estatuto altmain
                | CLOSECURLY clear_scope
        '''
        pass

    # Add the main to function dictionary
    def p_save_main(self, p):
        ''' save_main : '''
        self.funct_dir.add_to_dictionary(p[-1])
        self.funct_dir.add_to_scope(p[-1])
        pass

    # remove main and program from scope (finish reading the file)
    def p_clear_scope(self, p):
        ''' clear_scope : '''
        self.funct_dir.pop_scope()
        self.funct_dir.pop_scope()
        pass

    def p_class(self, p):
        '''
        class     : CLASS ID altclass save_class OPENCURLY alt2class
        altclass  : TWODOTS ID
                  | empty
        alt2class : var alt2class
                  | function alt2class
                  | constructor CLOSECURLY SEMICOLON remove_class_scope
        '''
        # saves the inheritance type of the class
        if p[1] == ":":
            p[0] = p[2]
        pass

    # Add the class and its inheritance to the dictionary
    def p_save_class(self, p):
        ''' save_class : '''
        self.funct_dir.add_to_dictionary(p[-2], p[-1])
        self.funct_dir.add_to_scope(p[-2])
        pass

    # Removes the class from the scope
    def p_remove_class_scope(self, p):
        ''' remove_class_scope : '''
        self.funct_dir.pop_scope()
        pass

    def p_constructor(self, p):
        '''
        constructor : CONSTRUCTOR save_constructor OPENPAREN altconst add_params_const CLOSEPAREN OPENCURLY alt2const
        altconst    : params
                    | empty
        alt2const   : var alt2const
                    | estatuto alt2const
                    | CLOSECURLY remove_constructor_scope
        '''
        pass

    # Add the construction to the dictionary
    def p_save_constructor(self, p):
        ''' save_constructor : '''
        self.funct_dir.add_to_dictionary(p[-1])
        self.funct_dir.add_to_scope(p[-1])
        pass

    def p_add_params_const(self, p):
        '''add_params_const : '''
        for param in self.__stack_params:
            name, type = param
            self.funct_dir.get_function(
                self.funct_dir.get_current_scope()
            )["tablevars"].add_to_dictionary(name, type)
        self.__stack_params.clear()
        pass

    def p_remove_constructor_scope(self, p):
        ''' remove_constructor_scope : '''
        self.funct_dir.pop_scope()
        pass

    def p_var(self, p):
        '''
        var : VAR listids TWODOTS type save_vars SEMICOLON
        '''
        pass

    def p_save_vars(self, p):
        '''
        save_vars :
        '''
        for element in self.__stack_vars:
            self.funct_dir.get_function(
                self.funct_dir.get_current_scope()
            )["tablevars"].add_to_dictionary(element, p[-1])
        self.__stack_vars.clear()
        pass

    def p_listids(self, p):
        '''
        listids      : ID save_var_name listidsalty
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

    def p_save_var_name(self, p):
        '''
        save_var_name :
        '''
        self.__stack_vars.append(p[-1])
        pass

    def p_function(self, p):
        '''
        function : FUNC ID OPENPAREN altfunc  CLOSEPAREN alt2func save_function OPENCURLY alt3func
        altfunc  : params
                 | empty
        alt2func : TWODOTS type
                 | empty
        alt3func : var alt3func
                 | estatuto alt3func
                 | CLOSECURLY remove_function_scope
        '''
        if p[1] == ":":
            p[0] = p[2]
        if p[1] == "":
            p[0] = ""
        pass

    # Add function name and type to the dictionary
    def p_save_function(self, p):
        ''' save_function : '''
        # Saving function with their type
        self.funct_dir.add_to_dictionary(p[-5], p[-1])
        self.funct_dir.add_to_scope(p[-5])
        for param in self.__stack_params:
            name, type = param
            self.funct_dir.get_function(
                self.funct_dir.get_current_scope()
            )["tablevars"].add_to_dictionary(name, type)
        self.__stack_params.clear()
        pass

    def p_remove_function_scope(self, p):
        ''' remove_function_scope : '''
        self.funct_dir.pop_scope()
        pass

    def p_params(self, p):
        '''
        params      : ID TWODOTS type save_params altparams
        altparams   : COMMA ID TWODOTS type save_params altparams
                    | empty
        '''
        pass

    def p_save_params(self, p):
        '''
        save_params :
        '''
        self.__stack_params.append((p[-3], p[-1]))
        pass

    def p_callfunc(self, p):
        '''
        callfunc    : ID OPENPAREN altcall CLOSEPAREN
        altcall     : expresion alt2call
                    | empty
        alt2call   : COMMA altcall
                    | empty
        '''
        if p[1] is not None:
            # TODO: Fix this so we know is a method
            #p[0] = p[1]
            p[0] = None
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
        p[0] = p[1]
        pass

    def p_varcte(self, p):
        '''
        varcte : TRUE
                | FALSE
                | CTEFLOAT
                | CTESTRING
                | CTEINT
        '''
        p[0] = p[1]
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
        if p[1] is not None:
            p[0] = p[1]
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
                | varcall save_operand
        '''
        pass

    def p_save_operand(self, p):
        '''
        save_operand :
        '''
        var_found = False
        index = len(self.funct_dir.get_scope()) - 1
        while index >= 0 and var_found is False:
            scope = self.funct_dir.get_scope()[index]
            vars_table = self.funct_dir.get_function(scope)['tablevars']
            # Found None, which means there is a function call here
            if p[-1] is None:
                var_found = True
                print("found function")
            # save variables if they exists
            elif p[-1] in vars_table.get_dictionary():
                var_found = True
                vars = vars_table.get_variable(p[-1])
                self.quads.add_operand(p[-1], vars["type"])
            # Save constants that are not strings
            elif not isinstance(p[-1], str):
                var_found = True
                self.quads.add_operand(p[-1], type(p[-1]).__name__)
            # Save constant strings
            elif isinstance(p[-1], str) and p[-1][0] == '"':
                var_found = True
                self.quads.add_operand(p[-1], "string")
            # Save booleans
            elif isinstance(p[-1], str) and (p[-1] == 'false' or p[-1] == 'true'):
                var_found = True
                self.quads.add_operand(p[-1], "bool")
            else:
                index = index - 1

        if index < 0 and var_found is False:
            sys.exit(f"ERROR: couldn't find declaration of variable {p[-1]} in line {p.lineno(-1)}")
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

    # To detect if there is an error
    def p_error(self, p):
        self.__error = True
        print('\n gramatica no apropiada', p)

    def __init__(self, lexer):
        """The constructor of the parser

        :param lexer: The lexer object to use for our parser
        """
        self.parser = yacc.yacc(module=self, debug=True)  # To use debug add debug = True
        self.lexer = lexer

    def get_error(self) -> bool:
        """
        :return: if there is an error when parsing
        :rtype: bool
        """
        return self.__error
