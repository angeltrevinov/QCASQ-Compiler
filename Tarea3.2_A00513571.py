import ply.lex as lex
import ply.yacc as yacc
import sys

err = False
#Definición de Tokens a utilizar
tokens = [
            'BIGGERTHAN',
			'LESSTHAN',
			'DIFFERENT',
			'MINUS',
			'PLUS',
			'MULTIPLY',
			'DIVIDE',
			'ID',
			'TWODOTS',
			'COMMA',
			'LSQRBRA',
			'RSQRBRA',
			'LPAREN',
			'RPAREN',
            'SEMICOLON',
            'EQUALS',
            'CTESTRING',
            'CTEFLOAT',
            'CTEINT'
    ]
#Definición de palabras reservadas
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'print': 'PRINT',
    'program': 'PROGRAM'
}


tokens += list(reserved.values())

#Simbología de los tokens
t_BIGGERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_DIFFERENT = r'\<\>' 
t_MINUS = r'\-'
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_LSQRBRA = r'\{'
t_RSQRBRA = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'			
t_COMMA = r'\,'
t_TWODOTS = r'\:'
t_SEMICOLON = r'\;'
t_ignore = ' \t\n'

def t_CTESTRING(token):
    r'\"(.*)\"'
    token.value = str(token.value)
    return token

def t_CTEFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTEINT(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_error(t):
    print("No apropiado")
    t.lexer.skip(1)

lexer = lex.lex()

#Definición de gramáticas

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON vars bloque
            | PROGRAM ID SEMICOLON bloque
    '''
    pass

def p_vars(p):
    '''
    vars : VAR vars2
    '''
    pass
def p_vars2(p):
    '''
    vars2 : vars3 TWODOTS tipo SEMICOLON vars2
          | vars3 TWODOTS tipo SEMICOLON 
    '''
    pass
def p_vars3(p):
    '''
    vars3 : ID COMMA vars3  
          | ID 
    '''
    pass
def p_tipo(p):
    '''
    tipo : INT 
         | FLOAT 
    '''
    pass
def p_bloque(p):
    '''
    bloque : LSQRBRA estatuto bloque1 RSQRBRA
           | LSQRBRA estatuto RSQRBRA
           | LSQRBRA RSQRBRA
    '''
    pass
def p_estatuto(p):
    '''
    estatuto : asignacion 
             | condicion
             | escritura
    '''
    pass
def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN bloque ELSE bloque SEMICOLON
              | IF LPAREN expresion RPAREN bloque SEMICOLON
    '''
    pass

def p_escritura(p):
    '''
    escritura : PRINT LPAREN es1 RPAREN SEMICOLON
    '''
    pass
def p_es1(p):
    '''
    es1 : expresion
        | CTESTRING
        | expresion COMMA es1
        | CTESTRING COMMA es1 
    '''
    pass
def p_bloque1(p):
    '''
    bloque1 : estatuto bloque1
            | estatuto
    '''
    pass
def p_asignacion(t):
    '''
    asignacion : ID EQUALS expresion SEMICOLON
    '''
    pass
def p_expresion(p):
    '''
    expresion : exp BIGGERTHAN exp
              | exp LESSTHAN exp
              | exp DIFFERENT exp
              | exp
    '''
    pass
def p_exp(p):
    '''
    exp : termino exp1 exp 
        | termino
    '''
    pass
def p_exp1(p):
    '''
    exp1 : PLUS 
         | MINUS
    '''
    pass
def p_termino(p):
    '''
    termino : factor t1 termino
            | factor
    '''
    pass
def p_t1(p):
    '''
    t1 : MULTIPLY 
       | DIVIDE
    '''
    pass

def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
           | PLUS varcte
           | MINUS varcte
           | varcte
    '''
    pass
def p_varcte(p):
    '''
    varcte : ID
           | CTEINT
           | CTEFLOAT
    '''
    pass
def p_error(p):
    global err
    err = True
    print("\nNo apropiado\n")

parser = yacc.yacc()

try: 
    fileName = input("\nIngresa el nombre del archivo: ")
    filehandle = open(fileName, "r")
    srcFile = filehandle.read()
    result = parser.parse(srcFile)

    if not err:
        print("\nApropiado\n")
except:
    print("\nEl archivo no fue encontrado\n")