import os
import getopt

# Created modules
from line_counter import error
import global_vars as globalv

def parseArguments(argv):
    options, remaining = getopt.gnu_getopt(argv[1:], "t:hec", ["target=", "help", "emptylines", "comments"])

    if len(remaining) > 0:
        error("Unknown arguments " + str(remaining))
        pass

    target = None
    for opt, arg in options:
        if opt == "-t" or opt == "--target":
            if not os.path.exists(arg):
                error("Given path doesn't exist")
            target = arg
        elif opt == "-e" or opt == "--emptylines":
            globalv.noEmptyLinesOption = True
        elif opt == "-c" or opt == "--comments":
            globalv.noCommentsOption = True
        elif opt == "-h" or opt == "--help":
            help()

    if target is None:
        target = os.getcwd()

    return target

def help():
    pass