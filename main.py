from GenerateCode.Function_Dir import Function_Dir
from LexYacc.QCASQ_Lexer import QCASQ_Lexer
from LexYacc.QCSAQ_Parser import QCASQ_Parser
from GenerateCode.SemanticCube import SemanticCube
from GenerateCode.Types import Types


def test_from_file():
    """Read from a file and tries to compile it.

    Tests from a file and tries to execute the following:
        - Lex and Parser
        - Function Directory & Var tables
        - Semantic cube
    """
    file_name = input('Ingresa el nombre del archivo: \n')
    file = open(file_name, 'r')
    src_file = file.read()

    # Creates the Lex and Parser objects
    lexer = QCASQ_Lexer()
    pars = QCASQ_Parser(lexer)

    # Enable only this lines to test the lexer
    # lex = lexer.lexer
    # lex.input(src_file)

    # Enable the next lines to test parser
    parser = pars.parser
    parser.parse(src_file, tracking=True)

    # Prints the function directory generated after finishing reading code
    #pars.funct_dir.print_dictionary()
    print(pars.quads.__polish_vector__)
    print(pars.quads.__stack_operators__)
    print(pars.quads.__stack_quadruples__)

    if pars.get_error():
        print("Something went wrong")
    else:
        print("Ran successfully")
    file.close()


def test_direc():
    """Tests that function directory works fine."""
    test_Func_dir = Function_Dir()
    # defines a function with its type
    func_name = "test"
    func_type = "int"
    # defines a variable with its type
    var_name = "var_test"
    var_type = "string"
    # Adds to function directory
    test_Func_dir.add_to_dictionary(func_name, func_type)
    # Adds the variable to that function table
    test_Func_dir.get_function(func_name)['tablevars'].add_to_dictionary(var_name, var_type)
    # Prints the function directory that has been generated
    #test_Func_dir.print_dictionary()

def test_semantic_cube():
    """Test that the combinations of the semantic cube work well."""
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
