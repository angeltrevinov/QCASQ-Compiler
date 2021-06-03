import enum


class Types(enum.Enum):
    """
    To define the different variable types possible in the language.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """
    INVALID = "null"
    INT     = "int"
    FLOAT   = "float"
    STRING  = "string"
    CLASS   = "class"
    BOOL    = "bool"
