import time
from selenium.webdriver.common.keys import Keys
def view(driver):
    time.sleep(1)
    task_link = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
    task_link.click()
    q = ""
    button_text = ""
    global x
    x = 0
    global length
    length = 0
    global label_list
    label_list = []
    while q != "exit":
        try:
            time.sleep(1)
            button = driver.find_element_by_xpath(("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table/tbody/tr["+str(2+x)+"]/td[9]/span/a"))
            print "Found Index", 2+x, "Number", x
            button_text = button.text
            label = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table/tbody/tr["+str(2+x)+"]/td[3]/span/a").text
            label = str(label)
            label_list.append(label)
            length += 1
            x += 1     
        except:
            time.sleep(1)
            print "Cannot Find Index", 2+x, "Number", x
            q = "exit"
            break
        
        if(button_text != "View Status"):
            print "Nubmer", x, "is Finished"
            path = "/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table/tbody/tr["+str(1+x)+"]/td[9]/span/a"
            viewOut = driver.find_element_by_xpath(path)
            viewOut.click()
            time.sleep(1)
            download_sel = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/table/tbody/tr[4]/td[6]/span/a")
            download_sel.click()
            print "downloaded"
            task_link = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
            task_link.click()
        else:
            print "Number", x, "is still Running"
        print label_list
    return label_list
