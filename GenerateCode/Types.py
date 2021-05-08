import enum


class Types(enum.Enum):
    """To define the different variable types"""
    INVALID = 0
    INT     = 1
    FLOAT   = 2
    STRING  = 3
    CLASS   = 4
    BOOL    = 5
