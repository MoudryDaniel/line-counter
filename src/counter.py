import os
import re

# Created modules
import auxiliary as aux

def count(target):
    lines = {}

    # Target is a directory
    if os.path.isdir(target):
        # Depth option check
        if aux.depth is not None:
            if aux.depth <= 0:
                return lines
            aux.depth -= 1
        
        targets = os.listdir(target)

        for targ in targets:
            res = count(os.path.join(target, targ))
            if res != {}:
                lines = lines | res
    
    # Target is a file
    else:
        extension = getExtension(target)
        # Extensions option check
        if aux.extensions and extension not in aux.extensions:
            return lines

        # Ignore option check
        if aux.ignore and extension in aux.ignore:
            return lines

        res = countLines(target, extension) 
        if res is not None:
            lines[target] = res

    return lines

def countLines(file, extension):
    try:
        with open(file, "r") as f:
            lines = f.read().splitlines()
    except:
        return None

    count = 0
    for line in lines:
        line = line.strip()

        # No empty lines option check
        if aux.noBlankLinesOption:
            if line == "\0" or line == "": continue
        
        # No comments option check
        if aux.noCommentsOption:
            regex = aux.commentRegexes.get(extension)
            if regex is None:
                aux.error("List of regular expressions doesn't contain deffinition for " + extension + " file comments")
            if re.search(regex, line) is not None: continue

        count += 1

    return count

def getExtension(file):
    _, extension = os.path.splitext(file)
    return extension