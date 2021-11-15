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

global noEmptyLines
noEmptyLinesOption = False

global noCommentsOption
noCommentsOption = False