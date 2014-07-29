from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from os import listdir, rename, makedirs
from os.path import isfile, join, exists
import datetime

##user2 = str(raw_input("User: "))
##if user2 == "e":
##    user2 = "sc-eguetz"
##elif user2 == "v":
##    user2 = "sc-vvikram"
##elif user2 == "s":
##    user2 = "sc-sseshan"
chromePath = "/Users/voodoll2/Desktop/Automatic/chromedriver"
pathToModels = "/Users/voodoll2/Desktop/Automatic/Models/"
pathToOutputs = '/Users/voodoll2/Desktop/Automatic/Outputs'
loginURL = 'http://www.nsgportal.org/portal/login!input.action'

def step():
    blah = raw_input('>>> ')
    return

class nsgDriver:
    def __init__(self, username, password):
        self.chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory': pathToOutputs}
        self.chromeOptions.add_experimental_option('prefs',prefs)
        #phantomjs_path = "/home/steve/Programming/phantomjs-1.9.7-linux-i686/bin/phantomjs"
        self.driver = webdriver.Chrome(executable_path=chromePath, chrome_options=self.chromeOptions)
        # self.driver = webdriver.PhantomJS(phantomjs_path)
        self.uname = username
        self.pword = password
        self.inputZipFiles = []

    def login(self):
        """Open nsg portal login page"""
        self.driver.get(loginURL)
        try:
            self.driver.switch_to_alert().accept()
        except:
            pass
        """Send the username keys to the form and press tab"""
        elem =self.driver.find_element_by_name("username")
        elem.send_keys(self.uname)
        elem.send_keys(Keys.TAB)
        """Send the password keys to the form and press enter"""
        elem2 =self.driver.find_element_by_name("currentPassword")
        elem2.send_keys(self.pword)
        elem2.send_keys(Keys.RETURN)

    def upload(self, filename, loggedIn):
        if not loggedIn:
            self.login()
        """Find the data_link"""
        data_link = None
        try:
            data_link = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr/td[2]/a")
        except:
            plus_button = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[1]/div/table/tbody[1]/tr/th/a")
            plus_button.click()
            data_link = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr/td[2]/a")
        data_link_text = data_link.text
        """Click the data link in the sidebar"""
        if data_link_text == "Data (0)":
            data_link.click()
            time.sleep(0.5)
            upload_link =self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/span/a')
            upload_link.click()
        else:
            data_link.click()
            time.sleep(0.5)
            upload_link =self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/fieldset[2]/table/tbody/tr/td[2]/span/a')
            upload_link.click()
        time.sleep(1)
        """Give the file to the website to store as data"""
        browse_link =self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input')
        """Make the label of the data"""
        filename = filename.strip('"')
        browse_link.send_keys(pathToModels + str(filename))
        text_field =self.driver.find_element_by_xpath('//*[@id="pasteData_label"]')
        text_field.send_keys(filename)
        #time.sleep(10)
        """Save the data with file and label"""
        save_button =self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/form/table/tbody/tr[4]/td/input")
        #time.sleep(10)
        print "Looking..."
        time.sleep(2)
        save_button.click()
        print "Clicked"
        print "File Uploaded: ", filename

    def make_and_start_tasks(self, task_name, mainInputFile, run_after, loggedIn, hours, nodes, cores):
        if not loggedIn:
            self.login()
        time.sleep(1)
        task_link =self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
        task_link_text = task_link.text
        if task_link_text == "Tasks (0)":
            task_link.click()
            time.sleep(1)
            tasks =self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/span/a")
            tasks.click()
        else:
            task_link.click()
            time.sleep(1)
            tasks =self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table[2]/tbody/tr/td[2]/span/a")
            tasks.click()
        time.sleep(1)
        description_label =self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[2]/td[2]/input")
        description_label.send_keys(task_name)
        print 'setting parameters'
        print 'select input data'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[3]/td[2]/span/a").click()
        print 'select all data'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr/th/input").click()
        print 'confirm select data'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td/input").click()
        # step()
        print 'choose tool'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[4]/td[2]/span/a").click()
        # step()
        print 'select neuron'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[4]/ul/li[6]/strong/a").click()
        # step()
        print 'choose parameters'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[5]/td[2]/span/a/span").click()
        # step()
        print  'specify run time'
        time.sleep(0.2)
        self.driver.find_element_by_id('neuron73_tg_runtime_').clear()
        self.driver.find_element_by_id('neuron73_tg_runtime_').send_keys(hours)
        # step()
        print 'enter input file name'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/div/div/input[2]").clear()
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/div/div/input[2]").send_keys(mainInputFile.strip())
        # step()
        print 'enter number of nodes'
        time.sleep(0.3)
        try:
            self.driver.find_element_by_id('neuron73_tg_number_nodes_').clear()
        except:
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="createTask"]/table[1]/tbody/tr[5]/td[2]/span/a').click()
            self.driver.find_element_by_id('neuron73_tg_number_nodes_').clear()
        self.driver.find_element_by_id('neuron73_tg_number_nodes_').send_keys(str(nodes))
        # step()
        print 'enter number of cores'
        time.sleep(0.3)
        self.driver.find_element_by_id('neuron73_tg_number_cores_').clear()
        self.driver.find_element_by_id('neuron73_tg_number_cores_').send_keys(str(cores))
        # step()
        print 'click 9'
        time.sleep(0.3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/input").click()
        saveTask = 'yes'
        if(saveTask == "yes" or saveTask == "Yes"):
            if(run_after == "yes" or run_after == "Yes"):
                self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td[2]/input").click()
                self.driver.switch_to_alert().accept()
                time.sleep(5)
            else:
                self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td/input").click()
        else:
            self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td[3]/input").click()
        print "Made Task: ", task_name
        print "Will run after: " + run_after

    def deletePreviousData(self, loggedIn):
        if not loggedIn:
            self.login()
        """Find the data_link"""
        data_link =self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr/td[2]/a")
        data_link_text = data_link.text
        """Click the data link in the sidebar"""
        if not data_link_text == "Data (0)":
            data_link.click()
            self.driver.find_element_by_id('data_allChecked').click()
            self.driver.find_elements_by_id('data__cancel')[1].click()
            try:
                self.driver.switch_to_alert().accept()
            except:
                pass
        time.sleep(1)

    def viewStatus(self, startTimeList, taskNameList):
        numCompleted = 0
        stopTimes = []
        length = len(startTimeList)
        for i in range(length):
            stopTimes.append(0)
        completed = []
        runTimeFileName = 'runtimes1.txt'
        if runTimeFileName not in listdir(r"/Users/voodoll2/Desktop/Automatic/Outputs"):
            runTimeFile = open(r'/Users/voodoll2/Desktop/Automatic/Outputs/runtimes1.txt', 'w')
            runTimeFile.close()
        while(numCompleted < length):
            time.sleep(2)
            runTimeFile = open(r'/Users/voodoll2/Desktop/Automatic/Outputs/runtimes.txt', 'a+')
            for i in range(len(startTimeList)):
                path = '/html/body/div/div/div[2]/div[1]/div/div[2]/div[3]/form[2]/table[1]/tbody/tr[%s]/td[7]/span/a' % str(i + 2)
                try:
                    self.driver.find_element_by_xpath(path)
                    if not i in completed:
                        completed.append(i)
                        stopTimes[i] = datetime.datetime.now()
                        print 'task %s complete' %taskNameList[length - i - 1]
                        numCompleted += 1
                        differenceSeconds = (stopTimes[i] - startTimeList[i]).seconds
                        print 'difference Seconds: ', differenceSeconds
                        hours = differenceSeconds / 3600
                        minutes = (differenceSeconds%3600) / 60
                        seconds = differenceSeconds % 60
                        line = '%s ran for %s hours >>> %s minutes >>> %s seconds\n' % (taskNameList[length - n - 1], str(hours), str(minutes), str(seconds))
                        runTimeFile.write(line)
                        runTimeFile.close()
                except:
                    print 'task %s not complete' %taskNameList[length - i - 1]
                    continue
            refreshButton = self.driver.find_element_by_xpath('//*[@id="paginateTasks"]/table[1]/tbody/tr/td[1]/span/a')
            refreshButton.click()

    def run_task(self, numTasks, loggedIn):
        if not loggedIn:
            self.login()
        time.sleep(1)
        task_link =self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
        task_link.click()
        startTimes = []
        for num in range(2, 2 + numTasks):
            path = '//*[@id="task"]/table[1]/tbody/tr[%s]/td[9]/span/a' %str(num)
            runButton = self.driver.find_element_by_xpath(path)
            runButton.click()
            startTime = datetime.datetime.now()
            startTimes.append(startTime)
            try:
                self.driver.switch_to_alert().accept()
            except:
                pass
            time.sleep(2)
        self.viewStatus(startTimes, self.inputZipFiles)

    def download_outputs(self, numTasks, loggedIn):
        if not loggedIn:
            self.login()
        time.sleep(1.3)
        tasksLink =self.driver.find_element_by_xpath('//*[@id="treemenu"]/tbody[2]/tr[2]/td[2]/a')
        tasksLink.click()
        # self.saveOutputFolderNamesInRunOrder()
        ##  finds and clicks on view output link
        time.sleep(2)
        refreshButton = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/div[3]/form[1]/table[1]/tbody/tr/td[1]/span/a')
        refreshButton.click()
        for num in range(2, 2 + numTasks):
            xpath = '//*[@id="task"]/table[1]/tbody/tr[%s]/td[9]/span/a' %str(num)
            viewOutputButton =self.driver.find_element_by_xpath(xpath)
            viewOutputButton.click()
            time.sleep(1)
            downloadButton = self.driver.find_element_by_xpath('//*[@id="setTaskOutput"]/table[1]/tbody/tr[4]/td[6]/span/a')
            downloadButton.click()
            time.sleep(1)
            returnToTaskButton = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/div[3]/span[2]/a')
            returnToTaskButton.click()
        print 'all downloaded'

    def saveFileNames(self):
        self.inputZipFiles = sorted(listdir(pathToModels))

    def getFileNames(self):
        return self.inputZipFiles

    def renameOutputs(self):
        contents = listdir(pathToOutputs)
        single = []
        tars = []
        for f in contents:
            if f.endswith(').tar.gz'):
                tars.append(f)
        single.append('output.tar.gz')
        tars = sorted(tars)
        single += tars
        tars = single
        length = len(tars)
        for num in range(length):
            rename(join(pathToOutputs, tars[num]), join(pathToOutputs, self.inputZipFiles[length - num - 1] + '.tar.gz'))
