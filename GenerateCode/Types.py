import enum


class Types(enum.Enum):
    """To define the different variable types"""
    INVALID = "null"
    INT     = "int"
    FLOAT   = "float"
    STRING  = "string"
    CLASS   = "class"
    BOOL    = "bool"
