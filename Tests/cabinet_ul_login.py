import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome() #расположение chromedriver можно указать прямо 'C:\Tools\chromedriver'
driver.get('http://cabinet-ul.sibset.ru/login')
driver.find_element_by_name('login').send_keys('212140Tk')
driver.find_element_by_name('password').send_keys('212140Tk')
driver.find_element_by_class_name('ss-button').click() #кнопка войти



#WebDriverWait(driver, 10).until(EC.title_is("Наименование организации"))


#driver.close()