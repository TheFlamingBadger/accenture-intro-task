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
            getByDescPopulation(int(args[1]))

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
        getAveragePopulation()

    elif (cmd == "temperature"):
        if (len(args) < 3):
            print("Missing arguments: [lat] [long]")
        else:
            getCurrTemp(float(args[1]), float(args[2]))

    elif (cmd == "precipitation"):
        if (len(args) < 3):
            print("Missing arguments: [lat] [long]")
        else:
            getCurrPrecip(float(args[1]), float(args[2]))
    
    elif (cmd == "save"):
        fileType = defaultType
        path = defaultPath

        if (len(args) > 2):
            for i in range(1,len(args)):
                if (args[i] == "--format"):
                    if (i+1 <= len(args) and args[i+1] == "csv"):
                        fileType = "csv"
                elif (args[i] == "--path"):
                    if (i+1 <= len(args)):
                        path = args[i+1]

        getAllCountries(fileType, path)

    else:
        print(unknownCmdString)


def main():
    while(True):
        userInput = input()
        parseInput(userInput)


if __name__ == "__main__":
    main()
