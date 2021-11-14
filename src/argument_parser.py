import os
import getopt
from pathlib import Path

# Created modules
from line_counter import error

def parseArguments(argv):
    options, remaining = getopt.gnu_getopt(argv[1:], "t:h", ["target=", "help"])

    if len(remaining) > 0:
        error("Unknown arguments " + str(remaining))
        pass

    target = None
    for opt, arg in options:
        if opt == "-t" or opt == "--target":
            if not os.path.exists(arg):
                error("Given path doesn't exist")
            target = arg
        elif opt == "-h" or opt == "--help":
            help()
            
    if target is None:
        target = os.getcwd()

    return target

def help():
    pass