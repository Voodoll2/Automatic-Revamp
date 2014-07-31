class Model:
    def __init__(self, directoryPath, zipfilename, csvCores, csvNodes, hocfile, tool):
        self.dirpath = directoryPath
        self.zipfile = zipfilename
        self.csvcores = csvCores
        self.csvnodes = csvNodes
        self.hocfile = hocfile
        self.dataid = None
        self.tool = tool
    
    def __str__(self):
        return "[dirPath: " + self.directorypath + ", zip: " + self.zipfile + "]"
    
    def __repr__(self):
        return self.__str__()
    
    def setDataId(self, idNum):
        self.dataid = idNum