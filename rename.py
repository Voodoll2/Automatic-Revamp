import time
from os import listdir, rename
from os.path import join
def rename_out(pathToOutputs, label_list, user):
    pathToOutputs += "/"
    contents = listdir(pathToOutputs)
    print contents
    global q
    q = ""
    while q != "exit":
        contents = listdir(pathToOutputs)
        for f in contents:
            if "crdownload" in f:
                print "waiting..."
                time.sleep(1)
            else:
                q == "exit"
    single = []
    tars = []
    if user == "sc-eguetz":
        tars.append("a")
        for f in contents:
            if f[-8:] == ').tar.gz' and f[0] != ".":
                tars.append(f)
        tars = sorted(tars)
        tars[0] = 'output.tar.gz'
    else:
        tars.append("output.tar.gz")
        for f in contents:
            if f[-8:] == ').tar.gz':
                tars.append(f)
    print tars
    length = len(tars)
    for num in range(length):
        print "Start: ", str(pathToOutputs) + str(tars[num]), "End: ", str(pathToOutputs) + str(label_list[num]) + '.tar.gz' 
        rename(str(pathToOutputs) + str(tars[num]), str(pathToOutputs) + str(label_list[num]) + '.tar.gz')

labels = ['106551', '112359', '10360', '112834', '113732']
path = "/Users/voodoll2/Desktop/Paths/Outputs"
rename_out(path, labels, "sc-")
