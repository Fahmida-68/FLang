# tokens.py

# Token Types Constants
TOKEN_INT        = 'INT'
TOKEN_PLUS       = 'PLUS'
TOKEN_MINUS      = 'MINUS'
TOKEN_MUL        = 'MUL'
TOKEN_DIV        = 'DIV'
TOKEN_EOF        = 'EOF'

# Comparison & Assignment Operators
TOKEN_EQUALS     = 'EQUALS'       # =
TOKEN_EE         = 'EE'           # ==
TOKEN_LT         = 'LT'           # <
TOKEN_LBRACE     = 'LBRACE'       # {
TOKEN_RBRACE     = 'RBRACE'       # }
TOKEN_LPAREN     = 'LPAREN'       # (
TOKEN_RPAREN     = 'RPAREN'       # )

# FLang Keywords Mapping
TOKEN_IDENTIFIER = 'IDENTIFIER'   # For variable names like a, b, x
TOKEN_STRING     = 'STRING'       # For text inside quotes like "Hello World"
TOKEN_KEYWORD    = 'KEYWORD'      # For structural keywords

# List of registered Keywords 
KEYWORDS = [
    'shuru',
    'flang',
    'shesh',
    'bol',
    'rakho',
    'jotokkhon',
    'jodi',
    'natho'
]

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None: 
            return f'{self.type}:{self.value}'
        return f'{self.type}'
