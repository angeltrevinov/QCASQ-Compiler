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