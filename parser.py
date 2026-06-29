# parser.py
from tokens import *

class ASTNode: pass
class ProgramNode(ASTNode):
    def __init__(self, statements): self.statements = statements
class PrintNode(ASTNode):
    def __init__(self, expr): self.expr = expr
class VarAssignNode(ASTNode):
    def __init__(self, var_name, value_node):
        self.var_name = var_name
        self.value_node = value_node
class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
class IfNode(ASTNode):
    def __init__(self, condition, body, elif_condition=None, elif_body=None):
        self.condition = condition
        self.body = body
        self.elif_condition = elif_condition
        self.elif_body = elif_body
class VarAccessNode(ASTNode):
    def __init__(self, var_name): self.var_name = var_name
class LiteralNode(ASTNode):
    def __init__(self, token): self.token = token
class BinOpNode(ASTNode):
    def __init__(self, left, op_tok, right):
        self.left = left
        self.op_tok = op_tok
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = 0
        self.current_tok = self.tokens[self.tok_idx]

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

    def parse(self):
        statements = []
        if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'shuru':
            self.advance()
            if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'flang':
                self.advance()
            else: raise Exception("Expected 'flang' after 'shuru'")
        else: raise Exception("Program must start with 'shuru flang'")

        while not (self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'shesh'):
            if self.current_tok.type == TOKEN_EOF:
                raise Exception("Missing 'shesh flang' boundary.")
            stmt = self.statement()
            if stmt: statements.append(stmt)

        self.advance()
        if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'flang':
            self.advance()
        return ProgramNode(statements)

    def statement(self):
        tok = self.current_tok
        if tok.type == TOKEN_KEYWORD:
            if tok.value == 'bol':
                self.advance()
                return PrintNode(self.expr())
            elif tok.value == 'rakho':
                self.advance()
                if self.current_tok.type != TOKEN_IDENTIFIER: raise Exception("Expected variable name")
                var_name = self.current_tok.value
                self.advance()
                if self.current_tok.type != TOKEN_EQUALS: raise Exception("Expected '='")
                self.advance()
                return VarAssignNode(var_name, self.expr())
            elif tok.value == 'jotokkhon':
                self.advance()
                if self.current_tok.type != TOKEN_LPAREN: raise Exception("Expected '('")
                self.advance()
                condition = self.expr()
                if self.current_tok.type != TOKEN_RPAREN: raise Exception("Expected ')'")
                self.advance()
                if self.current_tok.type != TOKEN_LBRACE: raise Exception("Expected '{'")
                self.advance()
                body = []
                while not (self.current_tok.type == TOKEN_RBRACE):
                    body.append(self.statement())
                self.advance()
                return WhileNode(condition, body)
            elif tok.value == 'jodi':
                self.advance()
                if self.current_tok.type != TOKEN_LPAREN: raise Exception("Expected '('")
                self.advance()
                condition = self.expr()
                if self.current_tok.type != TOKEN_RPAREN: raise Exception("Expected ')'")
                self.advance()
                if self.current_tok.type != TOKEN_LBRACE: raise Exception("Expected '{'")
                self.advance()
                body = []
                while not (self.current_tok.type == TOKEN_RBRACE):
                    body.append(self.statement())
                self.advance()
                
                elif_cond, elif_body = None, None
                if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'natho':
                    self.advance()
                    if self.current_tok.type != TOKEN_LPAREN: raise Exception("Expected '('")
                    self.advance()
                    elif_cond = self.expr()
                    if self.current_tok.type != TOKEN_RPAREN: raise Exception("Expected ')'")
                    self.advance()
                    if self.current_tok.type != TOKEN_LBRACE: raise Exception("Expected '{'")
                    self.advance()
                    elif_body = []
                    while not (self.current_tok.type == TOKEN_RBRACE):
                        elif_body.append(self.statement())
                    self.advance()
                return IfNode(condition, body, elif_cond, elif_body)
        
        if tok.type == TOKEN_IDENTIFIER:
            var_name = tok.value
            self.advance()
            if self.current_tok.type == TOKEN_EQUALS:
                self.advance()
                return VarAssignNode(var_name, self.expr())
        raise Exception(f"Invalid statement: {tok}")

    def expr(self):
        left = self.comp_expr()
        while self.current_tok.type in (TOKEN_PLUS, TOKEN_MINUS):
            op_tok = self.current_tok
            self.advance()
            right = self.comp_expr()
            left = BinOpNode(left, op_tok, right)
        return left

    def comp_expr(self):
        left = self.term()
        while self.current_tok.type in (TOKEN_EE, TOKEN_LT):
            op_tok = self.current_tok
            self.advance()
            right = self.term()
            left = BinOpNode(left, op_tok, right)
        return left

    def term(self):
        left = self.factor()
        while self.current_tok.type in (TOKEN_MUL, TOKEN_DIV):
            op_tok = self.current_tok
            self.advance()
            right = self.factor()
            left = BinOpNode(left, op_tok, right)
        return left

    def factor(self):
        tok = self.current_tok
        if tok.type in (TOKEN_INT, TOKEN_STRING):
            self.advance()
            return LiteralNode(tok)
        elif tok.type == TOKEN_IDENTIFIER:
            self.advance()
            return VarAccessNode(tok.value)
        raise Exception(f"Invalid factor token: {tok}")