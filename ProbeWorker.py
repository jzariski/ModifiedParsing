import pandas as pd
import ParseAllFinal as paf

toParse = paf.ParseAllFinal()


## Parses through list to optimize probes in given range
## Outputs as a csv file
def dataFrameCreator(toParse, text, start, end, saved, bigFile):
    print("Welcome to the data frame creator\n")
    dataName = saved
    fileName = bigFile
    allList = toParse.createBigList(start, end, text, fileName)
    parsedProbes = toParse.parseThrough(allList, start, end, text)
    dataFrame = pd.DataFrame(parsedProbes,columns=['Start','End','Strand','gPercent'],dtype=float)
    dataFrame['Start'] = dataFrame['Start'].astype(int)
    dataFrame['End'] = dataFrame['End'].astype(int)
    dataFrame['Strand'] = dataFrame['Strand'].astype(str)
    print(dataFrame)
    dataFrame.to_csv(dataName)


## Client part to choose option
print("Welcome to the Probe Worker")

choice = input("Enter 1 for parsing, 2 for narrowing: ")

if choice == "1":
    bigFile = input("Enter big file name: ")

    text = False
    textI = input("Show text information (y/n)? ")
    if textI == "y":
        text = True
    elif textI == "n":
        text = False
    else:
        raise ValueError("Enter 'y' or 'n'")


    start = int(input("Enter start coordinate: "))
    end = int(input("Enter end coordinate: "))

    if end < start:
        raise ValueError("Start coordinate must be less than end coordinate")

    name = input("Enter name for output csv file: ")

    dataFrameCreator(toParse, text, start, end, name, bigFile)

## Allows editing of csv file based on coordinate or g-percent
## Outputs as new csv file
elif choice == "2":
    fileName = input("Enter csv file: ")
    newFileName = input("Enter output file: ")
    df = pd.read_csv(fileName)

    start = input("Enter start coordinate: ")
    end = input("Enter end coordinate: ")
    gPercentLow = input("Enter low gPercent: ")
    gPercentHigh = input("Enter high gPercent: ")

    newSet = []

    for index, row in df.iterrows():
        if int(row["Start"]) >= int(start) and int(row["End"]) <= int(end):
            if float(row["gPercent"]) >= float(gPercentLow) and float(row["gPercent"]) <= float(gPercentHigh):
                newSet.append([int(row["Start"]), int(row["End"]), str(row["Strand"]), float(row["gPercent"])])

    dataFrame = pd.DataFrame(newSet,columns=['Start','End','Strand','gPercent'],dtype=float)
    dataFrame['Start'] = dataFrame['Start'].astype(int)
    dataFrame['End'] = dataFrame['End'].astype(int)
    dataFrame['Strand'] = dataFrame['Strand'].astype(str)

    print(dataFrame)
    dataFrame.to_csv(newFileName)

else:
    raise ValueError("Enter '1' or '2'")











