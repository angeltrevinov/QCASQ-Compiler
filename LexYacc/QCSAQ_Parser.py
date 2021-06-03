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
    """
    The parser of our compiler. Here we are making sure the
    input has a valid structure, create our func and vars
    tables and generating intermediate code for our execution
    memory.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """

    __error = False
    __stack_vars = []  # this is to store if multiple vars came as a list, so we can also add their type
    __stack_params = []  # to save the params in their corresponding function directory
    tokens = QCASQ_Lexer.tokens  # add the lexer
    stack_dimensions = [] # to keep track of the number of dimensions if variable is an array
    # to keep track of the variables that we are sending the func call
    params_call = []
    count_params = 0
    count = 1

    # initialize Objects that we need
    class_dir = Class_Dir()
    quads = QuadrupleManager()
    limits = Limits()  # where every type of variable starts in memory
    ctes = CteTable()  # to save the constants that appear.

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

    def p_main(self, p):
        '''
        main    : MAIN save_main OPENPAREN CLOSEPAREN OPENCURLY altmain
        altmain : var altmain
                | estatuto altmain
                | CLOSECURLY
        '''
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

    def p_var(self, p):
        '''
        var : VAR listids TWODOTS type save_vars SEMICOLON
        '''
        pass

    def p_listids(self, p):
        """
        listids     : ID save_var_name dec_array empty_dim_stack listidsalty
        listidsalty : COMMA listids
                    | empty
        """
        pass

    def p_dec_array(self, p):
        """
        dec_array   : OPENBRACKET CTEINT CLOSEBRACKET dec_array2
                    | empty
        dec_array2  : OPENBRACKET CTEINT CLOSEBRACKET
                    | empty
        """
        if p[1] is not None:
            self.stack_dimensions.append(p[2])
            new_tuple = (self.__stack_vars[-1][0], True)
            self.__stack_vars.pop()
            self.__stack_vars.append(new_tuple)
        pass

    def p_array(self, p):
        '''
        array   : OPENBRACKET add_false_stack expresion end_false_stack CLOSEBRACKET generate_ver_quad array2 add_dir_base
                | empty
        array2  : OPENBRACKET add_false_stack expresion end_false_stack CLOSEBRACKET generate_ver_quad
                | empty
        '''

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

    def p_params(self, p):
        '''
        params      : ID TWODOTS type save_params altparams
        altparams   : COMMA ID TWODOTS type save_params altparams
                    | empty
        '''
        pass

    def p_callfunc(self, p):
        '''
        callfunc    : ID check_exists_func add_false_stack OPENPAREN altcall check_params CLOSEPAREN end_false_stack generate_gosub
        altcall     : expresion generate_param_quad alt2call
                    | empty
        alt2call   : COMMA altcall
                    | empty
        '''
        if p[1] is not None and p[1] != ",":
            p[0] = p[1]
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
        voidcall : callfunc SEMICOLON
                | ID DOT voidcall
        '''
        pass

    def p_while(self, p):
        '''
        while    : WHILE add_stack_jump OPENPAREN expresion CLOSEPAREN add_gotof OPENCURLY altwhile end_while
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
                        | array empty
        varcomp3        : varcomp1
                        | callfunc
        '''
        # TODO: doesn't know id.func() id.id
        if p[1] is not None and p[1] != ".":
            p[0] = p[1]
        pass


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
        condition : IF OPENPAREN expresion CLOSEPAREN add_gotof OPENCURLY altcondition add_end_if
                    | IF OPENPAREN expresion CLOSEPAREN add_gotof OPENCURLY altcondition ELSE generate_goto OPENCURLY altcondition add_end_if
        altcondition : estatuto altcondition
                    | CLOSECURLY
        '''
        pass

    def p_assign(self, p):
        '''
        assign : ID array save_comp EQUALS save_op expresion SEMICOLON
        '''
        pass

    def p_return(self, p):
        '''
        return  : RETURN expresion generate_quad_ret SEMICOLON add_return_exists
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

    # --------------- Neuralgic points ---------------------
    # Add the program name to the dictionary
    def p_save_program(self, p):
        """ save_program : """
        self.class_dir.add_to_dictionary(p[-1])
        self.class_dir.add_to_scope(p[-1])
        pass

    # Add the main to function dictionary
    def p_save_main(self, p):
        ''' save_main : '''
        self.quads.completeGoto("gotof")
        # adds main to the function directory of the program
        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_dictionary(p[-1])
        # sets the scope as main for the program class
        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_scope(p[-1])
        self.limits.reset_locals()
        pass

    # Add the class and its inheritance to the dictionary
    def p_save_class(self, p):
        """ save_class : """
        self.class_dir.add_to_dictionary(p[-2], p[-1])
        self.class_dir.add_to_scope(p[-2])
        pass

    # Removes the class from the scope
    def p_remove_class_scope(self, p):
        """ remove_class_scope : """
        class_scope = self.class_dir.get_current_scope()
        func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
        # save how many variables we have in the constructor
        count = self.limits.get_local_vars_count()
        self.class_dir.get_class(class_scope)["function_dir"].add_num_vars(count, func_scope)
        self.class_dir.pop_scope()
        pass

    # Add the construction to the dictionary
    def p_save_constructor(self, p):
        """ save_constructor : """
        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_dictionary(p[-1])

        self.class_dir.get_class(
            self.class_dir.get_current_scope()
        )["function_dir"].add_to_scope(p[-1])
        self.limits.reset_locals()
        pass

    def p_save_vars(self, p):
        """ save_vars : """
        class_func_scope_length = len(
            self.class_dir.get_class(
                self.class_dir.get_current_scope()
            )["function_dir"].get_scope()
        )
        class_scope = self.class_dir.get_current_scope()
        for element in self.__stack_vars:
            # Global variables for that class
            if class_func_scope_length == 0:
                # Check if we are in the global scope
                if len(self.class_dir.get_scope()) == 1:
                    # Add the variable to global vars
                    tipo = p[-1] + "G"
                    address = self.limits.getAddress(tipo) + self.limits.getCont(tipo)
                    if element[1] == True:  # An array has been found
                        dimensions = element[2]
                        R = self.calculate_r(dimensions)
                        self.limits.check_limits(address+R, tipo)
                        self.class_dir.get_class(
                            class_scope
                        )["tablevars"].add_to_dictionary(
                            element[0], p[-1], address, dimensions, R-1
                        )
                        self.limits.upCont(tipo, R)
                    else:  # A simple var has been foun
                        self.limits.check_limits(address, tipo)
                        self.class_dir.get_class(
                            class_scope
                        )["tablevars"].add_to_dictionary(
                            element[0], p[-1], address
                        )
                        self.limits.upCont(tipo)

                # TODO: CHECKS if var is declared inside a class
                else:
                    self.class_dir.get_class(
                        class_scope
                    )["tablevars"].add_to_dictionary(element[0], p[-1], 0)
            else:
                # local variables for a class
                func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
                tipo = p[-1] + "L"
                address = self.limits.getAddress(tipo) + self.limits.getCont(tipo)
                if element[1] == True:
                    dimensions = element[2]
                    R = self.calculate_r(dimensions)
                    self.limits.check_limits(address+R, tipo)
                    self.class_dir.get_class(
                        class_scope
                    )["function_dir"].get_function(
                        func_scope
                    )["tablevars"].add_to_dictionary(
                        element[0], p[-1], address, dimensions, R-1
                    )
                    self.limits.upCont(tipo, R)
                else:
                    self.limits.check_limits(address, tipo)
                    self.class_dir.get_class(
                        class_scope
                    )["function_dir"].get_function(
                        func_scope
                    )["tablevars"].add_to_dictionary(element[0], p[-1], address)
                    self.limits.upCont(tipo)
        self.__stack_vars.clear()
        pass

    def calculate_r(self, dimensions: list) -> int:
        R = 1
        for dim in dimensions:
            R = dim * R
        return R

    # Adds the var to the var stack to be safe later
    def p_save_var_name(self, p):
        """ save_var_name : """
        self.__stack_vars.append((p[-1], False))
        pass

    # Add function name and type to the dictionary
    def p_save_function(self, p):
        """ save_function : """
        # Saving function with their type to the function dir
        class_scope = self.class_dir.get_current_scope()
        if p[-1] is not None:
            self.class_dir.get_class(class_scope)["function_dir"].add_to_dictionary(p[-5], p[-1])
        else:
            self.class_dir.get_class(class_scope)["function_dir"].add_to_dictionary(p[-5])
        self.class_dir.get_class(class_scope)["function_dir"].add_to_scope(p[-5])
        cont_quad = len(self.quads.get_quadruples())  # Know where the function starts in the quads
        self.class_dir.get_class(class_scope)["function_dir"].add_quad_dir(cont_quad, p[-5])
        if p[-1] is not None:
            tipo = p[-1] + "G"
            address = self.limits.getAddress(tipo) + self.limits.getCont(tipo)
            self.class_dir.get_class(class_scope)["tablevars"].add_to_dictionary(p[-5], p[-1], address)
            self.limits.upCont(tipo)
        else:
            self.class_dir.get_class(class_scope)["tablevars"].add_to_dictionary(p[-5], "void", -1)
        self.limits.reset_locals()
        pass

    # store the params as part of variables for the function
    def p_store_params(self, p):
        """ store_params : """
        class_scope = self.class_dir.get_current_scope()
        func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
        for param in self.__stack_params:
            name, type = param
            address = self.limits.getAddress(type + "L") + self.limits.getCont(type + "L")
            self.limits.check_limits(address, type + "L")
            self.class_dir.get_class(
                class_scope
            )["function_dir"].get_function(
                func_scope
            )["params"].add_to_dictionary(name, type, address)
            self.limits.upCont(type + "L")
        self.__stack_params.clear()

    # Removes the current function from scope
    def p_remove_function_scope(self, p):
        """ remove_function_scope : """
        class_scope = self.class_dir.get_current_scope()
        func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
        # Save how many variables we used
        count = self.limits.get_local_vars_count()
        self.class_dir.get_class(class_scope)["function_dir"].add_num_vars(count, func_scope)
        has_return = self.class_dir.get_class(class_scope)["function_dir"].get_function(func_scope)["has_return"]
        if has_return == False:
            sys.exit(f"ERROR: couldn't find return for function {func_scope}")
        self.class_dir.get_class(class_scope)["function_dir"].pop_scope()
        tipo = self.class_dir.get_class(class_scope)["function_dir"].get_function(func_scope)["has_return"]
        self.quads.add_to_stack_op("endfunc")
        pass

    # Adds the params that needs to be received to the stack
    def p_save_params(self, p):
        """ save_params : """
        self.__stack_params.append((p[-3], p[-1]))
        pass

    def p_add_false_stack(self, p):
        """ add_false_stack : """
        self.quads.add_to_stack_op("(")
        pass

    def p_end_false_stack(self, p):
        """ end_false_stack : """
        self.quads.add_to_stack_op(")")
        pass

    def p_generate_gosub(self, p):
        """ generate_gosub : """
        name = p[-8]
        class_scope = self.class_dir.get_current_scope()
        func_dir = self.class_dir.get_class(class_scope)["function_dir"].get_dictionary()
        function = self.check_function_dir(func_dir, name)
        quad_start = function["startQuad"]
        self.quads.add_operand(quad_start, name)
        self.quads.add_to_stack_op("gosub")
        if function["type"] != "void":
            var = self.class_dir.get_class(class_scope)["tablevars"].get_variable(name)
            self.quads.add_operand(var["address"], var["type"])
            self.quads.add_to_stack_op("assignret")
        pass

    def p_check_params(self, p):
        """ check_params : """
        # Get fucntion we are calling
        if self.count_params < len(self.params_call):
            sys.exit(f"ERROR: Missing {len(self.params_call) - self.count_params} param(s) in line {p.lineno(-1)}")
        pass

    def p_generate_param_quad(self, p):
        """ generate_param_quad : """
        self.quads.empty_polish_vector()
        if self.count_params < len(self.params_call):
            self.quads.add_operand(self.params_call[self.count_params]["address"], self.params_call[self.count_params]["type"] )
            self.quads.add_to_stack_op("params")
            self.count_params = self.count_params + 1
        else:
            sys.exit(f"ERROR: Too many params in line {p.lineno(-1)}")

    def p_check_exists_func(self, p):
        ''' check_exists_func : '''
        func_found = False
        index_scope_class = len(self.class_dir.get_scope()) - 1
        while index_scope_class >= 0 and func_found is False:
            scope_class = self.class_dir.get_scope()[index_scope_class]
            func_dir = self.class_dir.get_class(scope_class)["function_dir"].get_dictionary()
            function = self.check_function_dir(func_dir, p[-1])
            index_scope_class = index_scope_class-1
            if function is None:
                sys.exit(f"ERROR: couldn't find declaration of function {p[-1]} in line {p.lineno(-1)}")
        self.create_era(p[-1], function)
        pass

    def p_empty_pv(self, p):
        """ empty_pv : """
        self.quads.empty_polish_vector()
        pass

    def p_add_stack_jump(self, p):
        """ add_stack_jump : """
        self.quads.add_jump_stack()
        pass

    def p_end_while(self, p):
        """ end_while : """
        self.quads.add_to_stack_op("gotow")
        pass

    def p_save_const(self, p):
        """ save_const : """
        # Save consts that are int and float
        if not isinstance(p[-1], str):
            if type(p[-1]).__name__ == "int":
                address = self.limits.getAddress("intC") + self.limits.getCont("intC")
                self.limits.check_limits(address, "intC")
                added = self.ctes.addInt(str(p[-1]), address)
                if added == True:
                    self.limits.upCont("intC")
                address = self.ctes.getInt(str(p[-1]))
            else:
                address = self.limits.getAddress("floatC") + self.limits.getCont("floatC")
                self.limits.check_limits(address, "floatC")
                added = self.ctes.addFloat(str(p[-1]), address)
                if added == True:
                    self.limits.upCont("floatC")
                address = self.ctes.getFloat(str(p[-1]))
            self.quads.add_operand(address, type(p[-1]).__name__)
        # save constant strings
        elif isinstance(p[-1], str) and p[-1][0] == '"':
            address = self.limits.getAddress("stringC") + self.limits.getCont("stringC")
            self.limits.check_limits(address, "stringC")
            added = self.ctes.addString(p[-1], address)
            if added == True:
                self.limits.upCont("stringC")
            address = self.ctes.getString(p[-1])
            self.quads.add_operand(address, "string")
        # save booleans
        elif isinstance(p[-1], str) and (p[-1] == 'false' or p[-1] == 'true'):
            address = self.limits.getAddress("boolC") + self.limits.getCont("boolC")
            self.limits.check_limits(address, "boolC")
            added = self.ctes.addBool(str(p[-1]), address)
            if added == True:
                self.limits.upCont("boolC")
            address = self.ctes.getBool(p[-1])
            self.quads.add_operand(address, "bool")
        pass

    def p_save_comp(self, p):
        """ save_comp : """
        if p[-1] is None:
            var_name = p[-2]
        else:
            var_name = p[-1]
        var = self.check_variable_exists(var_name, p)
        # catchet if var_name is a function, do not add
        if var is not None and var[2] is None:
            self.quads.add_operand(var[0], var[1])

        pass

    def p_save_op(self, p):
        """ save_op : """
        self.quads.add_to_stack_op(p[-1])
        pass

    def p_add_gotof(self, p):
        """ add_gotof : """
        self.quads.add_to_stack_op("gotof")
        pass

    def p_add_end_if(self, p):
        """ add_end_if : """
        self.quads.completeGoto("gotof")
        pass

    def p_generate_goto(self, p):
        """ generate_goto : """
        self.quads.completeGoto("goto")
        self.quads.add_to_stack_op("goto")
        pass

    def p_generate_quad_ret(self, p):
        """ generate_quad_ret : """
        self.quads.empty_polish_vector()
        class_scope = self.class_dir.get_current_scope()
        func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
        var = self.class_dir.get_class(class_scope)["tablevars"].get_variable(func_scope)
        if var["type"] == "void":
            sys.exit(f"Error: you cannot use a return inside a void function")
        self.quads.add_operand(var["address"], var["type"])
        self.quads.add_to_stack_op("return")
        self.quads.add_to_stack_op("endfunc")
        pass

    def p_add_return_exists(self, p):
        """ add_return_exists : """
        class_scope = self.class_dir.get_current_scope()
        func_scope = self.class_dir.get_class(class_scope)["function_dir"].get_current_scope()
        self.class_dir.get_class(class_scope)["function_dir"].get_function(func_scope)["has_return"] = True
        pass

    def p_empty_dim_stack(self, p):
        ''' empty_dim_stack : '''
        if self.__stack_vars[-1][1]:
            new_tuple = (self.__stack_vars[-1][0], True, self.stack_dimensions.copy())
            self.__stack_vars.pop()
            self.__stack_vars.append(new_tuple)
            self.stack_dimensions.clear()
        pass

    def p_generate_ver_quad(self, p):
        ''' generate_ver_quad : '''
        # TODO: Check dimensions to catch errors
        var_name = p[-6]
        var = self.check_variable_exists(var_name, p)
        if var is None:
            var_name = p[-12]
            var = self.check_variable_exists(var_name, p)
        if var[2] is None:
            sys.exit(f"{var_name} is not an array in line {p.lineno(-1)}")
        elif len(var[2]) == 1:
            limitS = var[2][0]
            self.quads.add_operand(limitS, "int")
            self.quads.add_to_stack_op("ver")
        elif len(var[2]) == 2:
            if(self.count < 0):
                self.count = 1
            limitS = var[2][self.count]
            self.quads.add_operand(limitS, "int")
            self.quads.add_to_stack_op("ver")
            if self.count > 0:
                self.multi_s_d(var_name, p)
            if self.count == 0:
                self.generate_s2(var_name)
            self.count -= 1
        pass

    def p_add_dir_base(self, p):
        ''' add_dir_base : '''
        var = self.check_variable_exists(p[-8], p)
        self.quads.add_operand(var[0], var[1])
        self.quads.add_to_stack_op("addbase")
        pass

    # --------------- Helper Functions ---------------------
    def create_era(self, function_name: str, function: dict):
        """
        Function that creates the quadruples for era
        :param function_name: the function name where we are
        :type function_name: str
        :param function: the function directory
        :type function: dict
        """
        self.quads.add_operand(function_name, "")
        self.quads.add_to_stack_op("era")
        params = function["params"].get_dictionary()
        for param in params:
            self.params_call.append(params[param])

    def check_function_dir(self, func_dir: dict, func_name: str):
        """
        Checks that the function exists inside the function
        directory of a class.
        :param func_dir: the function directory object
        :type func_dir: dict
        :param func_name: the name of the function to check
        :type func_name: str
        :return: the information of the function
        :rtype: dict
        """
        if func_name in func_dir:
            return func_dir[func_name]

    def check_variable_exists(self, var_name: str, p):
        """
        Checks if the variable exists in any scope
        :param var_name: the name of the variable to find
        :type var_name: str
        :param p: where we are in the parser
        :return: The variable found
        :rtype: dict
        """
        var_found = False
        index_scope_class = len(self.class_dir.get_scope()) - 1
        while index_scope_class >= 0 and var_found is False:
            # to stop function calls being a variable
            if var_name is None:
                var_found = True
            else:
                # To check inside the class object
                scope_class = self.class_dir.get_scope()[index_scope_class]  # get class scope we are checking
                current_class = self.class_dir.get_class(scope_class)  # get class object
                var = self.check_var_exists_function(current_class["function_dir"], var_name)
                # check global vars
                if var is None:
                    tablevars = current_class["tablevars"]
                    var = self.check_table_vars(tablevars, var_name)
                # when the var is found
                if var is not None:
                    var_found = True
                    # check if its a function
                    if self.check_var_in_function(var_name, current_class):
                        # checks the function is not void
                        if var[1] == "void":
                            sys.exit(f"Error: you cannot use a void function inside an expresion")
                    else:
                        return var
                else:
                    index_scope_class = index_scope_class - 1
        # if we cannot find the variable
        if index_scope_class < 0 and var_found is False:
            sys.exit(f"ERROR: couldn't find declaration of variable {var_name} in line {p.lineno(-1)}")

    def check_var_in_function(self, name_var: str, current_class) -> bool:
        """
        Checks that the var is a function call.

        :param name_var: name of the variable to checl
        :type name_var: str
        :param current_class: the current class we are on
        :type current_class: dict
        :return: If its a function
        :rtype: bool
        """
        if name_var in current_class["function_dir"].get_dictionary():
            return True
        else:
            return False

    def check_var_exists_function(self, function_dir: Function_Dir, var_name: str) -> tuple:
        """ Check that the var exists inside the function

        :param function_dir: The function dictionary to look at
        :type function_dir: Function_Dir
        :param var_name: variable name to search for
        :type var_name: str
        :return: The variable info if found
        :rtype: tuple
        """
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
        """ Check that the variable exists inside the tables var

        :param tablevars: The tables var to check at
        :type tablevars: Variables_Dir
        :param var_name:The var to look for
        :type var_name: str
        :return: The variables information
        :rtype: tuple
        """
        if var_name in tablevars.get_dictionary():
            var = tablevars.get_variable(var_name)
            return var["address"], var["type"], var["dims"]
        else:
            return None

    def generate_s2(self, var_name : str):
        """
        Generates the S2 quadruple.

        :param var_name: the name of the variable
        :type var_name: str
        """
        self.quads.add_to_stack_op("s2")

    def multi_s_d(self, var_name: str, p):
        """
        Generates the s1*d2 quadruple.

        :param var_name: the name of the variable
        :type var_name: str
        :param p: just o know the line of code
        """
        var = self.check_variable_exists(var_name, p)
        self.quads.add_operand(var[2][0], "int")
        self.quads.add_to_stack_op("s1d2")
        pass

    def __init__(self, lexer):
        """The constructor of the parser/

        :param lexer: The lexer object to use for our parser
        """
        self.parser = yacc.yacc(module=self, debug=True)  # To use debug add debug = True
        self.lexer = lexer

    def pars_data_vm(self) -> dict:
        """
        Transform the collected data to an object our virtual
        machine can understand.

        :return: obj that the vm is going to read
        :rtype: dict
        """
        # save the number of variables our global scope used.
        counts = self.limits.get_global_vars_count()
        self.class_dir.add_num_vars(counts)
        obj = {
            "ClassDir"   : self.class_dir.get_dictionary(),
            "Constants"  : self.ctes.get_ctes_table(),
            "Quadruples" : self.quads.get_quadruples()
        }
        return obj

    def get_error(self) -> bool:
        """
        :return: if there is an error when parsing
        :rtype: bool
        """
        return self.__error
