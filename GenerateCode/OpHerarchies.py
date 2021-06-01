import enum

class Hierarchies(enum.IntEnum):
    """
    Enum that gives herarchies of operations to our operators

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """
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
    VER         = 18
    ADDBASE     = 19

class OprTranslator():
    """
    Class that transforms our operators into values that we
    can use in execution memory.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """
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
        "assignret" : 23,
        "ver" : 24,
        "addbase" : 25
    }

    def translate(self, opr: str) -> int:
        """
        Giving an operator in string, returns the id we
        identified that operator with.
        :param opr: operator
        :type opr: str
        :return: the id of that operator
        :rtype: int
        """
        return self.OprTrans[opr]


class Operators():
    """
    Class that helps us look for the hierarchies of a certain
    operator.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """
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
        "assignret" : Hierarchies.ASSIGNRET,
        "ver" : Hierarchies.VER,
        "addbase" : Hierarchies.ADDBASE
    }