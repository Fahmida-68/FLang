# parser.py
from tokens import *

class ASTNode: pass

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

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

class BinOpNode(ASTNode):
    def __init__(self, left, op_tok, right):
        self.left = left
        self.op_tok = op_tok
        self.right = right

class LiteralNode(ASTNode):
    def __init__(self, token):
        self.token = token

class VarAccessNode(ASTNode):
    def __init__(self, var_name):
        self.var_name = var_name

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        self.current_tok = self.tokens[self.tok_idx] if self.tok_idx < len(self.tokens) else None

    def parse(self):
        statements = []
        while self.current_tok.type != TOKEN_EOF:
            if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'shuru':
                self.advance()
                if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'flang':
                    self.advance()
                    continue
            elif self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'shesh':
                self.advance()
                if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'flang':
                    self.advance()
                    break
            
            stmt = self.statement()
            if stmt: statements.append(stmt)
            
        return ProgramNode(statements)

    def statement(self):
        if self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'bol':
            self.advance()
            expr = self.expr()
            return PrintNode(expr)
            
        elif self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'rakho':
            self.advance()
            if self.current_tok.type != TOKEN_IDENTIFIER:
                raise Exception("Expected identifier after 'rakho'")
            var_name = self.current_tok.value
            self.advance()
            if self.current_tok.type != TOKEN_EQUALS:
                raise Exception("Expected '=' after variable name")
            self.advance()
            value = self.expr()
            return VarAssignNode(var_name, value)
            
        elif self.current_tok.type == TOKEN_IDENTIFIER:
            var_name = self.current_tok.value
            self.advance()
            if self.current_tok.type != TOKEN_EQUALS:
                raise Exception("Expected '=' for assignment")
            self.advance()
            value = self.expr()
            return VarAssignNode(var_name, value)
            
        elif self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'jotokkhon':
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
                stmt = self.statement()
                if stmt: body.append(stmt)
            self.advance()
            return WhileNode(condition, body)
            
        elif self.current_tok.type == TOKEN_KEYWORD and self.current_tok.value == 'jodi':
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
                stmt = self.statement()
                if stmt: body.append(stmt)
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
                    stmt = self.statement()
                    if stmt: elif_body.append(stmt)
                self.advance()
            return IfNode(condition, body, elif_cond, elif_body)
            
        elif self.current_tok.type in [TOKEN_EOF, TOKEN_RBRACE]:
            return None
        else:
            raise Exception(f"Unexpected token: {self.current_tok}")

    def expr(self):
        left = self.term()
        while self.current_tok.type in (TOKEN_PLUS, TOKEN_MINUS, TOKEN_EE, TOKEN_LT):
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
        elif tok.type == TOKEN_LPAREN:
            self.advance()
            expr = self.expr()
            if self.current_tok.type == TOKEN_RPAREN:
                self.advance()
                return expr
            raise Exception("Expected ')'")
        raise Exception(f"Expected number, string or variable, got {tok}")
