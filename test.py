import time
from os import listdir, rename, mkdir
from os.path import join
def step():
    print "When files are done downloading, enter a folder name and press enter."
    x = raw_input(">>> ")
    return x
folder_name = step()    
mkdir(str(pathToOutputs) + str(folder_name)) 
