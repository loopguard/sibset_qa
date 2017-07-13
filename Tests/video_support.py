import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://beta.norcom.ru/')
timeout = 5


driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/ul/li[8]/a').click() #помощь техподдержки


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/h2"))
    )
finally:
    driver.quit()