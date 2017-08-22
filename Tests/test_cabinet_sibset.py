#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Вход в личный кабинет Физ. лиц через админку
http://cabinet.sibset.ru/admin/auth/login
"""

from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class TestCabinetChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://dev.cabinet.sibset.ru/admin/account')
        self.driver.find_element_by_id(
            'adminuser-login').send_keys('a.efimov')  # login
        self.driver.find_element_by_id(
            'adminuser-password').send_keys('Pewpew15')  # password
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
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        contract = driver.find_element_by_id(
            'adminabonent-contract')
        submit = driver.find_element_by_class_name(
            'admin-contract-button')
        contract.send_keys('353829')
        submit.click()
        time.sleep(10)
        menu = wait.until(
            ec.presence_of_element_located(
                By.XPATH('/html/body/div[1]/div[1]/a[1]')))
        self.assertIn(
            "Личный кабинет", menu)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
