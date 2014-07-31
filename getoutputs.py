import time
from login import login
from Output import Output
from os import rename
from os.path import isfile, join

def step():
    blah = raw_input('step>>>')
    return

def getoutputs(driver, outputs, loggedIn, username, password):
        if not loggedIn:
            login(driver, username, password)
        time.sleep(1.3)
        tasksLink =driver.find_element_by_xpath('//*[@id="treemenu"]/tbody[2]/tr[2]/td[2]/a')
        tasksLink.click()
        time.sleep(2)
        refreshButton = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/div[3]/form[1]/table[1]/tbody/tr/td[1]/span/a')
        refreshButton.click()
        d = {}
        for i in range(len(outputs)):
            if i == 0:
                d = storeDataPositions(driver, len(outputs), loggedIn, username, password)
            rownum = d[outputs[i].desiredtarfile[:-7]]
            viewOutputPath = '//*[@id="task"]/table[1]/tbody/tr[%s]/td[9]/span/a' %str(rownum)
            viewOutputButton = driver.find_element_by_xpath(viewOutputPath)
            viewOutputButton.click()
            time.sleep(1)
            downloadButton = driver.find_element_by_xpath('//*[@id="setTaskOutput"]/table[1]/tbody/tr[4]/td[6]/span/a')
            downloadButton.click()
            time.sleep(1)
            step()
            renameOutput(outputs[i])
            step()
            returnToTaskButton = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/div[3]/span[2]/a')
            returnToTaskButton.click()
        print 'all downloaded'


def renameOutput(output):
    while not isfile(join(output.outputdirpath, 'output.tar.gz')):
        time.sleep(3)
        step()
    if isfile(join(output.outputdirpath, output.origtarfile)):
        step()
        print 'renaming'
        rename(join(output.outputdirpath, 'output.tar.gz'), join(output.outputdirpath, output.desiredtarfile))

def storeDataPositions(driver, numTasks, onTasksPage, username, password):
    if not onTasksPage:
        login(driver, username, password)
        time.sleep(1.3)
        tasksLink =driver.find_element_by_xpath('//*[@id="treemenu"]/tbody[2]/tr[2]/td[2]/a')
        tasksLink.click()
    d = {}
    for i in range(numTasks):
        taskLabelPath = '//*[@id="task"]/table[1]/tbody/tr[%s]/td[3]/span/a' %str(i + 2)
        taskLabel = None
        try:
            taskLabel = driver.find_element_by_xpath(taskLabelPath)
            if not taskLabel.text in d.keys():
                d[taskLabel.text] = i + 2
        except:
            continue
    return d

def storeOutputs(driver, numTasks, outputdirpath, onTasksPage, username, password):
    outputs = []
    d = storeDataPositions(driver, numTasks, onTasksPage, username, password)
    for k in d.keys():
        o = Output(outputdirpath, "output.tar.gz", k + '.tar.gz', None)
        outputs.append(o)
    return outputs


