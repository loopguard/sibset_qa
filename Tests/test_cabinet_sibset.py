#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Вход в личный кабинет Физ. лиц через админку
http://cabinet.sibset.ru/admin/auth/login
"""

from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestCabinetChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://dev.cabinet.sibset.ru/admin/account')
        self.driver.find_element_by_id(
            'adminuser-login').send_keys('a.efimov') #login
        self.driver.find_element_by_id(
            'adminuser-password').send_keys('Pewpew15') #password
        self.driver.find_element_by_class_name(
            'admin_submit_button').click()
        return self.driver

    def testLogin(self):
        """
        1.Авторизация в админку личного кабинета
        2.Заходим под тестовым лицевым счетом
        3.Проверяем что мы в личном кабинете
        """
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        contract = driver.find_element_by_id(
            'adminabonent-contract')
        submit = driver.find_element_by_class_name(
            'admin-contract-button')
        contract.send_keys('353829')
        submit.click()
        wait.until(
            EC.visibility_of(
                By.CLASS_NAME(
                    'cabinet_index_page')))
        self.assertIn(
            "Личный кабинет", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
