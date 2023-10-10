
from typing import Iterator
from .token import Token, TokenType
from string import ascii_letters, whitespace, digits, hexdigits, octdigits


BINARY_DIGITS = "01"
IDENTIFIER_CHARS = ascii_letters + digits + "_"
IDENTIFIER_START_CHARS = ascii_letters + "_"

SEPARATOR_CHARACTERS = " \n\r\f\t(){}[];,+-*/%$!=<>&|"


class Tokenizer:
    def __init__(self, input: str) -> None:
        self.input = list(input)

    def __iter__(self) -> Iterator[Token]:
        return self

    def read_identifier(self, token_type: TokenType, start: str) -> Token:
        var_name = start
        while self.input[0] in IDENTIFIER_CHARS:
            var_name += self.input.pop()

        return Token(
            token_type,
            var_name,
        )

    def slash(self):
        if self.input[0] == "/":
            # One line comment
            comment_text = "/"
            while self.input[0] != "\n":
                comment_text += self.input.pop()
            return Token(
                TokenType.COMMENT,
                comment_text,
            )
        elif self.input[0] == "*":
            self.input.pop()
            comment_text = "/*"

            prev_star = False

            while not prev_star or self.input[0] != "/":
                char = self.input.pop()
                if char == "*":
                    prev_star = True
                else:
                    prev_star = False
                comment_text += char

            self.input.pop()
            comment_text += "/"
            return Token(
                TokenType.COMMENT,
                comment_text,
            )
        else:
            return Token(
                TokenType.OPERATOR_DIVIDE,
                "/",
            )

    def float(self, start: str) -> Token:
        """Read a float, after the decimal point"""
        num = start
        while self.input[0] in digits:
            num += self.input.pop()

        # Exponent
        if self.input[0] == "e":
            num += self.input.pop()

            if self.input[0] in ["-", "+"]:
                num += self.input.pop()

            read_digits = False

            while self.input[0] in digits:
                num += self.input.pop()
                read_digits = True

            if not read_digits:
                return Token(
                    TokenType.ERROR,
                    num,
                    "Invalid exponent"
                )
        return Token(
            TokenType.LITERAL_NUMBER_FLOAT,
            num,
        )

    def get_next_token(self) -> Token:
        ...
        if len(self.input) == 0:
            raise StopIteration()

        # Discard whitespace
        while self.input[0] in whitespace:
            self.input.pop()

        if self.input[0] == "/":
            self.input.pop()
            return self.slash()

        elif self.input[0] == "$":
            # $$ capture operator
            if self.input[0] == "$":
                self.input.pop()
                return Token(
                    TokenType.OPERATOR_CAPTURE,
                    "$$"
                )

            if self.input[0] not in IDENTIFIER_CHARS:
                # No actual variable name read, not a valid token
                return Token(
                    TokenType.ERROR,
                    "$",
                    "$ without associated identifier",
                )

            return self.read_identifier(
                TokenType.VARIABLE,
                "$",
            )

        elif self.input[0] == ":":
            self.input.pop()
            if self.input[0] == "=":
                self.input.pop()
                return Token(
                    TokenType.OPERATOR_ASSIGN,
                    ":=",
                )
            else:
                return Token(
                    TokenType.ERROR,
                    ":",
                )

        elif self.input[0] == ",":
            self.input.pop()
            return Token(
                TokenType.OPERATOR_COMMA,
                ",",
            )

        elif self.input[0] == "|":
            self.input.pop()
            if self.input[0] == "|":
                self.input.pop()
                return Token(
                    TokenType.OPERATOR_BOOLEAN_OR,
                    "||"
                )
            else:
                return Token(
                    TokenType.OPERATOR_PIPE,
                    "|",
                )

        elif self.input[0] == "&":
            self.input.pop()
            if self.input[0] == "&":
                self.input.pop()
                return Token(
                    TokenType.OPERATOR_BOOLEAN_AND,
                    "&&"
                )
            else:
                return Token(
                    TokenType.OPERATOR_JOIN,
                    "&",
                )

        elif self.input[0] == "-":
            self.input.pop()
            if self.input[0] == ">":
                self.input.pop()
                return Token(
                    TokenType.OPERATOR_MAP,
                    "->",
                )
            else:
                return Token(
                    TokenType.OPERATOR_SUBTRACT,
                    "-",
                )

        elif self.input[0] == "=":
            self.input.pop()
            if self.input[0] == "=":
                self.input.pop()
                return Token(
                    TokenType.CONDITIONAL_EQUALITY,
                    "==",
                )
            else:
                return Token(
                    TokenType.OPERATOR_EQUALITY,
                    "=",
                )

        elif self.input[0] == "!":
            self.input.pop()
            if self.input[0] == "=":
                self.input.pop()
                if self.input[0] == "=":
                    self.input.pop()
                    return Token(
                        TokenType.CONDITIONAL_INEQUALITY,
                        "!==",
                    )
                else:
                    return Token(
                        TokenType.OPERATOR_INEQUALITY,
                        "!=",
                    )
            else:
                return Token(
                    TokenType.OPERATOR_NOT,
                    "!",
                )

        elif self.input[0] == "+":
            self.input.pop()
            return Token(
                TokenType.OPERATOR_ADD,
                "+",
            )

        elif self.input[0] == "*":
            self.input.pop()
            return Token(
                TokenType.OPERATOR_MULTIPLY,
                "*",
            )

        elif self.input[0] == "/":
            self.input.pop()
            return Token(
                TokenType.OPERATOR_DIVIDE,
                "/",
            )

        elif self.input[0] == "%":
            self.input.pop()
            return Token(
                TokenType.OPERATOR_MOD,
                "%",
            )

        elif self.input[0] == "^":
            self.input.pop()
            return Token(
                TokenType.OPERATOR_POWER,
                "^",
            )

        elif self.input[0] == ">":
            self.input.pop()
            if self.input[0] == "=":
                self.input.pop()
                return Token(
                    TokenType.CONDITIONAL_GREATER_EQUAL,
                    ">=",
                )
            else:
                return Token(
                    TokenType.CONDITIONAL_GREATER,
                    ">",
                )

        elif self.input[0] == "<":
            self.input.pop()
            if self.input[0] == "=":
                self.input.pop()
                return Token(
                    TokenType.CONDITIONAL_LESS_EQUAL,
                    "<=",
                )
            else:
                return Token(
                    TokenType.CONDITIONAL_LESS,
                    "<",
                )

        elif self.input[0] == '"' or self.input[0] == "'":
            string_contents = self.input.pop()

            while self.input[0] != string_contents[0] or self.input[0] != '\n':
                string_contents += self.input.pop()

            if string_contents[0] != string_contents[-1]:
                return Token(
                    TokenType.ERROR,
                    string_contents,
                    "Unterminated string literal",
                )
            else:
                return Token(
                    TokenType.LITERAL_STRING,
                    string_contents,
                )

        elif self.input[0] == "0":
            self.input.pop()
            # Hexadecimal
            if self.input[0] == "x":
                num = "0x"
                while self.input[0] in hexdigits:
                    num += self.input.pop()
                return Token(
                    TokenType.LITERAL_NUMBER_HEX,
                    num,
                )
            # Octal
            if self.input[0] == "o":
                num = "0o"
                while self.input[0] in octdigits:
                    num += self.input.pop()
                return Token(
                    TokenType.LITERAL_NUMBER_OCT,
                    num,
                )
            # Binary
            if self.input[0] == "b":
                num = "0b"
                while self.input[0] in BINARY_DIGITS:
                    num += self.input.pop()
                return Token(
                    TokenType.LITERAL_NUMBER_BIN,
                    num,
                )
            # Decimal
            if self.input[0] == ".":
                self.input.pop()
                return self.float("0.")

            return Token(
                TokenType.LITERAL_NUMBER_DEC,
                "0",
            )

        elif self.input[0] == ".":
            # In this case, we need at least one decimal
            if self.input[0] in digits:
                return self.float(".")
            else:
                return Token(
                    TokenType.ERROR,
                    ".",
                    "Invalid float literal",
                )

        elif self.input[0] in digits:
            num = self.input.pop()
            while self.input[0] in digits:
                num += self.input.pop()

            # Check for a float
            if self.input[0] in [".", "e"]:
                return self.float(num)

            # Otherwise, it's a decimal
            return Token(
                TokenType.LITERAL_NUMBER_DEC,
                num,
            )

        elif self.input[0] in IDENTIFIER_START_CHARS:
            return self.read_identifier(TokenType.UNKNOWN, "")

        else:
            return Token(
                TokenType.ERROR,
                self.input.pop(),
                "Unrecognised token",
            )

    def __next__(self) -> Token:
        next_token = self.get_next_token()

        # Check that next character is a separator
        extra_chars = ""

        # If the previous token ends in a separator char, we should return it
        if next_token.string[-1] in SEPARATOR_CHARACTERS:
            return next_token

        while self.input[0] not in SEPARATOR_CHARACTERS:
            extra_chars += self.input.pop()

        if extra_chars:
            # There were extra characters, meaning it's invalid syntax
            return Token(
                TokenType.ERROR,
                next_token.string + extra_chars,
                next_token.notes if next_token.notes else "Invalid syntax",
            )
        else:
            return next_token
