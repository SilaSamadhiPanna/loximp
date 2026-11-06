import sys

#token types
LEFT_PARENTHESES = "LEFT_PARENTHESES"
RIGHT_PARENTHESES = "RIGHT_PARENTHESES"
LEFT_BRACE = "LEFT_BRACE"
RIGHT_BRACE = "RIGHT_BRACE"

COMMA = "COMMA"
DOT = "DOT"
SEMICOLON = "SEMICOLON"

PLUS = "PLUS"
MINUS = "MINUS"
STAR = "STAR"
SLASH = "SLASH"

BANG = "BANG"
BANG_EQUAL = "BANG_EQUAL"

EQUAL = "EQUAL"
EQUAL_EQUAL = "EQUAL_EQUAL"

LESS = "LESS"
LESS_EQUAL = "LESS_EQUAL"

GREATER = "GREATER"
GREATER_EQUAL = "GREATER_EQUAL"

NUMBER = "NUMBER"
STRING = "STRING"
IDENTIFIER = "IDENTIFIER"

AND = "AND"
ELSE = "ELSE"
FALSE = "FALSE"
FOR = "FOR"
IF = "IF"
OR = "OR"
PRINT = "PRINT"
RETURN = "RETURN"
TRUE = "TRUE"
VAR = "VAR"
WHILE = "WHILE"
NIL = "NIL"

EOF = "EOF"

KEYWORDS = {
    "and": AND,
    "else": ELSE,
    "false": FALSE,
    "for": FOR,
    "if": IF,
    "or": OR,
    "print": PRINT,
    "return": RETURN,
    "true": TRUE,
    "var": VAR,
    "while": WHILE,
    "nil": NIL
}

class Expression:
    pass

class Statement:
    pass

class ExpressionStatement(Statement):
    def __init__(self, expression):
        self.expression = expression

class PrintStatement(Statement):
    def __init__(self, expression):
        self.expression = expression

class Literal(Expression):
    def __init__(self, value):
        self.value = value

class Grouping(Expression):
    def __init__(self, expression):
        self.expression = expression

