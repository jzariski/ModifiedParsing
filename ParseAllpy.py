## Parses through a collection of .bed files for a given chromosome
## and optimizes a probeset based off of lowest G-percent, while
## maintaing no overlap.

import sys

## Note to use this include the chromosome number as the only argument
## in command line


class ParseAll:
    
    def __init__(self):
        pass
    
    ## Included for those who only want to scan certain coordinates 
    ## Not implmented in normal usage below
    def shortenList(self, start, stop, file):
        
        bigList = open(file, "r")

        finalList = []

        for line in bigList:
            
            tempList = line.split()

            tempStart = int(tempList[1])
            tempStop = int(tempList[2])

            
            if tempStart >= start and tempStop <= stop:
                finalList.append(line)

        finalFinalList = []
        for line in finalList:
            newList = line.split()
            finalFinalList.append(newList)
        
        return finalFinalList
    
    ## Adds g-percent value to lists since it is not in .bed file
    def addGPercent(self, noGList):
        probesParsed = 0

        for stuff in noGList:
            currSeq = stuff[4]
            total = len(currSeq)
            numG = 0.0
            for letter in currSeq:
                if letter == 'G':
                    numG = numG + 1.0
            
            percentG = numG / total
            stuff.append(percentG)
            probesParsed = probesParsed + 1
            if probesParsed % 10000 == 0:
                print str(probesParsed) + " out of " + str(len(noGList)) + " parsed"
        print "Done calculating G-Percent"
        print "\n"


    ## Combines all BigProbeFiles
    def createBigList(self, int1, int2):
        biggerList =[]
        for x in range(0, 26):
            fileName = "chrX_chm13_RC" + str(x) + ".bed"
            shortenedList = self.shortenList(int1, int2, fileName)
            for probe in shortenedList:
                biggerList.append(probe)
        return biggerList

    ## Parses through Big List
    def parseThrough(self, finalProbeSet, int1, int2):

        coordinateSet = [] ## Set of all coordinates that are in the final probe set (so far)
        bestProbes = []
        totalProbes = len(finalProbeSet)
        probesParsed = 0

        for probe in finalProbeSet:
            start = int(probe[1])
            end = int(probe[2])
            noOverlap = True
            currNum = start

            while (currNum <= end) and noOverlap:
                if currNum in coordinateSet:
                    noOverlap = False
                else:
                    coordinateSet.append(currNum)
                    currNum = currNum + 1
            
            if noOverlap:
                bestProbes.append(probe)
            
            probesParsed = probesParsed + 1
            
        ## Some optional values that can be implemented if needed
        percentCoverage = ((len(coordinateSet) * 1.0) / (int2-int1)) * 100
        kb = ((int2 - int1) * 1.0) / 1000
        probesKB = len(bestProbes) / kb
        ## Final parsed probe set
        return bestProbes

    
    def checkNoOverlap(self, list):
    ## ONLY DO THIS IF THE LIST HAS BEEN SORTED BY POSITION FIRST
        x = 0
        onlyPositive = True
        while x < len(parsedProbes) - 1 and onlyPositive:
            big = int(parsedProbes[x+1][1])
            small = int(parsedProbes[x][2])
            if (big - small) <= 0:
                onlyPositive = False
            x = x + 1
        if onlyPositive:
            print "There are no overlaps"
        else:
            print "Some overlaps exist"
        print "\n"


toParse = ParseAll()
chrNum = str(sys.argv[1])

## BigProbeFiles can be gotten from nexus library
fileName = 'BigProbeFile' + chrNum + '.txt'
shortFileName = 'chr' + chrNum
fileThing = open(fileName, 'r')
finalList = []

## Turning BigProbeFile into lists readable by above methods
for line in fileThing:
    tempFinalList = []
    tempFinalList.append(shortFileName)
    tempList = line.split()
    for item in tempList:
        tempFinalList.append(item)
    finalList.append(tempFinalList)
    
fileThing.close()
parsedProbes = toParse.parseThrough(finalList, 0, 1800000000) ## Large length covers hg38

## Sorting parsed probes by length
parsedProbes.sort(key = lambda x: x[1])
testFile = open('Parsed22.txt', 'w')
for thing in parsedProbes:
    for item in thing:
        testFile.write(str(item) + ' ')
    testFile.write('\n')
testFile.close()

##toParse.checkNoOverlap(parsedProbes)





