from os import listdir
import time
import csv
def make_task(driver, modelrun, uplFolder):
    task_num = 0
    reader = csv.reader(modelrun)
    for line in reader:
        for filename in listdir(uplFolder):
            if line[2] == filename:
                print "SAME"
                task_name = line[2]
                mainInputFile = line[4]
                cores = line[7]
                nodes = line[8]
                print task_name, mainInputFile, cores, nodes
                time.sleep(1)
                try:
                    task_link = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
                except:
                    plus_button = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody/tr/th/a")
                    plus_button.click()
                    task_link = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr[2]/td[2]/a")
                task_link_text = task_link.text
                time.sleep(1)
                if task_link_text == "Tasks (0)":
                    task_link.click()
                    time.sleep(1)
                    tasks = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/span/a")
                    tasks.click()
                else:
                    task_link.click()
                    time.sleep(1)
                    tasks = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/table[2]/tbody/tr/td[2]/span/a")
                    tasks.click()
                time.sleep(1)
                description_label = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[2]/td[2]/input")
                description_label.send_keys(task_name)
                print 'setting parameters'
                print 'select input data'
                time.sleep(0.3)
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[3]/td[2]/span/a").click()
                print 'select all data'
                time.sleep(0.3)
                q = ""
                global x
                x = 0
                global click_num
                click_num = 0
                global select_list
                select_list = []
                while q != "exit":
                    try:
                        time.sleep(0.1)
                        select_label = driver.find_element_by_xpath(("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr["+str(2+x)+"]/td[4]")).text
                        print "Found Number", 1+x
                        x += 1 
                    except:
                        time.sleep(0.1)
                        print "Cannot Find Number", 1+x
                        q = "exit"
                    if select_label == task_name:
                        print "Number:", x+1
                        click_num = x+1
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr["+str(click_num)+"]/td/input").click()
                print 'confirm select data'
                time.sleep(2)
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td/input").click()
                # step()
                print 'choose tool'
                time.sleep(0.8)
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[4]/td[2]/span/a").click()
                # step()
                print 'select neuron'
                time.sleep(2)
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[4]/ul/li[6]/strong/a").click()
                # step()
                print 'choose parameters'
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table/tbody/tr[5]/td[2]/span/a/span").click()
                # step()
                print  'specify run time'
                time.sleep(1)
                hours = 2
                driver.find_element_by_id('neuron73_tg_runtime_').clear()
                driver.find_element_by_id('neuron73_tg_runtime_').send_keys(hours)
                # step()
                print 'enter input file name'
                time.sleep(0.3)
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/div/div/input[2]").clear()
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/div/div/input[2]").send_keys(mainInputFile.strip())
                # step()
                print 'enter number of nodes'
                time.sleep(0.3)
                try:
                    driver.find_element_by_id('neuron73_tg_number_nodes_').clear()
                except:
                    time.sleep(1)
                    driver.find_element_by_xpath('//*[@id="createTask"]/table[1]/tbody/tr[5]/td[2]/span/a').click()
                    driver.find_element_by_id('neuron73_tg_number_nodes_').clear()
                driver.find_element_by_id('neuron73_tg_number_nodes_').send_keys(str(nodes))
                # step()
                print 'enter number of cores'
                time.sleep(0.3)
                driver.find_element_by_id('neuron73_tg_number_cores_').clear()
                driver.find_element_by_id('neuron73_tg_number_cores_').send_keys(str(cores))
                # step()
                print 'click 9'
                time.sleep(0.3)
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/div/form/input").click()
                driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[3]/form/table[2]/tbody/tr/td/input").click()
                print "Made Task: ", task_name
                task_num += 1
    return task_num
