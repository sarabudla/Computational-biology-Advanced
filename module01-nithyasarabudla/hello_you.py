# hello_you.py 
import sys


def hello_name(name="you"):
    """1: hello_name which should be identical to hello_name from Problem 1.
Then, create a if __name__ == "__main__" block that takes in a name as a command line argument. and then prints "Hello, [Name]!". For example, running ./hello_you.py Chesley should print "Hello, Chesley!" to the terminal.
Running just ./hello_you.py without any arguments should print "Hello, you!"."""

    return "Hello, " + name + "!"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "you"
    print(hello_name(name))
