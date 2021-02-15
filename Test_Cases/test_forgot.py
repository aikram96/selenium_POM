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

    @file_data(os.path.join("Data", "data_forgot.json"))
    def test_forgot(self, username_validation):
        self.login_page.forgot_section()
        self.login_page.reset_password(username_validation=username_validation)

        print("----- Successfully Forgot -----")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C://Users//aikra//Documents//Selenium-Python-POM//reports", report_name="Forgot"))
