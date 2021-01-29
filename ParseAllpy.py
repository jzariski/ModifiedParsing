import sys


class ParseAll:
    
    def __init__(self):
        pass

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


    
    def createBigList(self, int1, int2):
        biggerList =[]
        for x in range(13, 26):
            fileName = "chrX_chm13_RC" + str(x) + ".bed"
            shortenedList = self.shortenList(int1, int2, fileName)
            for probe in shortenedList:
                biggerList.append(probe)
            print fileName + " is shortened to probes between " + str(int1) + " and " + str(int2)
        print "Done shortening lists"
        print "\n"
        return biggerList

    def parseThrough(self, finalProbeSet, int1, int2):

        coordinateSet = []
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
            
            if probesParsed % 1000 == 0:
                print str(probesParsed) + " out of " + str(len(finalProbeSet)) + " parsed"
        
        print "Done parsing"
        print "\n"
        percentCoverage = ((len(coordinateSet) * 1.0) / (int2-int1)) * 100
        print "Final Percent Coverage: " + str(percentCoverage)
        kb = ((int2 - int1) * 1.0) / 1000
        probesKB = len(bestProbes) / kb
        print "Probes per kilobase: " + str(probesKB)
        return bestProbes

    def bubbleSortPosition(self, list):
        for itr in range(len(list) - 1, 0, -1):
            for idx in range(itr):
                if int(list[idx][1]) > int(list[idx + 1][1]):
                    temp = list[idx]
                    list[idx] = list[idx + 1]
                    list[idx + 1] = temp
    
    def bubbleSortG(self, list):
        for itr in range(len(list) - 1, 0, -1):
            for idx in range(itr):
                if float(list[idx][6]) > float(list[idx + 1][6]):
                    temp = list[idx]
                    list[idx] = list[idx + 1]
                    list[idx + 1] = temp

    def checkNoOverlap(self, list):
    ## ONLY DO THIS IF THE LIST HAS BEEN BUBBLE SORTED BY POSITION FIRST
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

print "Beginning selection process"
print "\n"
toParse = ParseAll()
chrNum = str(sys.argv[1])
fileName = 'BigProbeFile' + chrNum + '.txt'
shortFileName = 'chr' + chrNum
fileThing = open(fileName, 'r')
finalList = []
print "Making new list"
for line in fileThing:
    tempFinalList = []
    tempFinalList.append(shortFileName)
    tempList = line.split()
    for item in tempList:
        tempFinalList.append(item)
    finalList.append(tempFinalList)
fileThing.close()
print "Parsing"
parsedProbes = toParse.parseThrough(finalList, 0, 180000000)
parsedProbes.sort(key = lambda x: x[1])
testFile = open('Parsed22.txt', 'w')
for thing in parsedProbes:
    for item in thing:
        testFile.write(str(item) + ' ')
    testFile.write('\n')
testFile.close()

##toParse.checkNoOverlap(parsedProbes)





