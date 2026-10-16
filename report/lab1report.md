Jacob Elliott
10/01/2026
CIS 343 01 Structure of Programming Languages

The name of my programming language is loximp. 

So far, Loximp has come from two sources - the main program run structure is my own. Almost all of the scanner logic is taken from chapter 4 of Crafting Interpreters, but translated into Python rather than Java. As intentional design decisions, an emphasis has been placed on ALL CAPS TEXT, as well as detailed system information. Loximp uses a slightly smaller set of reserved keywords than the complete Lox implementation found in Crafting Interpreters. 

Regular Expressions:

Number literals:
[0-9]+(\.[0-9]+)?

String literals:
"[^"]*"

Identifiers:
[A-Za-z_][A-Za-z0-9_]*

Dependency/setup Instructions:

Loximp requires Python 3 and has no external dependencies. From the root /loximp directory, run python3 src/loximp.py to start REPL mode. To scan a source file, run python3 src/loximp.py <source-file>.

Tests:
Multiple tests are included in loximp/test/lab1, which can be run with the following commands when in /loximp:

python3 src/loximp.py test/lab1/all_tokens.lox
python3 src/loximp.py test/lab1/emptyfile.lox
python3 src/loximp.py test/lab1/identifiers_keywords.lox
python3 src/loximp.py test/lab1/intentional_errors.lox
python3 src/loximp.py test/lab1/numbers.lox

all_tokens:
    Tests all defined tokens in loximp. Each lexeme should match its expected token type. Multiline strings should be identified. Identifiers should not be strings. 

    Input:
    (){}.,;

    + - * /

    !
    !=
    =
    ==
    <
    <=
    >
    >=

    0
    123
    123.456

    "hello"
    "hello world!"
    "hello
    world"
    ""

    identifier
    identifier123
    _private
    snake_case_123

    and
    else
    false
    for
    if
    or
    print
    return
    true
    var
    while
    nil

    // This entire line should be ignored by the scanner.

    Actual Output:
    LEFT_PARENTHESES ( None 1
    RIGHT_PARENTHESES ) None 1
    LEFT_BRACE { None 1
    RIGHT_BRACE } None 1
    DOT . None 1
    COMMA , None 1
    SEMICOLON ; None 1
    PLUS + None 3
    MINUS - None 3
    STAR * None 3
    SLASH / None 3
    BANG ! None 5
    BANG_EQUAL != None 6
    EQUAL = None 7
    EQUAL_EQUAL == None 8
    LESS < None 9
    LESS_EQUAL <= None 10
    GREATER > None 11
    GREATER_EQUAL >= None 12
    NUMBER 0 0.0 14
    NUMBER 123 123.0 15
    NUMBER 123.456 123.456 16
    STRING "hello" hello 18
    STRING "hello world!" hello world! 19
    STRING "hello
    world" hello
    world 21
    STRING ""  22
    IDENTIFIER identifier None 24
    IDENTIFIER identifier123 None 25
    IDENTIFIER _private None 26
    IDENTIFIER snake_case_123 None 27
    AND and None 29
    ELSE else None 30
    FALSE false None 31
    FOR for None 32
    IF if None 33
    OR or None 34
    PRINT print None 35
    RETURN return None 36
    TRUE true None 37
    VAR var None 38
    WHILE while None 39
    NIL nil None 40
    EOF  None 42
    PROGRAM ENDED

Result:
PASS - Actual output matched expected output.


emptyfile.lox:
    Simply an empty file. Will only return an EOF token. 

    Input:

    Actual Output:

    EOF  None 1
    PROGRAM ENDED

Result:
PASS - Actual output matched expected output.

identifiers_keywords:
    Tests identifiers and keywords. Tests for case sensitivity, underscores, mixed up digits, and identifiers that begin with keyword text. 

    Input:

    and
    else
    false
    for
    if
    or
    print
    return
    true
    var
    while
    nil

    anderson
    elsewhere
    falsehood
    format
    iffy
    orange
    printer
    returnValue
    trueValue
    variable
    whileLoop
    nilValue

    and2
    if2
    var2
    while123

    _if
    _var
    _private
    _
    snake_case
    snake_case_123

    AND
    ELSE
    FALSE
    FOR
    IF
    OR
    PRINT
    RETURN
    TRUE
    VAR
    WHILE
    NIL

    True
    False
    Var
    While

    Actual Output:
    
    AND and None 1
    ELSE else None 2
    FALSE false None 3
    FOR for None 4
    IF if None 5
    OR or None 6
    PRINT print None 7
    RETURN return None 8
    TRUE true None 9
    VAR var None 10
    WHILE while None 11
    NIL nil None 12
    IDENTIFIER anderson None 14
    IDENTIFIER elsewhere None 15
    IDENTIFIER falsehood None 16
    IDENTIFIER format None 17
    IDENTIFIER iffy None 18
    IDENTIFIER orange None 19
    IDENTIFIER printer None 20
    IDENTIFIER returnValue None 21
    IDENTIFIER trueValue None 22
    IDENTIFIER variable None 23
    IDENTIFIER whileLoop None 24
    IDENTIFIER nilValue None 25
    IDENTIFIER and2 None 27
    IDENTIFIER if2 None 28
    IDENTIFIER var2 None 29
    IDENTIFIER while123 None 30
    IDENTIFIER _if None 32
    IDENTIFIER _var None 33
    IDENTIFIER _private None 34
    IDENTIFIER _ None 35
    IDENTIFIER snake_case None 36
    IDENTIFIER snake_case_123 None 37
    IDENTIFIER AND None 39
    IDENTIFIER ELSE None 40
    IDENTIFIER FALSE None 41
    IDENTIFIER FOR None 42
    IDENTIFIER IF None 43
    IDENTIFIER OR None 44
    IDENTIFIER PRINT None 45
    IDENTIFIER RETURN None 46
    IDENTIFIER TRUE None 47
    IDENTIFIER VAR None 48
    IDENTIFIER WHILE None 49
    IDENTIFIER NIL None 50
    IDENTIFIER True None 52
    IDENTIFIER False None 53
    IDENTIFIER Var None 54
    IDENTIFIER While None 55
    EOF  None 55
    PROGRAM ENDED

