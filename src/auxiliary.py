import sys

def error(msg):
    print("ERROR: " + msg, file = sys.stderr)
    sys.exit(1)

global commentRegexes    
commentRegexes = {
    ".c": r"^\/\/",
    ".py": r"^#",
    ".html": r"^<!--",
    ".bat": r"^::",
    ".cpp": r"\/\/",
    ".java": r"\/\/",
    ".pl" :r"#", 
    ".s": r";",
    ".sh": r"^#"
    }
# TODO: add multiple possibilities for comments e.g. REM for .bat

global noBlankLines
noBlankLinesOption = False

global noCommentsOption
noCommentsOption = False

global extensions
extensions = []

global ignore
ignore = []

global depthOriginalValue
global depth
depthOriginalValue = None
depth = None