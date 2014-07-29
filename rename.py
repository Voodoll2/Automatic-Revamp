import time
from os import listdir, rename, mkdir
from os.path import join
def step():
    print "When files are done downloading, press enter."
    x = raw_input(">>> ")
    return

def rename_out(pathToOutputs, label_list, folder_name):
    step()
    pathToOutputs = pathToOutputs + "/" + str(folder_name) + "/"
    contents = listdir(pathToOutputs)
    print contents           
    single = []
    tars = []
    tars.append("a")
    for f in contents:
        if f[-8:] == ').tar.gz' and f[0] != ".":
            tars.append(f)
    tars = sorted(tars)
    tars[0] = 'output.tar.gz'
    print tars
    length = len(tars)
    for num in range(length):
        print "Start: ", str(pathToOutputs) + str(tars[num]), "End: ", str(pathToOutputs) + str(label_list[num]) + '.tar.gz' 
        rename(str(pathToOutputs) + str(tars[num]), str(pathToOutputs) + str(label_list[num]) + '.tar.gz')
