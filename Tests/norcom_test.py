#import time
# from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Tools\chromedriver')
driver.get('http://beta.norcom.ru/')
driver.find_element_by_link_text("Оплатить").click()
driver.find_element_by_id("account").send_keys("12345")
#time.sleep(30)
driver.find_element_by_id("amount").clear()
driver.find_element_by_id("amount").send_keys("500" + Keys.ENTER)
#driver.find_element_by_id("amount").send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + "500" + Keys.ENTER)
#driver.find_element_by_css_selector("form.form-horizontal").submit()