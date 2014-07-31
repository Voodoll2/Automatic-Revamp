from Task import Task
class Output:
    def __init__(self, directoryPath, originalTarFileName, desiredTarFileName, unzipDirectoryPath):
        self.outputdirpath = directoryPath
        self.origtarfile = originalTarFileName
        self.unzipdirpath = unzipDirectoryPath
        self.desiredtarfile = desiredTarFileName
    
    def __str__(self):
        return "[outputpath: " + self.outputdirpath + ", desiredtar: " + self.desiredtarfile + "]"
    
    def __repr__(self):
        return self.__str__()
    
    def setOutputDirPath(self, path):
        self.outputdirpath = path

