import unittest
import HtmlTestRunner
from ddt import ddt, file_data
from selenium import webdriver
import sys
import os

sys.path.append("C://Users//aikra//Documents//Selenium-Python-POM")

from Page_Object.Login_Page import login_page


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/aikra/Documents/Selenium-Python-POM/Drivers/chromedriver.exe")
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()
        cls.login_page = login_page(driver=cls.driver)
        cls.driver.implicitly_wait(time_to_wait=50)

    @file_data(os.path.join("Data", "data_login.json"))
    def test_login(self, username, password):
        self.login_page.login_in_app(username=username, password=password)
        is_login_successful = self.login_page.is_login_successful()

        # Assertions
        assert is_login_successful is True
        print("----- Successfully Login -----")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C://Users//aikra//Documents//Selenium-Python-POM//reports", report_name="Login"))
