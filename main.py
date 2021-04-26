from QCASQ_Lexer import *
from QCSAQ_Parser import *


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
    pars.funct_dir.print_dictionary()
    #pars.funct_dir.get_function("Example")["tablevars"].print_dictionary()
    #print("=============")
    #pars.var_dir.print_dictionary()
    #print("=============")
    #print(pars.funct_dir.get_scope())
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

    test_Func_dir.print_dictionary()


if __name__ == '__main__':
    test_from_file()
    #  test_direc()
