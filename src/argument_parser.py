import os
import getopt
import re

# Created modules
import auxiliary as aux

def parseArguments(argv):
    try:
        options, remaining = getopt.gnu_getopt(argv[1:], "t:bce:i:d:h", ["target=", "help", "blanklines", "comments", "extensions=", "ignore=", "depth="])
    except getopt.error as e:
        aux.error(str(e))

    if len(remaining) > 0:
        aux.error("Unknown arguments " + str(remaining))

    target = None
    for opt, arg in options:
        if opt == "-t" or opt == "--target":
            if not os.path.exists(arg):
                aux.error("Given path doesn't exist")
            target = arg
            print(arg)

        elif opt == "-b" or opt == "--blanklines":
            aux.noBlankLinesOption = True
        
        elif opt == "-c" or opt == "--comments":
            aux.noCommentsOption = True
        
        elif opt == "-e" or opt == "--extensions":
            parseExtensions(arg, aux.extensions)

        elif opt == "-i" or opt == "--ignore":
            parseExtensions(arg, aux.ignore)

        elif opt == "-d" or opt == "--depth":
            if not re.search(r"^[0-9]+$", arg):
                aux.error("Value of " + opt + " has to be a number (Integer)")
            aux.depth = int(arg) + 2

        elif opt == "-h" or opt == "--help":
            help()

    if aux.extensions and aux.ignore:
        aux.error("Not possible to specify wanted extensions and ignore extensions at the same time")

    if target is None:
        target = os.getcwd()

    return target

def parseExtensions(extensions, list):
    extensions = extensions.split(",")
    for ext in extensions:
        ext = ext.strip()
        if re.search("^\.([a-z]|[0-9])+$", ext):
            list.append(ext)
        else:
            aux.error(ext + "extension doesn't match regular expression")

def help():
    print("""
    Usage:
    python3 ./line_counter.py

    Options:
        -h, --help <-- show usage
        -t, --target PATH <-- specify path of file or directory (default is CWD)
        -b, --blanklines <-- exlude blank lines from the calculation
        -c, --comments <-- exclude comments from the calculation
        -e, --extensions COMMA-SEPARATED EXTENSION e.g. .py, .java <-- specify files to be included in the calculation
        -i, --ignore COMMA-SEPARATED EXTENSION e.g. .py, .java <-- specify file to be ignored from the calculation
        -d, --depth NUMBER (Integer) <-- specify depth of recursion (default is maximal depth) e.g. 0 is no recursion (only target directory)

    """)