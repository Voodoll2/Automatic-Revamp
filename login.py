from selenium.webdriver.common.keys import Keys

def login(driver, username, password):
    """Open nsg portal login page"""
    driver.get('http://www.nsgportal.org/portal/login!input.action')
    try:
        driver.switch_to_alert().accept()
    except:
        pass
    """Send the username keys to the form and press tab"""
    elem =driver.find_element_by_name("username")
    elem.send_keys(username)
    elem.send_keys(Keys.TAB)
    """Send the password keys to the form and press enter"""
    elem2 =driver.find_element_by_name("currentPassword")
    elem2.send_keys(password)
    elem2.send_keys(Keys.RETURN)