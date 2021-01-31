import sys

class FileWriter:
    
    def __init__(self):
        self.chrNum = str(sys.argv[1])
        pass

    def writeBigFile(self):
        bigList = self.createBigList(0,180000000)
        self.addGPercent(bigList)
        filename = "BigProbeFile" + self.chrNum + ".txt"
        outputFile = open(filename, "w")
        for probe in bigList:
            thing = str(probe[1]) + " " + str(probe[2]) + " " + str(probe[4]) + " " + str(probe[6])
            outputFile.write(thing)
            outputFile.write("\n")
        outputFile.close()

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
        
        bigList.close()
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

    
    def createBigList(self, int1, int2):
        biggerList =[]
        for x in range(0, 26):
            fileName = "chr" + self.chrNum + "_" + str(x) + ".bed"
            shortenedList = self.shortenList(int1, int2, fileName)
            for probe in shortenedList:
                biggerList.append(probe)
            print fileName + " is shortened to probes between " + str(int1) + " and " + str(int2)
        return biggerList


writerThing = FileWriter()
writerThing.writeBigFile()



