#Вход в личный кабинет юр.лица с вводом корректных данных


from selenium import webdriver


driver = webdriver.Chrome() #расположение chromedriver можно указать прямо 'C:\Tools\chromedriver'
driver.get('http://cabinet-ul.sibset.ru/login')
driver.find_element_by_name('login').send_keys('212140Tk')
driver.find_element_by_name('password').send_keys('212140Tk')
driver.find_element_by_class_name('ss-button').click()