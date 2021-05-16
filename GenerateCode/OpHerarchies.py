import enum


class Hierarchies(enum.IntEnum):
    PARENTESIS  = 0
    MULTDIV     = 1
    SUMSUB      = 2
    COMPARISON  = 3
    LOGIC       = 4
    ASSIGN      = 5


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
        "return": Hierarchies.ASSIGN,
        "input": Hierarchies.ASSIGN,
        "output": Hierarchies.ASSIGN,
    }