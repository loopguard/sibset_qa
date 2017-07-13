from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1(self):
        driver = self.driver
        driver.get("http://beta.norcom.ru/")
        driver.find_element_by_link_text("Оплатить").click()
        driver.find_element_by_id("account").send_keys("123456")
        driver.find_element_by_id("amount").clear()
        driver.find_element_by_id("amount").send_keys("500")
        driver.find_element_by_css_selector("form.form-horizontal").submit()
        driver.find_element_by_css_selector("body > div.container.content-container > div > div.col-md-9 > div > div > div > div:nth-child(4) > div:nth-child(2) > button").click()
        time.sleep(30)
    # def test_2(self):
    #     driver = self.driver
    #     driver.get("http://beta.norcom.ru/support/")
    #     # Приемная
    #     #driver.maximize_window()
    #     #driver.find_element_by_css_selector("#footer > div > div:nth-child(2) > ul > li:nth-child(3) > a").click()
    #     driver.find_element_by_css_selector("body > div.container.content-container.post-page > div > div > ul > li:nth-child(1) > h5 > a").click()
    #     driver.find_element_by_name("name").send_keys("Maks")
    #     driver.find_element_by_id("email").send_keys("maksimtester@yandex.ru")
    #     driver.find_element_by_id("phone1").send_keys("951")
    #     driver.find_element_by_id("phone2").send_keys("3636926")
    #     driver.find_element_by_id("contact").send_keys("Вавилова, 7")
    #     driver.find_element_by_name("text").send_keys("Тестирование")
    #     driver.find_element_by_css_selector("#ij_submit").click()
    #     time.sleep(30)
    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    #
    #
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e: return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
