# main.py
from interpreter import run
from lexer import lexer
from parser import parse

print("====== TOKENS ======\n")
tokens = lexer("program.fl")
for token in tokens:
    print(token)

print("\n====== PARSER ======\n")
syntax_ok = parse("program.fl")

if syntax_ok:
    print("\n====== OUTPUT ======\n")
    run("program.fl")