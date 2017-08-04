#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Вход в личный кабинет Физ. лиц через админку
http://cabinet.sibset.ru/admin/auth/login
"""

from selenium import webdriver
import unittest, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestCabinetChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://dev.cabinet.sibset.ru/admin/account')
        self.driver.find_element_by_id('adminuser-login').send_keys('a.efimov')
        self.driver.find_element_by_id('adminuser-password').send_keys('Pewpew15')
        self.driver.find_element_by_class_name('admin_submit_button').click()
        return self.driver

    def testLogin(self):
        driver = self.driver
        contract = driver.find_element_by_id('adminabonent-contract')
        submit = driver.find_element_by_class_name('admin-contract-button')
        contract.send_keys('353829')
        submit.click()
        driver.implicitly_wait(10)
        self.assertIn("Личный кабинет", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
