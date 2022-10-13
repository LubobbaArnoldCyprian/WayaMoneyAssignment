import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases.conftest import setup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import time


class Test_001_Login:
    baseURL = ReadConfig.get_application_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    post = ReadConfig.get_post()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_cookie()
        self.lp.set_user_email(self.user_email)
        self.lp.set_password(self.password)
        self.lp.click_login()
#postMessage
        self.lp.click_initial()
        self.lp.input_message(self.post)
        self.lp.click_post()
        time.sleep(5)
#logout
        self.lp.click_account()
        self.lp.click_logout()
        self.driver.close()



