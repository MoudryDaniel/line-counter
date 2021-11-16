#Created modules
import auxiliary as aux

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
    printHeader(longestPath, longestValue)
    printRowDivider(longestPath, longestValue)

    # Content of dictionary
    for key in dict:
        printRow(longestPath, longestValue, key, str(dict[key]))
        printRowDivider(longestPath, longestValue)
    
    # Sum of all lines
    print("Total number of lines: " + str(linesSum(dict)))
    print("")
    
    # Options
    printOptions()

def printHeader(longestPath, longestValue):
    longestPath = longestPath + 2 - len("File")
    rem = longestPath % 2
    spaces = longestPath // 2

    print("|", end = "")
    printCharSequence(" ", spaces)
    print("File", end = "")
    printCharSequence(" ", spaces)
    if rem == 1: print(" ", end = "")
    print("|", end = "")

    longestValue = longestValue + 2 - len("Lines")
    rem = longestValue % 2
    spaces = longestValue // 2

    printCharSequence(" ", spaces)
    print("Lines", end = "")
    printCharSequence(" ", spaces)
    if rem == 1: print(" ", end = "")
    print("|")

def printRowDivider(longestPath, longestValue):
    print("+", end = "")
    
    printCharSequence("-", longestPath + 2)
    print("+", end = "")
    printCharSequence("-", longestValue + 2)
    print("+")

def printRow(longestPath, longestValue, file, lines):
    spaces = longestPath - len(file)
    print("| " + file, end = "")
    if spaces > 0:
        printCharSequence(" ", spaces)

    spaces = longestValue - len(lines)
    print(" | ", end = "")
    if spaces > 0:
        printCharSequence(" ", spaces)
    print(lines + " |")

def printCharSequence(char, num):
    for _ in range(num): print(char, end = "")

def printOptions():
    print("Selected options: ")
    if aux.noBlankLinesOption: print(" -- Exclude blank lines")
    if aux.noCommentsOption: print(" -- Exclude comments")
    if aux.ignore: print(" -- Ignored extensions: "+ str(aux.ignore))
    if aux.extensions: print(" -- Possible extensions: "+ str(aux.extensions))
    print("")

def linesSum(dict):
    sum = 0
    for key in dict:
        sum += dict[key]

    return sum