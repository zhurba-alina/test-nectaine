from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://corporate-nectain.eastus.cloudapp.azure.com")
assert "Nectain" in driver.title
title_xpath = driver.find_element_by_class_name('login_title').text
title_css = driver.find_element_by_css_selector('.login_title').text
assert "Nectain" in title_xpath
assert "Nectain" in title_css

input_login = driver.find_element_by_id('login')
input_login.send_keys("admin")
input_password = driver.find_element_by_id('password')
input_password.send_keys("admin")

button_submit = driver.find_element_by_id('loginSubmitAuth')
button_submit.click()
# driver.close()