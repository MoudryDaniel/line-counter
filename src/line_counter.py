import sys

# Created modules
import argument_parser as argpars
import counter

def main():
    target = argpars.parseArguments(sys.argv)
    counter.count(target)

def error(msg):
    print("ERROR: " + msg, file = sys.stderr)

if __name__ == "__main__":
    main()