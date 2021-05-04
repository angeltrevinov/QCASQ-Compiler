from Types import Types

class SemanticCube:

    __cube__= {
        ###### INT
        "int": {
            "int": {
                "SUM": Types.INT,
                "SUBTRACT": Types.INT,
                "TIMES": Types.INT,
                "DIV": Types.INT,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.BOOL,
                "SMALLEQUALSTHAN": Types.BOOL,
                "SMALLTHAN": Types.BOOL,
                "BIGGEREQUALSTHAN": Types.BOOL,
                "BIGGERTHAN": Types.BOOL,
                "SAMEAS": Types.BOOL,
                "EQUALS": Types.INT,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INT
            },
            "float": {
                "SUM": Types.FLOAT,
                "SUBTRACT": Types.FLOAT,
                "TIMES": Types.FLOAT,
                "DIV": Types.FLOAT,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.BOOL,
                "SMALLEQUALSTHAN": Types.BOOL,
                "SMALLTHAN": Types.BOOL,
                "BIGGEREQUALSTHAN": Types.BOOL,
                "BIGGERTHAN": Types.BOOL,
                "SAMEAS": Types.BOOL,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "string": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "class": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "bool": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            }
        },
        ###### FLOAT
        "float": {
            "int": {
                "SUM": Types.FLOAT,
                "SUBTRACT": Types.FLOAT,
                "TIMES": Types.FLOAT,
                "DIV": Types.FLOAT,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.BOOL,
                "SMALLEQUALSTHAN": Types.BOOL,
                "SMALLTHAN": Types.BOOL,
                "BIGGEREQUALSTHAN": Types.BOOL,
                "BIGGERTHAN": Types.BOOL,
                "SAMEAS": Types.BOOL,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "float": {
                "SUM": Types.FLOAT,
                "SUBTRACT": Types.FLOAT,
                "TIMES": Types.FLOAT,
                "DIV": Types.FLOAT,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.BOOL,
                "SMALLEQUALSTHAN": Types.BOOL,
                "SMALLTHAN": Types.BOOL,
                "BIGGEREQUALSTHAN": Types.BOOL,
                "BIGGERTHAN": Types.BOOL,
                "SAMEAS": Types.BOOL,
                "EQUALS": Types.FLOAT,
                "OUTPUT": Types.STRING,
                "INPUT": Types.FLOAT
            },
            "string": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "class": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "bool": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            }
        },
        ####### STR
        "string": {
            "int": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "float": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "string": {
                "SUM": Types.STRING,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.BOOL,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.BOOL,
                "EQUALS": Types.STRING,
                "OUTPUT": Types.STRING,
                "INPUT": Types.STRING
            },
            "class": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "bool": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            }
        },
        ####### CLASS
        "class": {
            "int": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "float": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "string": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "class": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.BOOL,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.BOOL,
                "EQUALS": Types.CLASS,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "bool": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            }
        },
        ###### BOOL
        "bool": {
            "int": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "float": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "string": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.STRING,
                "INPUT": Types.INVALID
            },
            "class": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.INVALID,
                "AND": Types.INVALID,
                "DIFFERENTTHAN": Types.INVALID,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.INVALID,
                "EQUALS": Types.INVALID,
                "OUTPUT": Types.INVALID,
                "INPUT": Types.INVALID
            },
            "bool": {
                "SUM": Types.INVALID,
                "SUBTRACT": Types.INVALID,
                "TIMES": Types.INVALID,
                "DIV": Types.INVALID,
                "OR": Types.BOOL,
                "AND": Types.BOOL,
                "DIFFERENTTHAN": Types.BOOL,
                "SMALLEQUALSTHAN": Types.INVALID,
                "SMALLTHAN": Types.INVALID,
                "BIGGEREQUALSTHAN": Types.INVALID,
                "BIGGERTHAN": Types.INVALID,
                "SAMEAS": Types.BOOL,
                "EQUALS": Types.BOOL,
                "OUTPUT": Types.STRING,
                "INPUT": Types.BOOL
            }
        }
    }

    def get_result(self, op1: str, op2: str, oper: str) -> int:
        return self.__cube__[op1][op2][oper]