######################
#Вход в личный кабинет юр.лица с вводом корректных данных и выход
######################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome() #расположение chromedriver можно указать прямо 'C:\Tools\chromedriver'
driver.get('http://cabinet-ul.sibset.ru/login')
driver.find_element_by_name('login').send_keys('212140Tk')
driver.find_element_by_name('password').send_keys('212140Tk')
driver.find_element_by_class_name('ss-button').click()


wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/header/div[2]/a[2]'))) #Выход
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/header/div[2]/a[2]').click()
