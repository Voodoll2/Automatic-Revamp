import csv

class modelObject:
    def __init__(self, accessNumber, fileName, outputFileName, inputFileName, cores, nodes, linkToModeldb):
        self.accessNumber = accessNumber
        self.fileName = fileName
        self. outputFileName = outputFileName
        self. inputFileName = inputFileName
        self. cores = cores
        self. nodes = nodes
        self.linkToModeldb = linkToModeldb

    def getAccessNumber(self):
        return self.accessNumber
    def getFileName(self):
        return self.fileName
    def getOutputFileName(self):
        return self.outputFileName
    def getInputFileName(self):
        return self.inputFileName
    def getCores(self):
        return self.cores
    def getNodes(self):
        return self.nodes
    def getLink(self):
        return self.linkToModeldb

def csvToObjects(csvFile):
    reader = csv.reader(csvPath)
    modelObjects = []
    for row in reader:
        modelObjects.append(modelObject(row[2], row[1], row[3], row[4], row[7], row[8], row[9]))
    return modelObjects

def csvToDict(csvFile):
    reader = csv.reader(csvFile)
    modelDict = {}
    for row in reader:
        modelDict[row[2]] = {'Input File': row[4], 'Zip File': row[1], 'Output File': row[3], 'Cores': row[7], 'Nodes': row[8], 'Link': row[9]}
    return modelDict

# d = csvToDict(sheet)
# count = 1
# for k in d.keys():
#     print "%d >>> Access Number: %s >>> Input File: %s" % (count, k, d[k]['Input File'])
#     count += 1
