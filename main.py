from constants import helpString, emptyInputString, unknownCmdString


def parseInput(str):
    words = str.split()
    
    if (len(words) < 1):
        print(emptyInputString)
    elif (words[0] == "help"):
        print(helpString)
    else:
        print(unknownCmdString)


def main():
    while(True):
        userInput = input()
        parseInput(userInput)


if __name__ == "__main__":
    main()
