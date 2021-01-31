import sys


## argments formed as such for chromosome 22 at G-Percent 10: 
##  python scriptwriter.py 10 chr22 22
chrnum = str(sys.argv[3]) 
num = str(sys.argv[1])
chr = str(sys.argv[2])
tempfilename = "tf" + chrnum + "_" + num + ".sh"
tempfile = open(tempfilename, "w")
chrfilename = chr + ".fa"
outputname = chr + "_" + num

tempfile.write("#!/bin/bash\n")
tempfile.write("cd bigParse/" + chr + "\n")
tempfile.write("source activate oligo_miner_env\n")
tempfile.write("python blockParseFinal.py -f " + chrfilename + " -b -l 20 -L 60 -t 35 -T 49 -RC -GON -g 0 -G " + num + " -o " + outputname)
