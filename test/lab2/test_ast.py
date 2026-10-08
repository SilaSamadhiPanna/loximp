from src.loximp import (
    ASTPrinter, Binary, Grouping, Literal, Token, Unary,
    BANG, BANG_EQUAL, EQUAL_EQUAL, GREATER, GREATER_EQUAL,
    LESS, LESS_EQUAL, MINUS, PLUS, SLASH, STAR
)

printer = ASTPrinter()

#Lab 2 example
test1 = Binary(
    Unary(Token(MINUS, "-", None, 1), Literal(123)),
    Token(STAR, "*", None, 1),
    Grouping(Literal(45.67))
)

print(printer.print_expression(test1))

test2 = Binary(
    Binary(
        Literal("hello"),
        Token(EQUAL_EQUAL, "==", None, 1),
        Literal(True)
    ),
    Token(BANG_EQUAL, "!=", None, 1),
    Binary(
        Unary(Token(BANG, "!", None, 1), Literal(False)),
        Token(EQUAL_EQUAL, "==", None, 1),
        Literal(None)
    )
)

print(printer.print_expression(test2))

test3 = Binary(Literal(8), Token(SLASH, "/", None, 1), Literal(2))
test3 = Binary(test3, Token(PLUS, "+", None, 1), Literal(3))
test3 = Binary(test3, Token(MINUS, "-", None, 1), Literal(1))
test3 = Binary(test3, Token(LESS, "<", None, 1), Literal(20))
test3 = Binary(test3, Token(LESS_EQUAL, "<=", None, 1), Literal(25))
test3 = Binary(test3, Token(GREATER, ">", None, 1), Literal(5))
test3 = Binary(test3, Token(GREATER_EQUAL, ">=", None, 1), Literal(10))

print(printer.print_expression(test3))

test4 = Unary(
    Token(BANG, "!", None, 1),
    Grouping(
        Binary(
            Binary(
                Literal(2),
                Token(PLUS, "+", None, 1),
                Binary(
                    Literal(3),
                    Token(STAR, "*", None, 1),
                    Literal(4)
                )
            ),
            Token(EQUAL_EQUAL, "==", None, 1),
            Literal(14)
        )
    )
)

print(printer.print_expression(test4))

