from QCASQ_Lexer import *
from QCSAQ_Parser import *

if __name__ == '__main__':
    file_name = input('Ingresa el nombre del archivo: \n')
    file = open(file_name, 'r')
    src_file = file.read()

    lexer = QCASQ_Lexer()
    pars = QCASQ_Parser(lexer)

    lex = lexer.lexer
    parser = pars.parser

    parser.parse(src_file, debug=True, tracking=True)
    if pars.get_error() != True :
        print("Se pudo parsear correctamente")

    file.close()
