import os
import getopt

# Created modules
import auxiliary as aux

def parseArguments(argv):
    options, remaining = getopt.gnu_getopt(argv[1:], "t:hec", ["target=", "help", "emptylines", "comments"])

    if len(remaining) > 0:
        aux.error("Unknown arguments " + str(remaining))

    target = None
    for opt, arg in options:
        if opt == "-t" or opt == "--target":
            if not os.path.exists(arg):
                aux.error("Given path doesn't exist")
            target = arg

        elif opt == "-e" or opt == "--emptylines":
            aux.noEmptyLinesOption = True
        
        elif opt == "-c" or opt == "--comments":
            aux.noCommentsOption = True
        
        elif opt == "-h" or opt == "--help":
            help()

    if target is None:
        target = os.getcwd()

    return target

def help():
    pass
    # TODO: usage