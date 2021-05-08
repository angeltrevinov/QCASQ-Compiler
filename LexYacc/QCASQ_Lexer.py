import ply.lex as lex


class QCASQ_Lexer(object):
    # --------------- Definition of tokens -----------------
    tokens = [
        'SEMICOLON',            # ;
        'OPENPAREN',            # (
        'CLOSEPAREN',           # )
        'TWODOTS',              # :
        'COMMA',                # ,
        'DOT',                  # .
        'OPENBRACKET',          # [
        'CLOSEBRACKET',         # ]
        'OPENCURLY',            # {
        'CLOSECURLY',           # }
        'SAMEAS',               # ==
        'BIGGERTHAN',           # >
        'BIGGEREQUALSTHAN',     # >=
        'SMALLTHAN',            # <
        'SMALLEQUALSTHAN',      # <=
        'DIFFERENTTHAN',        # !=
        'AND',                  # &&
        'OR',                   # ||
        'EQUALS',               # =
        'SUBTRACT',             # -
        'SUM',                  # +
        'TIMES',                # *
        'DIV',                  # /
        'ID',
        'CTEINT',
        'CTEFLOAT',
        'CTESTRING'
    ]

    # ---------- Definition of Reserved Words --------------
    reserved = {
        'program'       : 'PROGRAM',
        'main'          : 'MAIN',
        'class'         : 'CLASS',
        'constructor'   : 'CONSTRUCTOR',
        'var'           : 'VAR',
        'if'            : 'IF',
        'else'          : 'ELSE',
        'func'          : 'FUNC',
        'return'        : 'RETURN',
        'input'         : 'INPUT',
        'output'        : 'OUTPUT',
        'int'           : 'INT',
        'float'         : 'FLOAT',
        'string'        : 'STRING',
        'bool'          : 'BOOL',
        'true'          : 'TRUE',
        'false'         : 'FALSE',
        'while'         : 'WHILE'
    }

    # ------ Regular expresion rules for simple tokens -----
    t_SEMICOLON             = r'\;'
    t_OPENPAREN             = r'\('
    t_CLOSEPAREN            = r'\)'
    t_TWODOTS               = r'\:'
    t_COMMA                 = r'\,'
    t_DOT                   = r'\.'
    t_OPENBRACKET           = r'\['
    t_CLOSEBRACKET          = r'\]'
    t_OPENCURLY             = r'\{'
    t_CLOSECURLY            = r'\}'
    t_SAMEAS                = r'\=\='
    t_BIGGERTHAN            = r'\>'
    t_BIGGEREQUALSTHAN      = r'\>\='
    t_SMALLTHAN             = r'\<'
    t_SMALLEQUALSTHAN       = r'\<\='
    t_DIFFERENTTHAN         = r'\!\='
    t_AND                   = r'\&\&'
    t_OR                    = r'\|\|'
    t_EQUALS                = r'\='
    t_SUBTRACT              = r'\-'
    t_SUM                   = r'\+'
    t_TIMES                 = r'\*'
    t_DIV                   = r'\/'
    t_ignore                = ' \t'


    def t_CTESTRING(self, t):
        r'\"(.*)\"'
        t.value = str(t.value)
        return t

    def t_CTEFLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_CTEINT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')  # check that id does not match reserved words
        return t

    def t_COMMENT(self, t):
        r'\/\/.*'
        pass
        # No return value. Token discarded

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # constructor
    def __init__(self):
        # adding reserve to tokens list
        self.tokens += list(self.reserved.values())
        self.lexer = lex.lex(module=self)  # to debug add debug=True
