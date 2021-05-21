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
        "output": 16
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
    }