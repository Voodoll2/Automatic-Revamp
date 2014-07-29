from os import listdir, rename
from os.path import join
def rename_out(pathToOutputs, label_list):
    pathToOutputs += "/"
    contents = listdir(pathToOutputs)
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

