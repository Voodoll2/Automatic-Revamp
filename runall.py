from Output import Output
from login import login
import time

def runAllTasks(driver, tasks, loggedIn, pathToOutputs, username, password):
    if not loggedIn:
        login(driver, username, password)
    time.sleep(1)
    task_link =driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
    task_link.click()
    outputs = []
    dictOfRows = {}
    for i in range(len(tasks)):
        if i == 0:
            dictOfRows = storeDataPositions(driver, len(tasks))
            print dictOfRows
        rowNum = dictOfRows[tasks[i].zipfile]
        runButtonPath = '//*[@id="task"]/table[1]/tbody/tr[%s]/td[9]/span/a' % (str(rowNum))
        runButton = driver.find_element_by_xpath(runButtonPath)
        runButton.click()
        o = None
        if i == 0:
            o = Output(pathToOutputs, "output.tar.gz", tasks[i].zipfile + '.tar.gz', None)
        else:
            o = Output(pathToOutputs, "output (%s).tar.gz" %(str(i)), tasks[i].zipfile + '.tar.gz', None)
        outputs.append(o)
        try:
            driver.switch_to_alert().accept()
        except:
            pass
        time.sleep(1)
    return outputs

def storeDataPositions(driver, numTasks):
    d = {}
    for i in range(numTasks):
        taskLabelPath = '//*[@id="task"]/table[1]/tbody/tr[%s]/td[3]/span/a' % (str(i + 2))
        taskLabel = None
        try:
            taskLabel = driver.find_element_by_xpath(taskLabelPath)
            if not taskLabel.text in d.keys():
                d[taskLabel.text] = i + 2
        except:
            continue
    return d



