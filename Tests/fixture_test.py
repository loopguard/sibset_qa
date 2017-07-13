import pytest
from selenium import webdriver


@pytest.yield_fixture()
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_python_org(browser):
    browser.get('http://python.org')
    assert 'Python' in browser.title