#######################
#Вход в личный кабинет Юр.лиц по адресу http://cabinet-ul.sibset.ru/login
#Проверка входа с корректными данными и выход из личного кабинета
#Проба работы с Unittest вместо pytest
#Chromedriver
#######################

from selenium import webdriver
import unittest, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class login_ul_chrome_test(unittest.TestCase): #Chromedriver

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cabinet-ul.sibset.ru/login')


    def test_1_login(self): #авторизация в личный кабинет
        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[4]/div/div[1]/div[2]/a[1]')))


    def test_2_logout(self): #выход из личного кабинета
        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/header/div[2]/a[2]'))) #Выход
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/header/div[2]/a[2]').click()

    def test_3_incorrectinput(self): #ввод некорректных данных при аторизации
        driver = self.driver
        driver.find_element_by_name('login').send_keys('1234')
        driver.find_element_by_name('password').send_keys('#$^')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))


class login_ul_firefox_test(unittest.TestCase): #Firefox

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://cabinet-ul.sibset.ru/login')


    def test_1_login(self): #авторизация в личный кабинет
        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()

    def test_2_logout(self): #выход из личного кабинета
        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/header/div[2]/a[2]'))) #Выход
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/header/div[2]/a[2]').click()

    def test_3_incorrectinput(self): #ввод некорректных данных при аторизации
        driver = self.driver
        driver.find_element_by_name('login').send_keys('1234')
        driver.find_element_by_name('password').send_keys('#$^')
        driver.find_element_by_class_name('ss-button').click()


    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()