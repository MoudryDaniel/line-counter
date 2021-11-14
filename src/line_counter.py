import sys

def main():
    global commentRegexes    
    commentRegexes = {
        "c": r"^\/\/",
        "py": r"^#",
        "html": r"^<!--"
        }

def error(msg):
    print(msg, file = sys.stderr)

if __name__ == "__main__":
    main()