import sys
import ply.lex as lex


class QCASQ_Lexer(object):
    """
    Class that defines the tokens that are accepted by our
    language.
    The Lexer of our compiler.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """

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
        # check that id does not match reserved words
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_COMMENT(self, t):
        r'\/\/.*'
        # check that id does not match reserved words
        pass

    def t_newline(self, t):
        r'\n+'
        # Define a rule so we can track line numbers
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        """
        To detect if there is an illegal token.
        :param t: the token received
        """
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # constructor
    def __init__(self):
        """
        Tells PLY to use this class as our definition of our
        tokens.
        """
        # adding reserve to tokens list
        self.tokens += list(self.reserved.values())
        self.lexer = lex.lex(module=self)  # to debug add debug=True
