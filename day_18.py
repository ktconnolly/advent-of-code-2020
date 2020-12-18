import operator

from utils import read_lines

EOF = "\0"
LOWEST_PRECEDENCE = -1
OPS = {"+": operator.add, "*": operator.mul}


class Token:
    EOF = "EOF"
    INT = "INT"
    PLUS = "+"
    ASTERISK = "*"
    LPAREN = "("
    RPAREN = ")"

    def __init__(self, token_type, literal):
        self.token_type = token_type
        self.literal = literal

    def __str__(self):
        return self.literal


class InfixExpression:
    def __init__(self, left, op):
        self.left = left
        self.operator = op
        self.right = None

    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"


class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.read_position = 0
        self.ch = ""

        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.code):
            self.ch = EOF
        else:
            self.ch = self.code[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        self.skip_whitespace()

        if self.ch == "+":
            tok = Token(Token.PLUS, self.ch)
        elif self.ch == "*":
            tok = Token(Token.ASTERISK, self.ch)
        elif self.ch == "(":
            tok = Token(Token.LPAREN, self.ch)
        elif self.ch == ")":
            tok = Token(Token.RPAREN, self.ch)
        elif self.ch == EOF:
            tok = Token(Token.EOF, "")
        elif self.ch.isdigit():
            return Token(Token.INT, self.read_number())
        else:
            raise Exception(f"Unknown char {self.ch}")

        self.read_char()
        return tok

    def read_number(self):
        pos = self.position
        while self.ch.isdigit():
            self.read_char()

            if self.ch == EOF:
                break

        return self.code[pos: self.position]

    def skip_whitespace(self):
        if self.ch == EOF:
            return

        while self.ch.isspace():
            self.read_char()


class Parser:
    def __init__(self, lexer, precedences):
        self.lexer = lexer
        self.precedences = precedences

        self.curr_token = lexer.next_token()
        self.peek_token = lexer.next_token()

        self.prefix_parse_fns = {}
        self.infix_parse_fns = {}

        self.register_prefix(Token.INT, self.parse_int)
        self.register_prefix(Token.LPAREN, self.parse_grouped_expression)
        self.register_infix(Token.PLUS, self.parse_infix_expression)
        self.register_infix(Token.ASTERISK, self.parse_infix_expression)

    def parse_program(self):
        program = []
        while not self.is_current(Token.EOF):
            program.append(self.parse_expression())
            self.next_token()

        return program

    def parse_expression(self, precedence=LOWEST_PRECEDENCE):
        prefix = self.prefix_parse_fns.get(self.curr_token.token_type)

        left_exp = prefix()

        while precedence < self.peek_precedence():
            infix = self.infix_parse_fns.get(self.peek_token.token_type)
            self.next_token()
            left_exp = infix(left_exp)

        return left_exp

    def parse_int(self):
        return int(self.curr_token.literal)

    def parse_infix_expression(self, left):
        op = self.curr_token.literal
        exp = InfixExpression(left, op)
        precedence = self.curr_precedence()
        self.next_token()
        exp.right = self.parse_expression(precedence)
        return exp

    def parse_grouped_expression(self):
        self.next_token()
        exp = self.parse_expression()
        return exp if self.expect_peek(Token.RPAREN) else None

    def expect_peek(self, token_type):
        if self.is_peek(token_type):
            self.next_token()
            return True
        return False

    def is_current(self, token_type):
        return self.curr_token.token_type == token_type

    def is_peek(self, token_type):
        return self.peek_token.token_type == token_type

    def peek_precedence(self):
        return self.precedences.get(self.peek_token.token_type, LOWEST_PRECEDENCE)

    def curr_precedence(self):
        return self.precedences.get(self.curr_token.token_type, LOWEST_PRECEDENCE)

    def next_token(self):
        self.curr_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def register_prefix(self, token_type, fn):
        self.prefix_parse_fns[token_type] = fn

    def register_infix(self, token_type, fn):
        self.infix_parse_fns[token_type] = fn


def evaluate(node):
    if isinstance(node, int):
        return node

    if isinstance(node, InfixExpression):
        left = evaluate(node.left)
        right = evaluate(node.right)
        operation = OPS.get(node.operator)
        return operation(left, right)


def run(program, precedences):
    lexer = Lexer(program)
    parser = Parser(lexer, precedences)

    result = None
    for stmt in parser.parse_program():
        result = evaluate(stmt)

    return result


def part_one():
    precedences = {
        Token.PLUS: 0,
        Token.ASTERISK: 0,
        Token.LPAREN: 1,
    }

    return sum(run(program, precedences) for program in read_lines(day=18))


def part_two():
    precedences = {
        Token.PLUS: 1,
        Token.ASTERISK: 0,
        Token.LPAREN: 2,
    }

    return sum(run(program, precedences) for program in read_lines(day=18))


assert part_one() == 69490582260
assert part_two() == 362464596624526
