import csv
def csvToDict(csvFile):
    reader = csv.reader(csvFile)
    modelDict = {}
    for row in reader:
        modelDict[row[2]] = {'Input File': row[4], 'Zip File': row[1], 'Output File': row[3], 'Cores': row[7], 'Nodes': row[8], 'Link': row[9]}
    return modelDict