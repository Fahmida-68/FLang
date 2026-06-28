# lexer.py
from tokens import Token, TOKEN_INT, TOKEN_PLUS, TOKEN_MINUS, TOKEN_MUL, TOKEN_DIV, TOKEN_PRINT, TOKEN_EOF

def lexer(filename):
    with open(filename, 'r') as f:
        text = f.read()

    tokens = []
    pos = 0
    while pos < len(text):
        char = text[pos]

        # Space, Tab, Newline skip korar jonno
        if char in ' \t\n\r':
            pos += 1
            continue
        
        # KEYWORD CHECK: "bol" keyword khujchi print korar jonno
        if text[pos:pos+3] == "bol" and (pos+3 >= len(text) or text[pos+3] in ' \t\n\r'):
            tokens.append(Token(TOKEN_PRINT))
            pos += 3
            continue

        # Operators Check
        if char == '+':
            tokens.append(Token(TOKEN_PLUS))
            pos += 1
        elif char == '-':
            tokens.append(Token(TOKEN_MINUS))
            pos += 1
        elif char == '*':
            tokens.append(Token(TOKEN_MUL))
            pos += 1
        elif char == '/':
            tokens.append(Token(TOKEN_DIV))
            pos += 1
        
        # Number Check (Multiple digits handle korar jonno loop)
        elif char.isdigit():
            num = ''
            while pos < len(text) and text[pos].isdigit():
                num += text[pos]
                pos += 1
            tokens.append(Token(TOKEN_INT, int(num)))
        else:
            # Jodi emon kichu pay jeta amader syntax e nai
            print(f"[Lexer Error]: Invalid character '{char}' at position {pos}")
            pos += 1
            
    tokens.append(Token(TOKEN_EOF))
    return tokens