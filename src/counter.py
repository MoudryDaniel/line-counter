import os
import re

# Created modules
import auxiliary as aux

def count(target):
    lines = {}

    # Target is a directory
    if os.path.isdir(target):
        targets = os.listdir(target)

        for targ in targets:
            res = count(os.path.join(target, targ))
            if res != {}:
                lines = lines | res
    
    # Target is a file
    else:
        res = countLines(target) 
        if res is not None:
            lines[target] = res

    return lines

def countLines(file):
    try:
        with open(file, "r") as f:
            lines = f.read().splitlines()
    except:
        return None

    count = 0
    for line in lines:
        line = line.strip()

        # No empty lines option
        if aux.noEmptyLinesOption:
            if line == "\0" or line == "": continue
        
        # No comments option
        if aux.noCommentsOption:
            extension = getExtension(file)
            regex = aux.commentRegexes.get(extension)
            if regex is None:
                aux.error("List of regular expressions doesn't contain deffinition for " + extension + " file comments")
            if re.search(regex, line) is not None: continue

        count += 1

    return count

def getExtension(file):
    _, extension = os.path.splitext(file)
    return extension