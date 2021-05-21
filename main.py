from LexYacc.QCASQ_Lexer import QCASQ_Lexer
from LexYacc.QCSAQ_Parser import QCASQ_Parser

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
    pars.class_dir.print_dictionary()
    pars.quads.print_quadruples()

    if pars.get_error():
        print("Something went wrong")
    else:
        print("Ran successfully")
    file.close()


if __name__ == '__main__':
    test_from_file()
    #  test_direc()
    # test_semantic_cube()
