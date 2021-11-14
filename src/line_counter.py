def main():
    global commentRegexes    
    commentRegexes = {
        "c": r"^\/\/",
        "py": r"^#",
        "html": r"^<!--"
        }

if __name__ == "__main__":
    main()