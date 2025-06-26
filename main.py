from constants import *
from queries import *


def parseInput(str):
    args = str.split()
    
    if (len(args) < 1):
        print(emptyInputString)
        return
    
    cmd = args[0]

    if (cmd == "help"):
        print(helpString)

    elif (cmd == "top-population"):
        if (len(args) < 2):
            print("Missing argument: [number of countries]")
        else:
            getByDescPopulation(args[1])

    elif (cmd == "language"):
        if (len(args) < 2):
            print("Missing argument: [language]")
        else:
            getByLanguage(args[1])
    
    elif (cmd == "longest-name"):
        getByLongestName()

    elif (cmd == "hemisphere"):
        if (len(args) < 2):
            print("Missing argument: [hemisphere]")
        else:
            getByHemisphere(args[1])

    elif (cmd == "avg-population"):
        getAveragePopulation(args[1])

    elif (cmd == "temperature"):
        if (len(args) < 3):
            print("Missing arguments: [lat] [long]")
        else:
            getCurrTemp(args[1], args[2])

    elif (cmd == "precipitation"):
        if (len(args) < 3):
            print("Missing arguments: [lat] [long]")
        else:
            getCurrPrecip(args[1], args[2])
    
    # save --format json|csv --output countries.json
    elif (cmd == "save"):
        fileType = defaultType
        path = defaultPath
        getAllCountries(fileType, path)

    else:
        print(unknownCmdString)


def main():
    while(True):
        userInput = input()
        parseInput(userInput)


if __name__ == "__main__":
    main()
