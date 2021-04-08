from QCASQ_Lexer import *

if __name__ == '__main__':
    file_name = input('Ingresa el nombre del archivo: \n')
    file = open(file_name, 'r')
    src_file = file.read()

    my_lexer = QCASQ_Lexer()
    lex = my_lexer.lexer
    lex.input(src_file)