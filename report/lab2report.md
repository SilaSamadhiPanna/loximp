Jacob Elliott
10/08/2026
CIS 343 01 Structure of Programming Languages

Dependency/Setup:

Loximp requires Python 3 and has no external dependencies. From the root /loximp directory, run "python3 src/loximp.py" to start REPL mode. To scan a source file, run "python3 src/loximp.py <source-file>". To run ASTPrinter output tests, run "PYTHONPATH=. python3 test/lab2/test_ast.py"

Report 2:

loximp continues to grow, now with a syntactic grammar design, AST implementation, and a functional AST printer. Lab2 includes all of the great design features we've come to appreciate from loximp, including an emphasis on ALL CAPS text, and simple, easy to follow python code. 

The AST classes and AST printer are heavily inspired by the inclass breakfast printer examples, as well as the inclass slides and Crafting Interpreters chapter 5. However, the loximp ASTPrinter uses a single printer class, and recursively calls the same print function repeatedly when given hardcoded expressions. isinstance() is used to check the type of object - the existence of this function was previously unknown to me, and it's use was suggested by ChatGPT. The syntactical grammar uses the structure introduced in class. Each grammar category is represented by a class. Literal, Grouping, Unary, and Binary all inherit from the shared Expression base class. 

Syntactical Grammar:

expression > literal
            | unary
            | binary
            |grouping ;

literal    > NUMBER | STRING | "true" | "false" | "nil" ;
grouping   > "(" expression ")" ;
unary      > ( "-" | "!" ) expression ;
binary     > expression operator expression ;
operator   > "==" | "!=" | "<" | "<=" | ">" | ">=" | "+" | "-" | "*" | "/" ;

Four hardcoded test statements have been prepared to cover every expression class, every supported literal type and operator, and nested expressions. 

Test 1: Passed 
This is the default test given in the lab2 instructions. 

    test1 = Binary(
        Unary(Token(MINUS, "-", None, 1), Literal(123)),
        Token(STAR, "*", None, 1),
        Grouping(Literal(45.67))
    )

    Expected Output:
    (* (- 123) (GROUP 45.67))

    Actual Output:
    (* (- 123) (GROUP 45.67))

    Original Expression:
    -123 * (45.67)

Test 2: Passed
Tests for string, boolean, NIL, equality and inequality, unary negation

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
    Expected Output:
    (!= (== hello TRUE) (== (! FALSE) NIL))

    Actual Output:
    (!= (== hello TRUE) (== (! FALSE) NIL))

    Original Expression:
    ("hello" == true) != ((!false) == nil)

Test 3: Passed
tests for many different operators, as well as a different way to build objects. 

    test3 = Binary(Literal(8), Token(SLASH, "/", None, 1), Literal(2))
    test3 = Binary(test3, Token(PLUS, "+", None, 1), Literal(3))
    test3 = Binary(test3, Token(MINUS, "-", None, 1), Literal(1))
    test3 = Binary(test3, Token(LESS, "<", None, 1), Literal(20))
    test3 = Binary(test3, Token(LESS_EQUAL, "<=", None, 1), Literal(25))
    test3 = Binary(test3, Token(GREATER, ">", None, 1), Literal(5))
    test3 = Binary(test3, Token(GREATER_EQUAL, ">=", None, 1), Literal(10))

    Expected Output:
    (>= (> (<= (< (- (+ (/ 8 2) 3) 1) 20) 25) 5) 10)

    Actual Output:
    (>= (> (<= (< (- (+ (/ 8 2) 3) 1) 20) 25) 5) 10)

    Original Expression:
    (((((((8 / 2) + 3) - 1) < 20) <= 25) > 5) >= 10)

Test 4: Passed
tests for grouping on complex objects.

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

    Expected Output:
    (! (GROUP (== (+ 2 (* 3 4)) 14)))

    Actual Output:
    (! (GROUP (== (+ 2 (* 3 4)) 14)))

    Original Expression:
    !(2 + 3 * 4 == 14)

Known Limitations or failing tests:

No test failures were observed.