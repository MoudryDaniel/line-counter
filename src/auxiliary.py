import sys

def error(msg):
    print("ERROR: " + msg, file = sys.stderr)
    sys.exit(1)

global commentRegexes    
commentRegexes = {
    ".c": r"^\/\/",
    ".py": r"^#",
    ".html": r"^<!--"
}

global noBlankLines
noBlankLinesOption = False

global noCommentsOption
noCommentsOption = False

global extensions
extensions = []

global ignore
ignore = []