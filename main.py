from LexYacc.QCASQ_Lexer import QCASQ_Lexer
from LexYacc.QCSAQ_Parser import QCASQ_Parser
from GenerateCode.SemanticCube import SemanticCube
from GenerateCode.Types import Types


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
    if pars.get_error():
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


def test_semantic_cube():
    semantic_cube = SemanticCube()
    result_sum_ints = semantic_cube.get_result("int", "int", "SUM")
    assert result_sum_ints == Types.INT, "not int"
    result_int_float = semantic_cube.get_result("int", "float", "DIV")
    assert result_int_float == Types.FLOAT, "not float"
    result_class_bool = semantic_cube.get_result("class", "bool", "DIFFERENTTHAN")
    assert result_class_bool == Types.INVALID, "not invalid"


if __name__ == '__main__':
    test_from_file()
    #  test_direc()
    # test_semantic_cube()
