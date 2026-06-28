# tokens.py

# Token Types Constants
TOKEN_INT    = 'INT'
TOKEN_PLUS   = 'PLUS'
TOKEN_MINUS  = 'MINUS'
TOKEN_MUL    = 'MUL'
TOKEN_DIV    = 'DIV'
TOKEN_PRINT  = 'PRINT'
TOKEN_EOF    = 'EOF'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None: return f'{self.type}:{self.value}'
        return f'{self.type}'