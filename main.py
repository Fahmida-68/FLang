# main.py
import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_code(source_code):
    try:
        lexer = Lexer(source_code)
        tokens = lexer.make_tokens()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        interpreter.execute(ast)
        
        return "\n".join(interpreter.console_output)
    except Exception as e:
        return f"[Compiler Error]: {str(e)}"

if __name__ == '__main__':
    # Standard runtime sequence reading standalone .fl files locally via console terminal
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            code = file.read()
        print(run_code(code))
    else:
        print("FLang Engine Active. Run with filename parameter blueprint (e.g., python main.py program.fl)")
