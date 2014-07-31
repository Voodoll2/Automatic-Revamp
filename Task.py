class Task:
    def __init__(self, inputfilename, zipfilename, nodes, cores, runtime, tool):
        self.hocfile = inputfilename
        self.zipfile = zipfilename
        self.nodes = nodes
        self.cores = cores
        self.runtime = runtime
        self.tool = tool
    
    def __str__(self):
        return "[hoc: " + self.hocfile + ", zip: " + self.zipfile + "]"
    
    def __repr__(self):
        return self.__str__()
    
    def setRunTime(self, hours):
        self.runtime = hours
    
    def setNodes(self, numNodes):
        self.nodes = numNodes
    
    def setCores(self, numCores):
        self.cores = numCores
    
    def setHocFile(self, name):
        self.hocfile = name