import enum

class Hierarchies(enum.IntEnum):
    MULTDIV     = 1
    SUMSUB      = 2
    COMPARISON  = 3
    LOGIC       = 4
    PARENTESIS  = 5
    ASSIGN      = 6
    RETURN      = 7
    OUTPUT      = 8
    INPUT       = 9
    GOTOF       = 10
    GOTO        = 11
    GOTOW       = 12
    ENDFUNC     = 13
    ERA         = 14
    PARAMS      = 15
    GOSUB       = 16
    ASSIGNRET   = 17

class OprTranslator():
    OprTrans = {
        "/": 1,
        "*": 2,
        "+": 3,
        "-": 4,
        "<": 5,
        "<=": 6,
        ">": 7,
        ">=": 8,
        "==": 9,
        "!=": 10,
        "&&": 11,
        "||": 12,
        "=": 13,
        "return": 14,
        "input": 15,
        "output": 16,
        "gotof" : 17,
        "goto": 18,
        "endfunc" : 19,
        "era" : 20,
        "params" : 21,
        "gosub" : 22,
        "assignret" : 23
    }

    def translate(self, opr: str):
        return self.OprTrans[opr]


class Operators():
    OpHierarchy = {
        "(": Hierarchies.PARENTESIS,
        ")": Hierarchies.PARENTESIS,
        "*": Hierarchies.MULTDIV,
        "/": Hierarchies.MULTDIV,
        "+": Hierarchies.SUMSUB,
        "-": Hierarchies.SUMSUB,
        '<': Hierarchies.COMPARISON,
        '<=':Hierarchies.COMPARISON,
        '>': Hierarchies.COMPARISON,
        '>=' : Hierarchies.COMPARISON,
        '==' : Hierarchies.COMPARISON,
        '!=' : Hierarchies.COMPARISON,
        '&&': Hierarchies.LOGIC,
        '||': Hierarchies.LOGIC,
        "=": Hierarchies.ASSIGN,
        "return": Hierarchies.RETURN,
        "input": Hierarchies.INPUT,
        "output": Hierarchies.OUTPUT,
        "gotof": Hierarchies.GOTOF,
        "goto": Hierarchies.GOTO,
        "gotow": Hierarchies.GOTOW,
        "endfunc": Hierarchies.ENDFUNC,
        "era" : Hierarchies.ERA,
        "params" : Hierarchies.PARAMS,
        "gosub" : Hierarchies.GOSUB,
        "assignret" : Hierarchies.ASSIGNRET
    }