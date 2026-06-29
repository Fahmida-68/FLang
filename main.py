from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_code(input_text):
    try:
        lexer = Lexer(input_text)
        tokens = lexer.make_tokens()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        output = interpreter.visit(ast)
        return output
    except Exception as e:
        return f"[Compiler Error]: {str(e)}"
