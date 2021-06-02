from LexYacc.QCASQ_Lexer import QCASQ_Lexer
from LexYacc.QCSAQ_Parser import QCASQ_Parser
from VirtualMachine.VM import VM

"""
Main file that encapsulates the parser and execution of 
the compiler in a single file. This is the starting point.

:Date: 06-02-2021
:Version: 1
:Authors:
    - Angel Treviño A01336559
    - Julia Jimenez A00821428 
"""


def test_from_file():
    """Reads from a file and tries to compile it."""
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

    # Enable this lines to print different structures used in the parser
    #pars.ctes.print_ctes()
    #pars.class_dir.print_dictionary()
    pars.quads.print_quadruples()
    #print(pars.pars_data_vm())

    # Enable this lines to execute the program from input file
    #print("Ejecución empieza")
    em = VM(pars.pars_data_vm())

    # Catch if there is an error
    if pars.get_error():
        print("Something went wrong")
    else:
        print("Ran successfully")
    file.close()


if __name__ == '__main__':
    test_from_file()
