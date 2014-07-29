from os import listdir
import time
def upload(driver, uplFolder):
    count = 0
    for filename in listdir(uplFolder):
        if filename[0] != ".":
            """Find the data_link"""
            data_link = None
            try:
                data_link = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr/td[2]/a")
            except:
                plus_button = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[1]/div/table/tbody[1]/tr/th/a")
                plus_button.click()
                data_link = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/table/tbody[2]/tr/td[2]/a")
            data_link_text = data_link.text
            """Click the data link in the sidebar"""
            if data_link_text == "Data (0)":
                data_link.click()
                time.sleep(0.5)
                upload_link = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/span/a')
                upload_link.click()
            else:
                data_link.click()
                time.sleep(0.5)
                upload_link = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/div[3]/form[2]/fieldset[2]/table/tbody/tr/td[2]/span/a')
                upload_link.click()
            time.sleep(1)
            """Give the file to the website to store as data"""
            browse_link = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input')
            """Make the label of the data"""
            filename = filename.strip('"')
            browse_link.send_keys(uplFolder + str(filename))
            text_field = driver.find_element_by_xpath('//*[@id="pasteData_label"]')
            text_field.send_keys(filename)
            #time.sleep(10)
            """Save the data with file and label"""
            save_button = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/form/table/tbody/tr[4]/td/input")
            #time.sleep(10)
            print "Looking..."
            time.sleep(2)
            save_button.click()
            print "Clicked"
            print "File Uploaded: ", filename
            count += 1
    return count
    
    
