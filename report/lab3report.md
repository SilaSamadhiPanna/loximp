Jacob Elliott
10/15/2026
CIS 343 01 Structure of Programming Languages

Dependency/Setup:

Loximp requires Python 3 and has no external dependencies. From the root /loximp directory, run "python3 src/loximp.py" to start REPL mode. To scan a source file, run "python3 src/loximp.py <source-file>". 

Report 3:

loximp v3 is here! In addition to the great feature's we've seen in previous releases, loximp now includes a parser that connects the scanner and AST printer. This parser design is taken directly from crafting interpreters and is translated into python. The only changes that I have been made is to keep error reporting in line with the eshtablished loximp style, as adding the necessary error reporting flags mentioned in class. The lab 1 and lab 2 sections of this project remain unchanged, and information about those specific sections can be found in the previous reports. 

The parser uses the following expression grammar:

expression > equality

equality > comparison (( "!=" | "==" ) comparison)*

comparison > term (( ">" | ">=" | "<" | "<=") term )*

term > factor (( "-" | "+" ) factor )*

factor > unary (( "/" | "*" ) unary )*

unary > ( "!" | "-" ) unary
    | primary

primary > NUMBER | STRING | "true" | "false" | "nil"
    | "(" expression ")"

The precedence order is eshtablished based on the heirarchy of function calls in the parser. The specific order is expression, equality, comparison, term, factor, unary, and primary, with each function calling the next in the sequence until a literal is reached. This structured, heirarchical function approach ensures that expressions are parsed in the accepted conventional order. Binary operators are left associative, and unary operators are right associative. For example, 1 + 2 + 3 is parsed as (1 + 2) + 3, and 1 + 2 * 3 is evaluated as 1 + (2 * 3).

Lab3 Tests:

A total of 20 seperate test files have been prepared to put loximp through the gauntlet. They can be found in /test/lab3. To run the tests, navigate to the loximp directory and input "python3 src/loximp.py test/lab3/filename.lox"

As an additional convience, all tests can be run at once using this command:

