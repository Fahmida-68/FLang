# tokens.py
TOKEN_INT = 'INT'
TOKEN_STRING = 'STRING'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_KEYWORD = 'KEYWORD'
TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_MUL = 'MUL'
TOKEN_DIV = 'DIV'
TOKEN_EQUALS = 'EQUALS'
TOKEN_EE = 'EE'
TOKEN_LT = 'LT'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'
TOKEN_LBRACE = 'LBRACE'
TOKEN_RBRACE = 'RBRACE'
TOKEN_EOF = 'EOF'

KEYWORDS = ['shuru', 'flang', 'shesh', 'bol', 'rakho', 'jodi', 'natho', 'jotokkhon']

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None: return f'{self.type}:{self.value}'
        return f'{self.type}'