class Unary(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

class Binary(Expression):
    def __init__(self, left, token, right):
        self.left = left
        self.token = token
        self.right = right

# --- start AI code ---

class ASTPrinter:

    def print_expression(self, expression):

        if isinstance(expression, Literal):

            if expression.value is None:
                return "NIL"

            elif expression.value is True:
                return "TRUE"

            elif expression.value is False:
                return "FALSE"

            return str(expression.value)
        
        elif isinstance(expression, Grouping):
            inner = self.print_expression(expression.expression)
            groupstring = "(GROUP " + inner + ")"
            return groupstring

        elif isinstance(expression, Unary):
            operand = self.print_expression(expression.operand)
            operator = expression.operator.lexeme
            unarystring = "(" + operator + " " + operand + ")"
            return unarystring

        elif isinstance(expression, Binary):
            left = self.print_expression(expression.left)
            operator = expression.token.lexeme
            right = self.print_expression(expression.right)
            binarystring = "(" + operator + " " + left + " " + right + ")"
            return binarystring
        
        else:
            print("UNKNOWN TYPE ERROR")
        
# --- end AI code ---

class Token:
    def __init__(self, token_type, lexeme, literal, line):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []

        self.had_error = False

        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(EOF, "", None, self.line))

        return self.tokens

    def is_at_end(self):
        return self.current >= len(self.source)    

    def advance(self):
        character = self.source[self.current]
        self.current = self.current +1
        return character


    def scan_token(self):
        character = self.advance()

        if character == "(":
            self.add_token(LEFT_PARENTHESES)

        elif character == ")":
            self.add_token(RIGHT_PARENTHESES)

        elif character == "{":
            self.add_token(LEFT_BRACE)

        elif character == "}":
            self.add_token(RIGHT_BRACE)

        elif character == ",":
            self.add_token(COMMA)

        elif character == ".":
            self.add_token(DOT)

        elif character == "-":
            self.add_token(MINUS)

        elif character == "+":
            self.add_token(PLUS)

        elif character == ";":
            self.add_token(SEMICOLON)

        elif character == "*":
            self.add_token(STAR)

        elif character == "!":
            if self.match("="):
                self.add_token(BANG_EQUAL)
            else:
                self.add_token(BANG)     

        elif character == "=":
            if self.match("="):
                self.add_token(EQUAL_EQUAL)
            else:
                self.add_token(EQUAL)

        elif character == "<":
            if self.match("="):
                self.add_token(LESS_EQUAL)
            else:
                self.add_token(LESS)

        elif character == ">":
            if self.match("="):
                self.add_token(GREATER_EQUAL)
            else:
                self.add_token(GREATER)   

        elif character == "/":
            if self.match("/"):
                while self.peek() != "\n" and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(SLASH)  

        elif character == " ":
            pass

        elif character == "\r":
            pass

        elif character == "\t":
            pass

        elif character == "\n":
            self.line = self.line + 1   

        elif character == '"':
            self.string()
               
        elif self.is_digit(character):
            self.number()
    
        elif self.is_alpha(character):
            self.identifier()

        else:
            self.error("UNEXPECTED CHARACTER: " + character)

    def add_token(self, token_type, literal=None):
        lexeme = self.source[self.start:self.current]
        new_token = Token(token_type, lexeme, literal, self.line)
        self.tokens.append(new_token)

    def match(self, expected):
        if self.is_at_end():
            return False

        if self.source[self.current] != expected:
            return False

        self.current = self.current + 1
        return True

    def peek(self):
        if self.is_at_end():
            return "\0"

        return self.source[self.current]

    def string(self):
        while self.peek() != '"' and not self.is_at_end():

            if self.peek() == "\n":
                self.line = self.line + 1

            self.advance()

        if self.is_at_end():
            self.error("UNTERMINATED STRING.")
            return

        self.advance()

        value = self.source[self.start + 1:self.current - 1]

        self.add_token(STRING, value)

    def is_digit(self, character):
        return character >= "0" and character <= "9"

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()

            while self.is_digit(self.peek()):
                self.advance()

        value = float(self.source[self.start:self.current])

        self.add_token(NUMBER, value)

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"

        return self.source[self.current + 1]

    def is_alpha(self, character):
        return (
            (character >= "a" and character <= "z")
            or (character >= "A" and character <= "Z")
            or character == "_"
        )    
   
    def is_alpha_numeric(self, character):
        return self.is_alpha(character) or self.is_digit(character)

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        text = self.source[self.start:self.current]

        if text in KEYWORDS:
            self.add_token(KEYWORDS[text])
        else:
            self.add_token(IDENTIFIER)

    def error(self, message):
        self.had_error = True
        print("[LINE", self.line, "] SCANNER ERROR:", message)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.had_error = False

    def parse(self):

        statements = []
        
        while not self.is_at_end():
            try:
                statements.append(self.statement())

            except ParseError as error:
                self.had_error = True
                print(error, file=sys.stderr)
                self.synchronize()

        return statements

    def statement(self):
        if self.matchtoken(PRINT):
            return self.print_statement()
        
        return self.expression_statement()

    def synchronize(self):
        if self.is_at_end():
            return
        
        if self.peek().token_type == PRINT:
            return

        self.advance()

        while not self.is_at_end():
            if self.previous().token_type == SEMICOLON:
                return
            
            if self.peek().token_type == PRINT:
                return

            self.advance()

    def print_statement(self):
        value = self.expression()
        self.consume(SEMICOLON, "EXPECT ';' AFTER VALUE.")
        return PrintStatement(value)

    def expression_statement(self):
        expr = self.expression()
        self.consume(SEMICOLON, "EXPECT ';' AFTER EXPRESSION.")
        return ExpressionStatement(expr)

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def is_at_end(self):
        return self.peek().token_type == EOF

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()
    
    def check(self, token_type):
        if self.is_at_end():
            return False
        return self.peek().token_type == token_type

    def matchtoken(self, *token_types):
        for token_type in token_types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def primary(self):

        if self.matchtoken(FALSE):
            return Literal(False)

        if self.matchtoken(TRUE):
            return Literal(True)

        if self.matchtoken(NIL):
            return Literal(None)

        if self.matchtoken(NUMBER, STRING):
            return Literal(self.previous().literal)

        if self.matchtoken(LEFT_PARENTHESES):
            expression = self.expression()
            self.consume(RIGHT_PARENTHESES, "EXPECTED ')' AFTER EXPRESSION")
            return Grouping(expression)

        raise self.error(self.peek(), "EXPECTED EXPRESSION")

    def unary(self):

        if self.matchtoken(BANG, MINUS):
            operator = self.previous()
            operand = self.unary()
            return Unary(operator, operand)

        return self.primary()

    def factor(self):
        expr = self.unary()

        while self.matchtoken(SLASH, STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def term(self):
        expr = self.factor()

        while self.matchtoken(MINUS, PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def comparison(self):
        expr  = self.term()

        while self.matchtoken(GREATER, GREATER_EQUAL, LESS, LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        
        return expr

    def equality(self):
        expr = self.comparison()

        while self.matchtoken(BANG_EQUAL, EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr
        
    def expression(self):
        return self.equality()
    
    def consume(self, token_type, message):

        if self.check(token_type):
            return self.advance()
        
        raise self.error(self.peek(), message)

    def error(self, token, message):

        if token.token_type == EOF:
            location = "end of input"
        else:
            location = "'" + token.lexeme + "'"

        return ParseError(f"[LINE {token.line} at {location}: {message}")

class LoxRuntimeError(Exception):
    def __init__(self, token, message):
        super().__init__(message)
        self.token = token

class Evaluator:
    def evaluate(self, expression):
        if isinstance(expression, Literal):
            return expression.value
        
        elif isinstance(expression, Grouping):
            return self.evaluate(expression.expression)

        elif isinstance(expression, Unary):
            right = self.evaluate(expression.operand)
            operator = expression.operator

            if operator.token_type == MINUS:
                if isinstance(right, bool):
                    right = float(right)

                self.check_number_operand(operator, right)
                return -right

            elif operator.token_type == BANG:
                return not self.is_truthy(right)

        elif isinstance(expression, Binary):
            left = self.evaluate(expression.left)
            right = self.evaluate(expression.right)
            operator = expression.token

            if isinstance(left, bool):
                left = float(left)

            if isinstance(right, bool):
                right = float(right)

            if operator.token_type == EQUAL_EQUAL:
                return self.is_equal(left, right)

            elif operator.token_type == BANG_EQUAL:
                return not self.is_equal(left, right)

            elif operator.token_type == PLUS:
                if isinstance(left, float) and isinstance(right, float):
                    return left + right
                if isinstance(left, str) and isinstance(right, str):
                    return left + right

                raise LoxRuntimeError(operator, "OPERANDS MUST BE TWO NUMBERS OR STRINGS")

            self.check_number_operands(operator, left, right)

            if operator.token_type == MINUS:
                return left - right
            
            elif operator.token_type == SLASH:
                if right == 0.0:
                    raise LoxRuntimeError(operator, "CANNOT DIVIDE BY ZERO")
                return left / right

            elif operator.token_type == STAR:
                return left * right

            elif operator.token_type == GREATER:
                return left > right

            elif operator.token_type == GREATER_EQUAL:
                return left >= right

            elif operator.token_type == LESS:
                return left < right

            elif operator.token_type == LESS_EQUAL:
                return left <= right

    def execute(self, statement):
        if isinstance(statement, ExpressionStatement):
            self.evaluate(statement.expression)

        elif isinstance(statement, PrintStatement):
            value = self.evaluate(statement.expression)
            print(self.stringify(value))

    def interpret(self, statements):
        try:
            for statement in statements:
                self.execute(statement)

        except LoxRuntimeError as error:
            print(f"{error}\n[LINE {error.token.line}]", file=sys.stderr)

    def stringify(self, value):
        if value is None:
            return "NIL"
        
        if value is True:
            return "TRUE"

        if value is False:
            return "FALSE"
        
        if isinstance(value, float):
            text = str(value)

            if text.endswith(".0"):
                text = text[:-2]

            return text

        return str(value)

    def check_number_operand(self, operator, operand):
        if isinstance(operand, float):
            return
        
        raise LoxRuntimeError(
            operator, "OPERAND MUST BE A NUMBER"
        )
    def check_number_operands(self, operator, left, right):
        if isinstance(left, float) and isinstance(right, float):
            return

        raise LoxRuntimeError(operator, "OPERANDS MUST BE NUMBERS")

    def is_equal(self, left, right):
        if left is None and right is None:
            return True

        if left is None:
            return False

        return left == right
    def is_truthy(self, value):
        if value is None:
            return False

        if isinstance(value, bool):
            return value

        if isinstance(value, float):
            return value != 0.0

        return True



class ParseError(Exception):
    pass


def RunScanner(parameter):
    # Main scanner entry. Called by Repl() and RunFile()
    evaluator = Evaluator()
    scanner = Scanner(parameter)
    tokens = scanner.scan_tokens()

    if scanner.had_error:
        return


    parser = Parser(tokens)
    statements = parser.parse()

    if parser.had_error:
        return

    evaluator.interpret(statements)
    
def MainRunTree(inputline):
    #first function call of main, passes to RunFile or REPL mode
    if len(inputline) == 1:
        print()
        print("WELCOME")
        Repl()
    elif len(inputline) == 2:
        filename = inputline[1]
        RunFile(filename)
    elif len(inputline) >= 3:
        print()
        print("MULTIPLE INPUT HANDLING NOT DEFINED")
        print()

def Repl():
    #try and except professor provided
    try:
        print()
        print("REPL MODE INITIATED")
        print()
        while True:
            print("SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT")
            print()
            parameter = input("> ")
            RunScanner(parameter)
    except KeyboardInterrupt:
        print()
        print()
        print("REPL MODE DEACTIVATED")
        print()

def RunFile(name):
    # Called by MainRunTree
    with open(name, "r") as file:
        inputfilecontents = file.read()
    RunScanner(inputfilecontents)

def main():
    printer = ASTPrinter()

    # --- start AI code ---print
    #Existence of sys.argv learned from ChatGPT
    MainRunTree(sys.argv)
    #--- end AI code ---
    print("PROGRAM ENDED")
    print()
    print()

if __name__ == "__main__":
    main()