for file in test/lab3/*.lox; do
    echo "$file"
    python3 src/loximp.py "$file"
done 2>&1 | tee test/lab3/results.txt

The results of the tests are as follows:

Test 1:
    test/lab3/arithmetic.lox

    SOURCE INPUT:
    10 - 3 + 2

    ACTUAL OUTPUT:
    (+ (- 10.0 3.0) 2.0)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (+ (- 10.0 3.0) 2.0)
    PROGRAM ENDED

    TEST PASSED
    This test checks a standard expression and shows correct left associativity


Test 2:
    test/lab3/associativity.lox

    SOURCE INPUT:
    16 / 4 / 2

    ACTUAL OUTPUT:
    (/ (/ 16.0 4.0) 2.0)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (/ (/ 16.0 4.0) 2.0)
    PROGRAM ENDED

    TEST PASSED
    This test checks repeated uses of the same operator

Test 3:
    test/lab3/boolean.lox

    SOURCE INPUT:
    true == false

    ACTUAL OUTPUT:
    (== TRUE FALSE)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (== TRUE FALSE)
    PROGRAM ENDED

    TEST PASSED
    This is a simple equality operator check


Test 4:
    test/lab3/comparison.lox

    SOURCE INPUT:
    1 < 2 <= 3

    ACTUAL OUTPUT:
    (<= (< 1.0 2.0) 3.0)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (<= (< 1.0 2.0) 3.0)
    PROGRAM ENDED

    TEST PASSED
    This test checks the less than operators

Test 5:
    test/lab3/comparison2.lox

    SOURCE INPUT:
    4 > 3 >= 2

    ACTUAL OUTPUT:
    (>= (> 4.0 3.0) 2.0)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (>= (> 4.0 3.0) 2.0)
    PROGRAM ENDED

    TEST PASSED
    This test checks the greater than operators

Test 6:
    test/lab3/equality.lox

    SOURCE INPUT:
    1 == 1 != 2

    ACTUAL OUTPUT:
    (!= (== 1.0 1.0) 2.0)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (!= (== 1.0 1.0) 2.0)
    PROGRAM ENDED

    TEST PASSED
    This test checks the equality operators

Test 7:
    test/lab3/grouping.lox

    SOURCE INPUT:
    ((1 + 2) * (3 - 4))

    ACTUAL OUTPUT:
    (GROUP (* (GROUP (+ 1.0 2.0)) (GROUP (- 3.0 4.0))))
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (GROUP (* (GROUP (+ 1.0 2.0)) (GROUP (- 3.0 4.0))))
    PROGRAM ENDED

    TEST PASSED
    This test checks for correct grouping


Test 8:
    test/lab3/invalid_character.lox

    SOURCE INPUT:
    1 + @ 2

    ACTUAL OUTPUT:
    [LINE 1 ] SCANNER ERROR: UNEXPECTED CHARACTER: @
    PROGRAM ENDED

    EXPECTED OUTPUT:
    [LINE 1 ] SCANNER ERROR: UNEXPECTED CHARACTER: @
    PROGRAM ENDED

    TEST PASSED / ERROR REPORTED
    This error demonstrates unexpected character handling


Test 9:
    test/lab3/missing_left_operand.lox

    SOURCE INPUT:
    * 2

    ACTUAL OUTPUT:
    [LINE 1 at '*': EXPECTED EXPRESSION
    PROGRAM ENDED

    EXPECTED OUTPUT:
    [LINE 1 at '*': EXPECTED EXPRESSION
    PROGRAM ENDED

    TEST PASSED / ERROR REPORTED
    This errors shows what happens when a statement starts with an operator rather than a number


Test 10:
    test/lab3/missing_operand_end.lox

    SOURCE INPUT:
    1 +

    ACTUAL OUTPUT:
    [LINE 2 at end of input: EXPECTED EXPRESSION
    PROGRAM ENDED

    EXPECTED OUTPUT:
    [LINE 2 at end of input: EXPECTED EXPRESSION
    PROGRAM ENDED

    TEST PASSED / ERROR REPORTED
    This error shows what happens when there is a missing operand


Test 11:
    test/lab3/missing_operand.lox

    SOURCE INPUT:
    1 + * 2

    ACTUAL OUTPUT:
    [LINE 1 at '*': EXPECTED EXPRESSION
    PROGRAM ENDED

    EXPECTED OUTPUT:
    [LINE 1 at '*': EXPECTED EXPRESSION
    PROGRAM ENDED

    TEST PASSED / ERROR REPORTED
    The purpose of this error is catch improper use of operators and grammatically incorrect expressions


Test 12:
    test/lab3/missing_parenthesis.lox

    SOURCE INPUT:
    (1 + 2

    ACTUAL OUTPUT:
    [LINE 2 at end of input: EXPECTED ')' AFTER EXPRESSION
    PROGRAM ENDED

    EXPECTED OUTPUT:
    [LINE 2 at end of input: EXPECTED ')' AFTER EXPRESSION
    PROGRAM ENDED

    TEST PASSED / ERROR REPORTED
    The purpose of this error is to show that loximp can display missing parenthases errors. 


Test 13:
    test/lab3/multiplication.lox

    SOURCE INPUT:
    8 / 2 * 3

    ACTUAL OUTPUT:
    (* (/ 8.0 2.0) 3.0)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (* (/ 8.0 2.0) 3.0)
    PROGRAM ENDED

    TEST PASSED
    This test checks left associativity for factor operators


Test 14:
    test/lab3/nil.lox

    SOURCE INPUT:
    nil

    ACTUAL OUTPUT:
    NIL
    PROGRAM ENDED

    EXPECTED OUTPUT:
    NIL
    PROGRAM ENDED

    TEST PASSED
    This test checks the nil token type

Test 15:
    test/lab3/number.lox

    SOURCE INPUT:
    42

    ACTUAL OUTPUT:
    42.0
    PROGRAM ENDED

    EXPECTED OUTPUT:
    42.0
    PROGRAM ENDED

    TEST PASSED
    This test checks for a single number literal


Test 16:
    test/lab3/precedence.lox

    SOURCE INPUT:
    1 + 2 * 3 == 7

    ACTUAL OUTPUT:
    (== (+ 1.0 (* 2.0 3.0)) 7.0)
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (== (+ 1.0 (* 2.0 3.0)) 7.0)
    PROGRAM ENDED

    TEST PASSED
    This test checks for correct precedence with terms and factors


Test 17:
    test/lab3/string.lox

    SOURCE INPUT:
    "hello"

    ACTUAL OUTPUT:
    hello
    PROGRAM ENDED

    EXPECTED OUTPUT:
    hello
    PROGRAM ENDED

    TEST PASSED
    This test checks for a simple string


Test 18:
    test/lab3/trailing_tokens.lox

    SOURCE INPUT:
    1 + 2 3

    ACTUAL OUTPUT:
    [LINE 1 at '3': UNEXEPECTED TOKEN
    PROGRAM ENDED

    EXPECTED OUTPUT:
    [LINE 1 at '3': UNEXEPECTED TOKEN
    PROGRAM ENDED

    TEST PASSED / ERROR REPORTED
    This error shows an unexpected token at the end of a file, which in this case happens to be a three without an associated operator. 


Test 19:
    test/lab3/unary.lox

    SOURCE INPUT:
    !-3

    ACTUAL OUTPUT:
    (! (- 3.0))
    PROGRAM ENDED

    EXPECTED OUTPUT:
    (! (- 3.0))
    PROGRAM ENDED

    TEST PASSED
    This test checks for unary negation


Test 20:
    test/lab3/unexpected_parenthesis.lox

    SOURCE INPUT:
    1 + 2)

    ACTUAL OUTPUT:
    [LINE 1 at ')': UNEXEPECTED TOKEN
    PROGRAM ENDED

    EXPECTED OUTPUT:
    [LINE 1 at ')': UNEXEPECTED TOKEN
    PROGRAM ENDED

    TEST PASSED / ERROR REPORTED
    This error reports an unexpected token at the end of a file, which happens to be a right parenthases in this case. 

A handdrawn syntax tree for the expression 1 + 2 * 3 = 4 - 5 can be found in report/images/

Known Limitations or failing tests:

Test 10: Reports that the error occured on line two, probably because of the missing operand and the way the scanner consumes newline tokens. 