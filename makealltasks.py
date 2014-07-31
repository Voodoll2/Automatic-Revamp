from login import login
import time

def makeAllTasks(driver, tasks, loggedIn, username, password):
    if not loggedIn:
        login(driver, username, password)
    time.sleep(1)
    dictOfInputData = {}
    for i in range(len(tasks)):
        task_link =driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
        task_link_text = task_link.text
        if task_link_text == "Tasks (0)":
            task_link.click()
            time.sleep(1)
            createtasks = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/span/a")
            createtasks.click()
        else:
            task_link.click()
            time.sleep(1)
            createtasks =driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table[2]/tbody/tr/td[2]/span/a")
            createtasks.click()
        time.sleep(1)
        description_label =driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[2]/td[2]/input")
        description_label.send_keys(tasks[i].zipfile)
        print 'setting parameters'
        print 'select input data'
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[3]/td[2]/span/a").click()
        print 'select corresponding data'
        time.sleep(0.3)
        if(i == 0):
            dictOfInputData = storeDataPositions(driver, 70)
        rowNum = dictOfInputData[tasks[i].zipfile]
        print 'rownum: ', rowNum
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/div[3]/form/table[1]/tbody/tr[%s]/td[1]/input[1]' % str(rowNum)).click()
        print 'confirm select data'
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td/input").click()
        print 'choose tool'
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[4]/td[2]/span/a").click()
        print 'select neuron'
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[4]/ul/li[6]/strong/a").click()
        print 'choose parameters'
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[5]/td[2]/span/a/span").click()
        print  'specify runall time'
        time.sleep(0.2)
        driver.find_element_by_id('neuron73_tg_runtime_').clear()
        driver.find_element_by_id('neuron73_tg_runtime_').send_keys(str(tasks[i].runtime))
        print 'enter input file name'
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/div/div/input[2]").clear()
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/div/div/input[2]").send_keys(tasks[i].hocfile.strip())
        print 'enter number of nodes'
        time.sleep(0.3)
        try:
            driver.find_element_by_id('neuron73_tg_number_nodes_').clear()
        except:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="createTask"]/table[1]/tbody/tr[5]/td[2]/span/a').click()
            driver.find_element_by_id('neuron73_tg_number_nodes_').clear()
        driver.find_element_by_id('neuron73_tg_number_nodes_').send_keys(str(tasks[i].nodes))
        print 'enter number of cores'
        time.sleep(0.3)
        driver.find_element_by_id('neuron73_tg_number_cores_').clear()
        driver.find_element_by_id('neuron73_tg_number_cores_').send_keys(str(tasks[i].cores))
        print 'save parameters'
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/input").click()
        print 'save task'
        time.sleep(0.2)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td/input").click()    
        print "Made Task: ", tasks[i].zipfile


def storeDataPositions(driver, numTasks):
    d = {}
    for i in range(numTasks):
        inputDataLabelPath = '/html/body/div/div/div[2]/div[1]/div/div[2]/div[3]/form/table[1]/tbody/tr[%s]/td[4]' % (str(i + 2))
        inputDataLabel = None
        try:
            inputDataLabel = driver.find_element_by_xpath(inputDataLabelPath)
            if not inputDataLabel.text in d.keys():
                d[inputDataLabel.text] = i + 2
        except:
            continue
    return d


