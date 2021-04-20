from QCASQ_Lexer import *
from QCSAQ_Parser import *
from Function_Dir import *


def test_from_file():
    file_name = input('Ingresa el nombre del archivo: \n')
    file = open(file_name, 'r')
    src_file = file.read()

    lexer = QCASQ_Lexer()
    pars = QCASQ_Parser(lexer)

    # to test lex
    # lex = lexer.lexer
    # lex.input(src_file)

    # to test parser
    parser = pars.parser
    parser.parse(src_file)
    if pars.get_error() == True:
        print("Error")
    else:
        print("todo bien")

    file.close()


def test_direc():
    test_Func_dir = Function_Dir()
    func_name = "test"
    func_type = "int"

    var_name = "var_test"
    var_type = "string"

    test_Func_dir.add_to_dictionary(func_name, func_type)
    test_Func_dir.get_function(func_name)['tablevars'].add_to_dictionary(var_name, var_type)

    print("function:", test_Func_dir.get_function(func_name))
    print("============")
    print("var tables:", test_Func_dir.get_function(func_name)['tablevars'].get_variable(var_name))
    print("============")


if __name__ == '__main__':
    test_from_file()
    #  test_direc()
