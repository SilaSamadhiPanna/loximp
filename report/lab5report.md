Jacob Elliott
11/24/2026
CIS 343 01 Structure of Programming Languages

Dependency/Setup:

Loximp requires Python 3 and has no external dependencies. From the root /loximp directory, run "python3 src/loximp.py" to start REPL mode. To execute a source file, run "python3 src/loximp.py <source-file>". 

Report 5:

Loximp continues to expand, now with the inclusion of variable declaration, access, and assignment. The code is a translation of java into python, following crafting interpreters. Loximp handles variable access before declaration by raising a runtime error. Variables can be created without an explicit initializer and are assigned a NIL value. Variables can be redeclared, redeclaration in the same environment replaces that variable's value, and variable values follow nested environments. 

Successful variable declaration, access, and assignment output:

1
2
NIL
0
PROGRAM ENDED

Test Program:

var total = 1;
print total;

total = total + 1;
print total;

var pending;
print pending;

var total = 0;
print total;


Block Scope Code Output:

inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c
PROGRAM ENDED

This code contains three environments within which the variables a, b, and c are assigned and called. First, variables a, b, and c are created and assigned with values. As we move past the first left brace, we enter a new block, so that when the values of a and b are updated, new local variables are created in a new sub environment. As the second left brace is passed we enter into the third environment, where another local variable of a is created and assigned its value. Then a, b, and c are printed. a returns the value found immediately within the local environment. The value of b is not found locally, so the next environment in the chain is checked, where it is found in the outer environment. The value of c is neither found locally or in the outer environment, so the check moves to the global environment. As the first right brace is passed we leave behind the inner environment, and with it, the value of a that was assigned there, resulting in the outer value of a being the closest in the chain, and the same checks for b and c. Finally, with the passing of the second right brace, the outer environment is left behind, and printing a, b, and c return the values that are found within the global environment. 

REPL mode error demonstrations:
WELCOME

REPL MODE INITIATED

SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> print missing;
UNDEFINED VARIABLE 'missing'.
[LINE 1]
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> print later; var later = 1;
UNDEFINED VARIABLE 'later'.
[LINE 1]
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> missing = 1;
UNDEFINED VARIABLE 'missing'.
[LINE 1]
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> { var secret = 1; } print secret;
UNDEFINED VARIABLE 'secret'.
[LINE 1]
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> 5 = 10;
[LINE 1] at '=': INVALID ASSIGNMENT TARGET.
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> var a = 1; a + 1 = 10;
[LINE 1] at '=': INVALID ASSIGNMENT TARGET.
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> var a = 1; (a) = 10;
[LINE 1] at '=': INVALID ASSIGNMENT TARGET.
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> var = 1;
[LINE 1] at '=': EXPECT VARIABLE NAME.
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> var value = ;
[LINE 1] at ';': EXPECTED EXPRESSION
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> var value = 1
[LINE 1] at end of input: EXPECT ';' AFTER VARIABLE DECLARATION.
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> { print 1;
[LINE 1] at end of input: EXPECT '}' AFTER BLOCK.
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT

> }
[LINE 1] at '}': UNMATCHED '}'.
SYSTEM PREPARED FOR INPUT. CTRL + C TO EXIT
