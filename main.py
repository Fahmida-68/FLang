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
        interpreter.visit(ast)
        
        if hasattr(interpreter, 'console_output') and interpreter.console_output:
            return "\n".join(str(x) for x in interpreter.console_output)
        return "Program executed successfully (No output)."
        
    except Exception as e:
        return f"[Compiler Error]: {str(e)}"
