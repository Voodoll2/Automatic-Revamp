from loginwithPython import nsgDriver
import DownloadModels as download
from os import listdir
from os.path import isfile, join, exists
from os import makedirs
from csvModels import csvToDict

mypath = "/Users/voodoll2/Desktop/Automatic/Models/"

#username = str(raw_input("Username: "))
#password = str(raw_input("Password: "))
username = "sc-eguetz"
password = "Xcaliber1"
driver = nsgDriver(username, password)
count = 0
inputZips = []

def command_line():
    alreadyLoggedIn = False
    global inputZips
    while True:
        userInput = str(raw_input(">>>"))
        if(userInput == 'autodownloadrun'):
            download.download()
            setInputZips()
            enter_files()
            alreadyLoggedIn = True
            run_task(alreadyLoggedIn)

        elif(userInput == 'autorun'):
            setInputZips()
            enter_files()
            alreadyLoggedIn = True
            run_task(alreadyLoggedIn)
            get_output(alreadyLoggedIn)
            rename_outputs()

        elif(userInput == "download"):
            download.download()
            setInputZips()
    
        elif(userInput == "login"):
            userInput = userInput.split(" ")
            enter_files()
            alreadyLoggedIn = True

        elif(userInput == "runall"):
            run_task(alreadyLoggedIn)

        elif(userInput == 'getoutputs'):
            get_output(alreadyLoggedIn)
            rename_outputs()

        elif(userInput == 'rename'):
            rename_outputs()

        elif(userInput == 'exit'):
            return

def enter_files():
    setInputZips()
    driver.login()
    global count
    modelnames = inputZips
    for modelname in modelnames:
        if modelname[0] == ".":
            continue
        else:
            driver.upload(modelname, True)
            count += 1
            make_task_from_data(True, modelname)
            driver.deletePreviousData(True)

def make_task_from_data(loggedIn, zipFile):
    print 'Making new task...'
    sheet = open("/Users/voodoll2/Desktop/Automatic/modelrun.csv", "rU")
    task_name = inputZips[count - 1]
    if task_name.endswith('.zip'):
        task_name = task_name[:-4]
    d = csvToDict(sheet)
    try:
        inputFileName = d[task_name]['Input File']
    except:
        return
    hours = 2
    nodes = d[task_name]['Nodes']
    cores = d[task_name]['Cores']
    driver.make_and_start_tasks(task_name, inputFileName, 'no', loggedIn, hours, nodes, cores)

def run_task(loggedIn):
    setInputZips()
    driver.run_task(len(inputZips), loggedIn)

def get_output(loggedIn):
    setInputZips()
    driver.download_outputs(len(inputZips), loggedIn)

def rename_outputs():
    setInputZips()
    print inputZips
    driver.renameOutputs()

def setInputZips():
    global inputZips
    driver.saveFileNames()
    inputZips = driver.getFileNames()

command_line()
