import time
def run_task(driver):
        time.sleep(1)
        task_link = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
        task_link.click()
        startTimes = []
        q = ""
        global x
        x = 0
        global length
        length = 0
        global select_list
        select_list = []
        while q != "exit":
                try:
                        time.sleep(1)
                        select = driver.find_element_by_xpath(("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table/tbody/tr["+str(2+x)+"]/td/input"))
                        print "Found Number", 1+x
                        length += 1
                        x += 1     
                except:
                        time.sleep(1)
                        print "Cannot Find Number", 1+x
                        q = "exit"
                        break
                path = "/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table/tbody/tr["+str(1+x)+"]/td[9]/span/a"
                runButton = driver.find_element_by_xpath(path)
                runButton.click()
                try:
                        driver.switch_to_alert().accept()
                except:
                        pass
