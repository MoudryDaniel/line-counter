def showResult(dict):
    longestPath = len("File")
    longestValue = len("Lines")

    for key in dict:
        pathLength = len(key)
        if pathLength > longestPath:
            longestPath = pathLength

        valueLength = len(str(dict[key]))
        if valueLength > longestValue:
            longestValue = valueLength

    print("")
    # Header
    printRowDivider(longestPath, longestValue)
    printRow(longestPath, longestValue, "File", "Lines")
    printRowDivider(longestPath, longestValue)

    # Content of dictionary
    for key in dict:
        printRow(longestPath, longestValue, key, str(dict[key]))
        printRowDivider(longestPath, longestValue)
    
    # Sum of all lines
    print("Total number of lines: " + str(linesSum(dict)))
    print("")

def printRowDivider(longestPath, longestValue):
    print("+", end = "")
    for _ in range(longestPath + 2):
        print("-", end = "")
    print("+", end = "")
    for _ in range(longestValue + 2):
        print("-", end = "")
    print("+")

def printRow(longestPath, longestValue, file, lines):
    spaces = longestPath - len(file)
    print("| " + file, end = "")
    if spaces > 0:
        for _ in range(spaces):
            print(" ", end = "")

    spaces = longestValue - len(lines)
    print(" | ", end = "")
    if spaces > 0:
        for _ in range(spaces):
            print(" ", end = "")
    print(lines + " |")

def linesSum(dict):
    sum = 0
    for key in dict:
        sum += dict[key]

    return sum