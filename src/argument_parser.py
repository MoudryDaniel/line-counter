import os
import getopt
import re

# Created modules
import auxiliary as aux

def parseArguments(argv):
    try:
        options, remaining = getopt.gnu_getopt(argv[1:], "t:hbce:i:", ["target=", "help", "blanklines", "comments", "extensions=", "ignore="])
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
    pass
    # TODO: usage