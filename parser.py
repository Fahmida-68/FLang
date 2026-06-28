# parser.py
from lexer import lexer
from tokens import TOKEN_PRINT, TOKEN_INT, TOKEN_EOF

def parse(filename):
    tokens = lexer(filename)
    
    # Ekta basic grammar validation checks
    if len(tokens) > 0 and tokens[0].type != TOKEN_PRINT:
        print("[Parser Error]: Program must start with 'bol' keyword.")
        return False
        
    print("[Parser Success]: Code syntax analysis complete without any error.")
    return True