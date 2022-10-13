from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(20)
        print("Launching Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
