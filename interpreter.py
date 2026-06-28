# interpreter.py
from lexer import lexer
from tokens import TOKEN_PRINT, TOKEN_INT, TOKEN_PLUS, TOKEN_MINUS, TOKEN_MUL, TOKEN_DIV

def run(filename):
    tokens = lexer(filename)
    
    if not tokens or tokens[0].type != TOKEN_PRINT:
        return

    # Calculator Engine Logic
    idx = 1
    if idx < len(tokens) and tokens[idx].type == TOKEN_INT:
        result = tokens[idx].value
        idx += 1
        
        while idx < len(tokens):
            op = tokens[idx]
            if op.type in [TOKEN_PLUS, TOKEN_MINUS, TOKEN_MUL, TOKEN_DIV]:
                idx += 1
                if idx < len(tokens) and tokens[idx].type == TOKEN_INT:
                    next_val = tokens[idx].value
                    if op.type == TOKEN_PLUS: result += next_val
                    elif op.type == TOKEN_MINUS: result -= next_val
                    elif op.type == TOKEN_MUL: result *= next_val
                    elif op.type == TOKEN_DIV: 
                        if next_val == 0:
                            print("[Runtime Error]: Division by zero!")
                            return
                        result //= next_val # Integer division
                idx += 1
            else:
                break
        print(f"Output: {result}")