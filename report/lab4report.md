Jacob Elliott
11/5/2026
CIS 343 01 Structure of Programming Languages

Dependency/Setup:

Loximp requires Python 3 and has no external dependencies. From the root /loximp directory, run "python3 src/loximp.py" to start REPL mode. To execute a source file, run "python3 src/loximp.py <source-file>". 

Report 4:

Loximp v4 adds expression statements and print statements, synchronization, and panic error mode recovery. 

Two tests were run per the Lab 4 assignment. 

Terminal command: python3 src/loximp.py test/lab4/lab4test1.lox

Input:

"one"
true;
print 2 +

Output:

[LINE 2 at 'true': EXPECT ';' AFTER EXPRESSION.
[LINE 3 at end of input: EXPECTED EXPRESSION
PROGRAM ENDED

Terminal command: python3 src/loximp.py test/lab4/lab4test2.lox

Input:

4 + 2;
print "one";
print true;
print 1 + 2;
print nil;

Output:

one
TRUE
3
NIL
PROGRAM ENDED
