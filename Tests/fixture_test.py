import pytest, time, logging
from selenium import webdriver
#logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

@pytest.yield_fixture()
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_python_org(browser):
    browser.get('http://python.org')
    assert 'Welcome to Python.org' in browser.title
    browser.find_element_by_css_selector("#id-search-field").send_keys("pycon")
    browser.find_element_by_name("submit").click()
    browser.find_element_by_css_selector("#content > div > section > form > ul > li:nth-child(1) > h3 > a").click()
    #time.sleep(10)
