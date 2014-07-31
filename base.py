from selenium import webdriver
from os import listdir
from os.path import isfile, join
import re
from Model import Model
from login import login
from upload import uploadFile
from makealltasks import makeAllTasks
from csvmodels import csvToDict
from runall import runAllTasks
from getoutputs import getoutputs, storeOutputs
import download

userfile = str(raw_input("Where Are Models Stored: "))
username = ""
password = "changeme"
person =str(raw_input("User: "))
if person == 'v':
	chromePath = "/home/vasu/Desktop/paths/chromedriver/chromedriver"
	pathToModels = "/home/vasu/Desktop/paths/Models/"
	pathToOutputs = "/home/vasu/Desktop/paths/Outputs/"
	csvsheets = open("/home/vasu/Desktop/Automatic 2/modelrun.csv", "rU")
elif person == "s":
	pathToModels = "/home/steve/Programming/pythondev/nsgwork/" + userfile + "/" 
	pathToOutputs = "/home/steve/Programming/pythondev/nsgwork/" + userfile + "outputs/"
	chromePath = "/home/steve/Programming/pythondev/chromedriver"
	csvsheet = 'modelrun.csv'
elif person == "e":
	chromePath = "/Users/voodoll2/Desktop/paths/chromedriver/chromedriver"
	pathToModels = "/Users/voodoll2/Desktop/paths/Models/"
	pathToOutputs = "/Users/voodoll2/Desktop/paths/Outputs"
	csvsheet = open("/Users/voodoll2/Desktop/Auto/modelrun.csv", "rU")

account =str(raw_input("Account: "))
if account == "e":
	username = "sc-eguetz"
elif account == "v":
	username = "sc-vvikram"
elif account == "s":
	username = "sc-sseshan"
elif account == "v2":
	username = "vasutest"
elif account == "s2":
	username = "seshantest"


nodescores = str(raw_input('csv or nodes:cores >>> '))


chromeOptions = webdriver.ChromeOptions()
prefs = {'download.default_directory': pathToOutputs}
chromeOptions.add_experimental_option('prefs',prefs)
phantomjs_path = "/home/steve/Programming/phantomjs-1.9.7-linux-i686/bin/phantomjs"
driver = webdriver.Chrome(executable_path=chromePath, chrome_options=chromeOptions)

def command_line():
    alreadyLoggedIn = False
    tasks = []
    outputs = []
    while True:
        userInput = str(raw_input(">>>"))
        if(userInput == 'autodownloadrun'):
            download.download(pathToModels)
            login(driver, username, password)
            alreadyLoggedIn = True
            tasks = uploadAll(driver, alreadyLoggedIn, username, password, nodescores)
            makeAllTasks(driver, tasks, alreadyLoggedIn, username, password)
            outputs = runAllTasks(driver, tasks, alreadyLoggedIn, pathToOutputs, username, password)
            print "outputs: ", outputs
            
        elif(userInput == 'autorun'):
            login(driver, username, password)
            alreadyLoggedIn = True
            tasks = uploadAll(driver, alreadyLoggedIn, username, password, nodescores)
            print "tasks: ", tasks
            makeAllTasks(driver, tasks, alreadyLoggedIn, username, password)
            outputs = runAllTasks(driver, tasks, alreadyLoggedIn, pathToOutputs, username, password)
            print "Outputs: ", outputs

        elif(userInput == "download"):
            download.download(pathToModels)
    
        elif(userInput == "login"):
            login(driver, username, password)
            alreadyLoggedIn = True
        
        elif(userInput == "uploadandmaketasks"):
            tasks = uploadAll(driver, alreadyLoggedIn, username, password, nodescores)
            print "tasks: ", tasks
            makeAllTasks(driver, tasks, alreadyLoggedIn, username, password)

        elif(userInput == "runall"):
            outputs = runAllTasks(driver, tasks, pathToOutputs, alreadyLoggedIn, username, password)
            print "outputs: ", outputs
        
        elif(userInput == "getoutputs"):
            if not alreadyLoggedIn:
                count = 0
                for f in listdir(pathToModels):
                    count += 1
                    print count
                outputs = storeOutputs(driver, count, pathToOutputs, alreadyLoggedIn, username, password)
                print outputs
                alreadyLoggedIn = True
            getoutputs(driver, outputs, alreadyLoggedIn, username, password)
        
        elif(userInput == "exit"):
            return

def customSortKey(filename):
    return int(filename[2:3])

def uploadAll(driver, loggedIn, username, password, nodescores):
    allContents = listdir(pathToModels)
    allContents = sorted(allContents, key=customSortKey)
    zips = []
    tasks = []
    for f in allContents:
        if isfile(join(pathToModels, f)):
            zips.append(f)
    d = csvToDict(open(csvsheet))
    for f in zips:
        n = 0
        c = 0
        if nodescores == 'csv':
            n = d[f]['Nodes']
            c = d[f]['Cores']
        else:
            regexnodes = re.findall('\d+:', nodescores)
            n = int(regexnodes[0][:-1])
            regexcores = re.findall(':\d+', nodescores)
            c = int(regexcores[0][1:])
        mod = Model(pathToModels, f, c, n, d[f]['Input File'], 'Neuron')
        tasks.append(uploadFile(driver, mod, loggedIn, username, password))
    return tasks

def createAllOutputObjects(driver, numTasks, pathToOutputs, pathToModels):
    pass

command_line()
