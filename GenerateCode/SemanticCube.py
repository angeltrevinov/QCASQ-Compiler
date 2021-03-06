from GenerateCode.Types import Types


class SemanticCube():
    """
    Class that acts as our semantic cube, tells which operations
    can be done with certain operands.

    :Date: 06-02-2021
    :Version: 1
    :Authors:
        - Angel Treviño A01336559
        - Julia Jimenez A00821428
    """

    __cube__ = {
        # -----------------  INT ---------------------------
        "int": {
            "int": {
                "+": Types.INT,
                "-": Types.INT,
                "*": Types.INT,
                "/": Types.INT,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.BOOL,
                "<=": Types.BOOL,
                "<": Types.BOOL,
                ">=": Types.BOOL,
                ">": Types.BOOL,
                "==": Types.BOOL,
                "=": Types.INT,
                "output": Types.STRING,
                "input": Types.INT
            },
            "float": {
                "+": Types.FLOAT,
                "-": Types.FLOAT,
                "*": Types.FLOAT,
                "/": Types.FLOAT,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.BOOL,
                "<=": Types.BOOL,
                "<": Types.BOOL,
                ">=": Types.BOOL,
                ">": Types.BOOL,
                "==": Types.BOOL,
                "=": Types.INT,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "string": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "class": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "bool": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            }
        },
        # ----------------- FLOAT --------------------------
        "float": {
            "int": {
                "+": Types.FLOAT,
                "-": Types.FLOAT,
                "*": Types.FLOAT,
                "/": Types.FLOAT,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.BOOL,
                "<=": Types.BOOL,
                "<": Types.BOOL,
                ">=": Types.BOOL,
                ">": Types.BOOL,
                "==": Types.BOOL,
                "=": Types.FLOAT,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "float": {
                "+": Types.FLOAT,
                "-": Types.FLOAT,
                "*": Types.FLOAT,
                "/": Types.FLOAT,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.BOOL,
                "<=": Types.BOOL,
                "<": Types.BOOL,
                ">=": Types.BOOL,
                ">": Types.BOOL,
                "==": Types.BOOL,
                "=": Types.FLOAT,
                "output": Types.STRING,
                "input": Types.FLOAT
            },
            "string": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "class": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "bool": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            }
        },
        # ---------------- STR -----------------------------
        "string": {
            "int": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "float": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "string": {
                "+": Types.STRING,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.BOOL,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.BOOL,
                "=": Types.STRING,
                "output": Types.STRING,
                "input": Types.STRING
            },
            "class": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "bool": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            }
        },
        # ------------------- CLASS ------------------------
        "class": {
            "int": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "float": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "string": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "class": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.BOOL,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.BOOL,
                "=": Types.CLASS,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "bool": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            }
        },
        # ------------------ BOOL --------------------------
        "bool": {
            "int": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "float": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "string": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.STRING,
                "input": Types.INVALID
            },
            "class": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.INVALID,
                "&&": Types.INVALID,
                "!=": Types.INVALID,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.INVALID,
                "=": Types.INVALID,
                "output": Types.INVALID,
                "input": Types.INVALID
            },
            "bool": {
                "+": Types.INVALID,
                "-": Types.INVALID,
                "*": Types.INVALID,
                "/": Types.INVALID,
                "||": Types.BOOL,
                "&&": Types.BOOL,
                "!=": Types.BOOL,
                "<=": Types.INVALID,
                "<": Types.INVALID,
                ">=": Types.INVALID,
                ">": Types.INVALID,
                "==": Types.BOOL,
                "=": Types.BOOL,
                "output": Types.STRING,
                "input": Types.BOOL
            }
        }
    }

    def get_result(self, op1: str, op2: str, oper: str) -> str:
        """Gets the type result depending on the desire operation.

        :param op1: The first oper&& variable type
        :type op1: str
        :param op2: The second oper&& variable type
        :type op2: str
        :param oper: The name of the operat|| (check lexer definition)
        :type oper: str
        :return: The variable type that results from this operation
        :rtype: Types
        """
        return self.__cube__[op1][op2][oper].value