Result:
PASS - Actual output matched expected output.

intentional_errors:
    Tests unrecognized characters. Confirms that scanner continues after errors, comment contents are ignored, special characters are allowed inside strings, and unterminated strings are correctly idenfied. 

    Input:

    @
    #
    $
    %
    ^
    &
    [
    ]
    :
    ?
    '

    good@bad
    123#456
    hello$world

    // @ # $ % ^ & [ ] : ? '
    // The symbols above should cause NO errors because they are inside comments.

    "@ # $ % ^ & [ ] : ? '"
    "These symbols are also valid inside a string: @#$%^&[]"

    123 + 456
    if true
    var employee123

    "unterminated string

    Actual Output:
    [line 1 ] Scanner Error: Unexpected character: @
    [line 2 ] Scanner Error: Unexpected character: #
    [line 3 ] Scanner Error: Unexpected character: $
    [line 4 ] Scanner Error: Unexpected character: %
    [line 5 ] Scanner Error: Unexpected character: ^
    [line 6 ] Scanner Error: Unexpected character: &
    [line 7 ] Scanner Error: Unexpected character: [
    [line 8 ] Scanner Error: Unexpected character: ]
    [line 9 ] Scanner Error: Unexpected character: :
    [line 10 ] Scanner Error: Unexpected character: ?
    [line 11 ] Scanner Error: Unexpected character: '
    [line 13 ] Scanner Error: Unexpected character: @
    [line 14 ] Scanner Error: Unexpected character: #
    [line 15 ] Scanner Error: Unexpected character: $
    [line 27 ] Scanner Error: Unterminated string.
    IDENTIFIER good None 13
    IDENTIFIER bad None 13
    NUMBER 123 123.0 14
    NUMBER 456 456.0 14
    IDENTIFIER hello None 15
    IDENTIFIER world None 15
    STRING "@ # $ % ^ & [ ] : ? '" @ # $ % ^ & [ ] : ? ' 20
    STRING "These symbols are also valid inside a string: @#$%^&[]" These symbols are also valid inside a string: @#$%^&[] 21
    NUMBER 123 123.0 23
    PLUS + None 23
    NUMBER 456 456.0 23
    IF if None 24
    TRUE true None 24
    VAR var None 25
    IDENTIFIER employee123 None 25
    EOF  None 27
    PROGRAM ENDED

Result:
PASS - Actual output matched expected output.

numbers:
    Verifies that integer and decimal literals work correctly. 

    Input:

    0
    1
    7
    42
    123
    000123

    0.0
    0.5
    1.5
    12.34
    123.456
    999.001

    -123
    -12.34
    +123
    +12.34

    123.
    .123

    1.2.3
    12..34

    123abc
    123_abc
    1a

    Actual Output:

    NUMBER 0 0.0 1
    NUMBER 1 1.0 2
    NUMBER 7 7.0 3
    NUMBER 42 42.0 4
    NUMBER 123 123.0 5
    NUMBER 000123 123.0 6
    NUMBER 0.0 0.0 8
    NUMBER 0.5 0.5 9
    NUMBER 1.5 1.5 10
    NUMBER 12.34 12.34 11
    NUMBER 123.456 123.456 12
    NUMBER 999.001 999.001 13
    MINUS - None 15
    NUMBER 123 123.0 15
    MINUS - None 16
    NUMBER 12.34 12.34 16
    PLUS + None 17
    NUMBER 123 123.0 17
    PLUS + None 18
    NUMBER 12.34 12.34 18
    NUMBER 123 123.0 20
    DOT . None 20
    DOT . None 21
    NUMBER 123 123.0 21
    NUMBER 1.2 1.2 23
    DOT . None 23
    NUMBER 3 3.0 23
    NUMBER 12 12.0 24
    DOT . None 24
    DOT . None 24
    NUMBER 34 34.0 24
    NUMBER 123 123.0 26
    IDENTIFIER abc None 26
    NUMBER 123 123.0 27
    IDENTIFIER _abc None 27
    NUMBER 1 1.0 28
    IDENTIFIER a None 28
    EOF  None 28
    PROGRAM ENDED

Result:
PASS - Actual output matched expected output.

REPL Mode Error Test:

REPL Mode Input:

WELCOME

REPL MODE INITIATED

SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> @
[LINE 1 ] SCANNER ERROR: UNEXPECTED CHARACTER: @
EOF  None 1
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

Result:
PASS - REPL mode continued after error report

Known Limitations:

1) Pasting multiple lines of code into REPL mode will result in disordered returned content
2) Block comments are not supported
3) String escape sequences are not supported