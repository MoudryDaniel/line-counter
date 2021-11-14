import os
import re

import global_vars as globalv

def count(target):
    lines = {}

    if os.path.isdir(target):
        targets = os.listdir(target)
        for targ in targets:
            res = count(os.path.join(target, targ))
            if res != {}:
                lines = lines | res
    else:
        extension = getExtension(target)
        if extension in globalv.commentRegexes:
            lines[target] = countLines(target, getExtension(target))

    return lines

def countLines(file, extension):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    count = 0
    for line in lines:
        line = line.strip()

        if line == "\0":
            continue

        if line == "":
            continue
        
        if re.search(globalv.commentRegexes.get(extension), line) is not None:
            continue

        count += 1

    return count

def getExtension(file):
    parts = file.split(".")
    return parts[-1]