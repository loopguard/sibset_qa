"""
Вход в личный кабинет Юр.лиц по адресу http://cabinet-ul.sibset.ru/login
Проверка входа с корректными данными и выход из личного кабинета
Проба работы с Unittest вместо pytest
Chromedriver
"""

from selenium import webdriver
import unittest, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class login_ul_chrome_test(unittest.TestCase):
    """
    Тесты под управлением драйвера Chrome
    """

    def setUp(self):
        """
        Раскоментить опции для запуска браузера Хром без отрисовки UI в режиме --headless
        """
        #options.binary_location = '/Users/a.efimov/AppData/Local/Google/Chrome SxS/Application/chrome.exe'
        #options.add_argument('headless')

        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get('http://cabinet-ul.sibset.ru/login')


    def test_1_login(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Вводим корректные данные для авторизации
        3.Проверяем что мы в ЛК
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[4]/div/div[1]/div[2]/a[1]')))

    def test_2_logout(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку Выход, жмем
        3.Проверяем что мы вышли из ЛК
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/header/div[2]/a[2]'))) #Выход
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/header/div[2]/a[2]').click()

    def test_3_incorrectinput(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Вводим некорректные данные авторизации
        3.Проверяем наличие 'error' оповещения о неверном вводе данных
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('1234')
        driver.find_element_by_name('password').send_keys('#$^')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))

    def test_4_settings(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку перехода к настройкам, жмем
        3.Проверяем что мы в разделе настроек
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector('#root > div > div > div > header > div.additional_menu > a:nth-child(1)').click()
        wait.until(EC.presence_of_element_located((By.NAME, 'old_password')))

    def test_5_docs(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку перехода к документам, жмем
        3.Проверяем что мы в разделе документы
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/a[2]').click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))

    def test_6_notification(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку перехода к уведомлениям, жмем
        3.Проверяем что мы в разделе настроек уведомлений
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/a[3]/span').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[4]/div/div[1]')))

    def test_7_promise_payment(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Выбираем Обещаный платеж
        3.Проверяем переход на новую вкладку с оплатой
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div/div[1]/div[2]/a[1]').click()
        driver.get('http://insufficient-funds.211.ru/?account=1000000212140')
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'send_promise')))

    def test_8_ul_payment(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Выбираем Способы Оплаты
        3.Проверяем переход на новую вкладку с оплатой для юр лиц
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div/div[1]/div[2]/a[2]').click()
        driver.get('http://nsk.sibset.ru/b2b/abonentam/?account=1000000212140')
        wait.until(EC.presence_of_element_located((By.ID, "account")))


    def tearDown(self):
        self.driver.close()



class login_ul_firefox_test(unittest.TestCase):

    """
    Тесты под управлением драйвера Firefox(Gekodriver)
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://cabinet-ul.sibset.ru/login')


    def test_1_login(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Вводим корректные данные для авторизации
        3.Проверяем что мы в ЛК
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[4]/div/div[1]/div[2]/a[1]')))

    def test_2_logout(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку Выход, жмем
        3.Проверяем что мы вышли из ЛК
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/header/div[2]/a[2]'))) #Выход
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/header/div[2]/a[2]').click()

    def test_3_incorrectinput(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Вводим некорректные данные авторизации
        3.Проверяем наличие 'error' оповещения о неверном вводе данных
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('1234')
        driver.find_element_by_name('password').send_keys('#$^')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))

    def test_4_settings(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку перехода к настройкам, жмем
        3.Проверяем что мы в разделе настроек
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector('#root > div > div > div > header > div.additional_menu > a:nth-child(1)').click()
        wait.until(EC.presence_of_element_located((By.NAME, 'old_password')))

    def test_5_docs(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку перехода к документам, жмем
        3.Проверяем что мы в разделе документы
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/a[2]').click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))

    def test_6_notification(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Находим кнопку перехода к уведомлениям, жмем
        3.Проверяем что мы в разделе настроек уведомлений
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/a[3]/span').click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[4]/div/div[1]')))

    def test_7_promise_payment(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Выбираем Обещаный платеж
        3.Проверяем переход на новую вкладку с оплатой
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div/div[1]/div[2]/a[1]').click()
        driver.get('http://insufficient-funds.211.ru/?account=1000000212140')
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'send_promise')))

    def test_8_ul_payment(self):
        """
        1.Заходим на страницу личного кабинета Юр.лиц
        2.Выбираем Способы Оплаты
        3.Проверяем переход на новую вкладку с оплатой для юр лиц
        """

        driver = self.driver
        driver.find_element_by_name('login').send_keys('212140Tk')
        driver.find_element_by_name('password').send_keys('212140Tk')
        driver.find_element_by_class_name('ss-button').click()
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div/div[1]/div[2]/a[2]').click()
        driver.get('http://nsk.sibset.ru/b2b/abonentam/?account=1000000212140')
        wait.until(EC.presence_of_element_located((By.ID, "account")))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()