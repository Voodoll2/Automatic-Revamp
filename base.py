from os import listdir
from os.path import isfile, join, exists
from os import makedirs
from csvModels import csvToDict
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import sys
import csv
import json
from os import listdir, rename, makedirs
from os.path import isfile, join, exists
import datetime
from login import login
from upload import upload
from task import make_task
from run import run_task
from download import download as Download
from view_status import view
from rename import rename_out

class Init():
    def __init__(self, driver, user, passwd, uplFolder, outFolder, modelrun):
        self.driver = driver
        self.user = user
        self.passwd = passwd
        self.uplFolder = uplFolder
        self.outFolder = outFolder
        self.modelrun = modelrun
        self.loginUrl = "http://www.nsgportal.org/portal/login!input.action"
        self.data_num = 0
        self.num_tasks = 0
        self.labels = []

    def login(self):
        login(self.driver, self.loginUrl, self.user, self.passwd)

    def upload(self):
         self.data_num = upload(self.driver, self.uplFolder)

    def make_task(self):
        self.num_tasks = make_task(self.driver, self.modelrun, self.uplFolder)

    def run(self):
        run_task(self.driver)

    def download(self):
        Download()

    def view_status(self):
        self.labels = view(self.driver)
        print self.labels
        rename_out(self.outFolder, self.labels)
def main():
    chromePath = "chromedriver/chromedriver"
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : "/Users/voodoll2/Desktop/Automatic/Outputs/"}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=chromePath, chrome_options=chromeOptions)
##    user = str(raw_input("Username: "))
##    passwd = str(raw_input("Password: "))
    user = "sc-eguetz"
    passwd = "Xcaliber1"
    uplFolder = "/Users/voodoll2/Desktop/Automatic/Models/"
    outFolder = "/Users/voodoll2/Desktop/Automatic/Outputs"
    modelrun = open("/Users/voodoll2/Desktop/Automatic/modelrun.csv", "rU")
    fieldnames = ("Model Name","filename","ID Number","Output filename", "main filename", "program used", "Time taken", "Cores", "nodes", "Link to Model")
    init = Init(driver, user, passwd, uplFolder, outFolder, modelrun)
    command = str(raw_input(">>> "))
    while command != "quit" or command != "exit":
        if command == "" or command == None:
            print "You must enter a command"
        elif command == "login":
            init.login()
        elif command == "upload":
            init.upload()
        elif command == "make":
            init.make_task()
        elif command == "run":
            init.run()
        elif command == "download":
            init.download()
        elif command == "view":
            init.view_status()
        elif command == "all":
            init.download()
            init.login()
            init.upload()
            init.make_task()
            init.run()
            init.view_status()
        else:
            print "Command not recognized. You must enter a proper command."
        command = str(raw_input(">>> "))
    sys.exit()
main()
    





    
    
    
