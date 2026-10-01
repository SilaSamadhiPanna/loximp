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
        print("[LINE", self.line, "] SCANNER ERROR:", message)




def RunScanner(parameter):
    # Main scanner entry. Called by Repl() and RunFile()
    scanner = Scanner(parameter)
    tokens = scanner.scan_tokens()

#token checker - eventually to be removed
    for token in tokens:
        print(
            token.token_type,
            token.lexeme,
            token.literal,
            token.line
        )

    
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
    MainRunTree(sys.argv)
    print("PROGRAM ENDED")
    print()
    print()

if __name__ == "__main__":
    main()
