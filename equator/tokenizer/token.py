"""
# Equator / Tokenizer / Token

Definitions for tokens
"""
from enum import Enum
from typing import Optional


class TokenType(Enum):
    ERROR = -1
    EOF = -2

    COMMENT = 0

    KEYWORD_IF = 1
    KEYWORD_ELSE = 2
    KEYWORD_WHEN = 3
    KEYWORD_WHILE = 4
    KEYWORD_WHILST = 5
    KEYWORD_EQUATION = 6
    KEYWORD_RELATION = 7

    LITERAL_BOOLEAN = 10
    LITERAL_STRING = 11
    LITERAL_NUMBER_DEC = 12
    LITERAL_NUMBER_HEX = 13
    LITERAL_NUMBER_OCT = 14
    LITERAL_NUMBER_BIN = 15
    LITERAL_NUMBER_FLOAT = 16

    UNKNOWN = 20
    VARIABLE = 21

    SYNTAX_PAREN_OPEN = 30
    SYNTAX_PAREN_CLOSE = 31
    SYNTAX_BRACKET_OPEN = 32
    SYNTAX_BRACKET_CLOSE = 33
    SYNTAX_BRACE_OPEN = 34
    SYNTAX_BRACE_CLOSE = 35
    SYNTAX_SEMICOLON = 36

    OPERATOR_ASSIGN = 40
    OPERATOR_COMMA = 41
    OPERATOR_PIPE = 42
    OPERATOR_MAP = 43
    OPERATOR_JOIN = 44
    OPERATOR_CAPTURE = 45
    OPERATOR_EQUALITY = 46
    OPERATOR_INEQUALITY = 47
    OPERATOR_ADD = 48
    OPERATOR_SUBTRACT = 49
    OPERATOR_MULTIPLY = 50
    OPERATOR_DIVIDE = 51
    OPERATOR_MOD = 52
    OPERATOR_POWER = 53
    OPERATOR_NOT = 54
    OPERATOR_BOOLEAN_OR = 55
    OPERATOR_BOOLEAN_AND = 56

    CONDITIONAL_EQUALITY = 60
    CONDITIONAL_INEQUALITY = 61
    CONDITIONAL_GREATER = 62
    CONDITIONAL_GREATER_EQUAL = 63
    CONDITIONAL_LESS = 64
    CONDITIONAL_LESS_EQUAL = 65


class Token:
    """
    A token
    """

    def __init__(
        self,
        kind: TokenType,
        string: str,
        notes: Optional[str] = None,
    ) -> None:
        self.kind = kind
        self.string = string
        self.notes = notes

    def __repr__(self) -> str:
        return self.string
