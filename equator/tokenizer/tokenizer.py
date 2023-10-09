
from typing import Iterator
from .token import Token, TokenType
from string import ascii_letters, whitespace, digits


VARIABLE_CHARS = ascii_letters + digits + "_"


class Tokenizer:
    def __init__(self, input: str) -> None:
        self.input = list(input)

    def __iter__(self) -> Iterator[Token]:
        return self

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

    def __next__(self) -> Token:
        if len(self.input) == 0:
            raise StopIteration()

        # Discard whitespace
        while self.input[0] in whitespace:
            self.input.pop()

        if self.input[0] == "/":
            self.input.pop()
            return self.slash()

        elif self.input[0] == "$":
            var_name = self.input.pop()

            # $$ capture operator
            if self.input[0] == "$":
                self.input.pop()
                return Token(
                    TokenType.OPERATOR_CAPTURE,
                    "$$"
                )

            while self.input[0] in VARIABLE_CHARS:
                var_name += self.input.pop()

            return Token(
                TokenType.VARIABLE,
                var_name,
            )

        else:
            return Token(
                TokenType.ERROR,
                self.input.pop()
            )
