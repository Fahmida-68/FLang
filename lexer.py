# lexer.py
from tokens import *

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t\n\r':
                self.advance()
            elif self.current_char.isdigit():
                tokens.append(self.make_number())
            elif self.current_char.isalpha():
                tokens.append(self.make_identifier())
            elif self.current_char == '"' or self.current_char == "'":
                tokens.append(self.make_string())
            elif self.current_char == '+':
                tokens.append(Token(TOKEN_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TOKEN_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TOKEN_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TOKEN_DIV))
                self.advance()
            elif self.current_char == '=':
                tokens.append(self.make_equals())
            elif self.current_char == '<':
                tokens.append(Token(TOKEN_LT))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TOKEN_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TOKEN_RPAREN))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TOKEN_LBRACE))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TOKEN_RBRACE))
                self.advance()
            else:
                raise Exception(f"Illegal Character: '{self.current_char}'")
        
        tokens.append(Token(TOKEN_EOF))
        return tokens

    def make_number(self):
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return Token(TOKEN_INT, int(num_str))

    def make_string(self):
        quote_char = self.current_char
        string_str = ''
        self.advance()
        while self.current_char is not None and self.current_char != quote_char:
            string_str += self.current_char
            self.advance()
        self.advance()
        return Token(TOKEN_STRING, string_str)

    def make_identifier(self):
        id_str = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            id_str += self.current_char
            self.advance()
        tok_type = TOKEN_KEYWORD if id_str in KEYWORDS else TOKEN_IDENTIFIER
        return Token(tok_type, id_str)

    def make_equals(self):
        self.advance()
        if self.current_char == '=':
            self.advance()
            return Token(TOKEN_EE)
        return Token(TOKEN_EQUALS)
