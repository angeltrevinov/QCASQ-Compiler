import sys
import ply.yacc as yacc
from LexYacc.QCASQ_Lexer import QCASQ_Lexer
from GenerateCode.Class_Dir import Class_Dir
from GenerateCode.Function_Dir import Function_Dir
from GenerateCode.Variables_Dir import Variables_Dir
from GenerateCode.QuadruplesManager import QuadrupleManager
from VirtualMachine.Limits import Limits
from GenerateCode.CteTable import CteTable


class QCASQ_Parser:
    __error = False
    __stack_vars = []  # this is to store if multiple vars came as a list, so we can also add their type
    __stack_params = []  # to save the params in their corresponding function directory
    tokens = QCASQ_Lexer.tokens

    # initialize function director
    class_dir = Class_Dir()
    quads = QuadrupleManager()
    limits = Limits()
    ctes = CteTable()

    # --------- Definition of grammatical rules ------------
    def p_program(self, p):
        '''
        program     : PROGRAM ID save_program SEMICOLON altprogram
        altprogram  : class altprogram
                    | var altprogram
                    | function altprogram
                    | main remove_class_scope
        '''
        pass

    # Add the program name to the dictionary
    def p_save_program(self, p):
        ''' save_program : '''
        self.class_dir.add_to_dictionary(p[-1])
        self.class_dir.add_to_scope(p[-1])
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
        ''' save_main : '''
        # adds main to the function directory of the program
        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_dictionary(p[-1])
        # sets the scope as main for the program class
        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_scope(p[-1])
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
        self.class_dir.add_to_dictionary(p[-2], p[-1])
        self.class_dir.add_to_scope(p[-2])
        pass

    # Removes the class from the scope
    def p_remove_class_scope(self, p):
        ''' remove_class_scope : '''
        self.class_dir.pop_scope()
        pass

    def p_constructor(self, p):
        '''
        constructor : CONSTRUCTOR save_constructor OPENPAREN altconst store_params CLOSEPAREN OPENCURLY alt2const
        altconst    : params
                    | empty
        alt2const   : var alt2const
                    | estatuto alt2const
                    | CLOSECURLY
        '''
        pass

    # Add the construction to the dictionary
    def p_save_constructor(self, p):
        ''' save_constructor : '''
        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_dictionary(p[-1])

        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_scope(p[-1])
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
        class_func_scope_length = len(self.class_dir.get_class(self.class_dir.get_current_scope())["function_dir"].get_scope())
        class_scope = self.class_dir.get_current_scope()
        for element in self.__stack_vars:
            # Global variables for that class
            if class_func_scope_length == 0:
                if len(self.class_dir.get_scope()) == 1:
                    tipo = p[-1] + "G"
                    address = self.limits.getAddress(tipo) + self.limits.getCont(tipo)
                    self.class_dir.get_class(class_scope)["tablevars"].add_to_dictionary(element, p[-1], address)
                    self.limits.upCont(tipo)
                else:
                    self.class_dir.get_class(class_scope)["tablevars"].add_to_dictionary(element, p[-1], 0)
            else:
                # local variables for a class
                func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
                tipo = p[-1] + "L"
                address = self.limits.getAddress(tipo) + self.limits.getCont(tipo)
                self.class_dir.get_class(
                    class_scope
                )["function_dir"].get_function(
                    func_scope
                )["tablevars"].add_to_dictionary(element, p[-1],address)
                self.limits.upCont(tipo)

        self.__stack_vars.clear()
        pass

    def p_listids(self, p):
        '''
        listids      : ID save_var_name array listidsalty
        listidsalty : COMMA listids
                    | empty
        '''
        pass

    def p_array(self, p):
        '''
        array : OPENBRACKET expresion CLOSEBRACKET empty_pv array2
                | empty
        array2 : OPENBRACKET expresion CLOSEBRACKET empty_pv
              | empty
        '''

    def p_save_var_name(self, p):
        '''
        save_var_name :
        '''
        self.__stack_vars.append(p[-1])
        pass

    def p_function(self, p):
        '''
        function : FUNC ID OPENPAREN altfunc  CLOSEPAREN alt2func save_function store_params OPENCURLY alt3func
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
        class_scope = self.class_dir.get_current_scope()
        self.class_dir.get_class(class_scope)["function_dir"].add_to_dictionary(p[-5], p[-1])
        self.class_dir.get_class(class_scope)["function_dir"].add_to_scope(p[-5])
        pass

    def p_store_params(self, p):
        '''store_params : '''
        class_scope = self.class_dir.get_current_scope()
        func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
        for param in self.__stack_params:
            name, type = param
            address = self.limits.getAddress(type + "L") + self.limits.getCont(type + "L")
            self.class_dir.get_class(
                class_scope
            )["function_dir"].get_function(
                func_scope
            )["params"].add_to_dictionary(name, type, address)
            self.limits.upCont(type + "L")
        self.__stack_params.clear()

    def p_remove_function_scope(self, p):
        ''' remove_function_scope : '''
        class_scope = self.class_dir.get_current_scope()
        self.class_dir.get_class(class_scope)["function_dir"].pop_scope()
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
        estatuto : assign empty_pv
                | condition empty_pv
                | write empty_pv
                | read empty_pv
                | return empty_pv
                | voidcall empty_pv
                | while empty_pv
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

    def p_empty_pv(self, p):
        ''' empty_pv : '''
        self.quads.empty_polish_vector()
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
        varcall : varcte save_const
                | varcomplicated save_comp
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
        # TODO: doesn't know id.func() id.id
        if p[1] is not None:
            p[0] = p[1]
        pass

    def p_save_const(self, p):
        ''' save_const : '''
        # Save consts that are int and float
        if not isinstance(p[-1], str):
            if  type(p[-1]).__name__ == "int":
                address = self.limits.getAddress("intC") + self.limits.getCont("intC")
                self.ctes.addInt(str(p[-1]), address)
                self.limits.upCont("intC")
                address = self.ctes.getInt(str(p[-1]))
            else:
                address = self.limits.getAddress("floatC") + self.limits.getCont("floatC")
                self.ctes.addFloat(str(p[-1]), address)
                self.limits.upCont("floatC")
                address = self.ctes.getFloat(str(p[-1]))
            self.quads.add_operand(address, type(p[-1]).__name__)
        # save constant strings
        elif isinstance(p[-1], str) and p[-1][0] == '"':
            address = self.limits.getAddress("stringC") + self.limits.getCont("stringC")
            self.ctes.addString(p[-1], address)
            self.limits.upCont("stringC")
            address = self.ctes.getString(p[-1])
            self.quads.add_operand(address, "string")
        # save booleans
        elif isinstance(p[-1], str) and (p[-1] == 'false' or p[-1] == 'true'):
            address = self.limits.getAddress("boolC") + self.limits.getCont("boolC")
            self.ctes.addBool(str(p[-1]), address)
            self.limits.upCont("boolC")
            address = self.ctes.getBool(p[-1])
            self.quads.add_operand(address, "bool")
        pass

    def p_save_comp(self, p):
        ''' save_comp : '''
        self.check_variable_exists(p)
        pass

    def check_variable_exists(self, p):
        var_found = False
        index_scope_class = len(self.class_dir.get_scope()) - 1
        while index_scope_class >= 0 and var_found is False:
            if p[-1] is None:
                var_found = True
                print("function is found")
            else:
                scope_class = self.class_dir.get_scope()[index_scope_class]  # get class scope we are checking
                current_class = self.class_dir.get_class(scope_class) # get class object
                var = self.check_var_exists_function(current_class["function_dir"], p[-1])
                if var is None:
                    tablevars = current_class["tablevars"]
                    var = self.check_table_vars(tablevars, p[-1])
                if var is not None:
                    var_found = True
                    self.quads.add_operand(var[0], var[1])
                else:
                    index_scope_class = index_scope_class - 1
        if index_scope_class < 0 and var_found is False:
            sys.exit(f"ERROR: couldn't find declaration of variable {p[-1]} in line {p.lineno(-1)}")

    def check_var_exists_function(self, function_dir: Function_Dir, var_name: str) -> tuple:
        index_scope_func = len(function_dir.get_scope()) - 1
        while index_scope_func >= 0:
            scope_func = function_dir.get_scope()[index_scope_func]
            current_func = function_dir.get_function(scope_func)
            var = self.check_table_vars(current_func["tablevars"], var_name)
            if var is not None:
                return var
            else:
                var = self.check_table_vars(current_func["params"], var_name)
                if var is not None:
                    return var
            index_scope_func = index_scope_func - 1
        return None

    def check_table_vars(self, tablevars: Variables_Dir, var_name: str) -> tuple: #( var , type)
        if var_name in tablevars.get_dictionary():
            var = tablevars.get_variable(var_name)
            return var["address"], var["type"]
        else:
            return None

    def p_expresion(self, p):
        '''
        expresion       : exp altexpresion
        altexpresion    : altexpresion2 save_op  exp
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
        if p[1] is not None:
            p[0] = p[1]
        pass

    def p_exp(self, p):
        '''
        exp     : termino
                | termino altexp
        altexp  : SUM save_op termino altexp
                | SUBTRACT save_op termino altexp
                | empty
        '''
        pass

    def p_termino(self, p):
        '''
        termino     : factor
                    | factor alttermino
        alttermino : TIMES save_op factor alttermino
                    | DIV save_op factor alttermino
                    | empty
        '''
        pass

    def p_save_op(self, p):
        ''' save_op : '''
        self.quads.add_to_stack_op(p[-1])
        pass

    def p_read(self, p):
        '''
        read : INPUT save_op OPENPAREN ID save_comp CLOSEPAREN SEMICOLON
        '''
        pass

    def p_write(self, p):
        '''
        write :  OUTPUT save_op OPENPAREN expresion altwrite
        altwrite : COMMA save_op expresion altwrite
                | CLOSEPAREN SEMICOLON
        '''
        pass

    def p_factor(self, p):
        '''
        factor : OPENPAREN save_op expresion CLOSEPAREN save_op
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
        assign : ID save_comp EQUALS save_op expresion SEMICOLON
        '''
        pass

    def p_return(self, p):
        '''
        return  : RETURN save_op expresion SEMICOLON
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
        sys.exit(f"ERROR: illegal token found: {p.value[0]} in line { p.lineno}")

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
