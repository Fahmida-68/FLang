# main.py
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
        
        # ১. ইন্টারপ্রিটারে আসলে কোন মেথডটি আছে তা চেক করা হচ্ছে
        if hasattr(interpreter, 'execute'):
            output = interpreter.execute(ast)
        elif hasattr(interpreter, 'visit'):
            output = interpreter.visit(ast)
        else:
            return "[Compiler Error]: Interpreter ক্লাসে execute বা visit কোনো মেথডই খুঁজে পাওয়া যায়নি।"
            
        # ২. যদি ইন্টারপ্রিটার সরাসরি কিছু রিটার্ন না করে console_output লিস্টে ডাটা রাখে
        if hasattr(interpreter, 'console_output') and interpreter.console_output:
            return "\n".join(str(x) for x in interpreter.console_output)
            
        return str(output) if output is not None else "Program executed successfully."
        
    except Exception as e:
        return f"[Compiler Error]: {str(e)}"
