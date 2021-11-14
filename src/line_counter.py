import sys

# Created modules
import argument_parser as argpars

def main():
    argpars.parseArguments(sys.argv)

def error(msg):
    print("ERROR: " + msg, file = sys.stderr)

if __name__ == "__main__":
    main()