# interpreter.py
from tokens import *
from parser import *

class Interpreter:
    def __init__(self):
        self.global_memory = {}
        self.console_output = []

    def execute(self, node):
        if isinstance(node, ProgramNode):
            for stmt in node.statements:
                self.execute(stmt)
        elif isinstance(node, PrintNode):
            val = self.evaluate(node.expr)
            self.console_output.append(str(val))
        elif isinstance(node, VarAssignNode):
            val = self.evaluate(node.value_node)
            self.global_memory[node.var_name] = val
        elif isinstance(node, WhileNode):
            while self.evaluate(node.condition):
                for stmt in node.body:
                    self.execute(stmt)
        elif isinstance(node, IfNode):
            if self.evaluate(node.condition):
                for stmt in node.body: self.execute(stmt)
            elif node.elif_condition and self.evaluate(node.elif_condition):
                for stmt in node.elif_body: self.execute(stmt)

    def evaluate(self, node):
        if isinstance(node, LiteralNode):
            return node.token.value
        elif isinstance(node, VarAccessNode):
            if node.var_name in self.global_memory:
                return self.global_memory[node.var_name]
            raise Exception(f"Runtime Error: Variable '{node.var_name}' data reference missing.")
        elif isinstance(node, BinOpNode):
            left_val = self.evaluate(node.left)
            right_val = self.evaluate(node.right)
            op = node.op_tok.type
            if op == TOKEN_PLUS: return left_val + right_val
            if op == TOKEN_MINUS: return left_val - right_val
            if op == TOKEN_MUL: return left_val * right_val
            if op == TOKEN_DIV: return left_val // right_val
            if op == TOKEN_EE: return left_val == right_val
            if op == TOKEN_LT: return left_val < right_val
        return None
