import sys

# Created modules
import argument_parser as argpars
import counter
from show import showResult

def main():
    target = argpars.parseArguments(sys.argv)
    res = counter.count(target)
    showResult(res)

def error(msg):
    print("ERROR: " + msg, file = sys.stderr)

if __name__ == "__main__":
    main()