import sys

def RunScanner(parameter):
    # Main scanner entry. Called by Repl() and RunFile()
    print()
    print("INPUT PARAMETER: ", parameter)
    print()
    print("INPUT DISCARDED, NO SCANNER AVAILABLE")
    print()
    
def MainRunTree(inputline):
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
