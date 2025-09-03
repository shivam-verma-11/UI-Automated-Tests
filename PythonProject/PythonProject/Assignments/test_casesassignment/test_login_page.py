import pytest

from selenium import webdriver
#from selenium.webdriver.chrome import webdriver
#from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from assignment.Login_Page import Login_Page


class Test_01_Login_Page():
    login_page_url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    invalid_username = "standard_user1"

    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        act_title = self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_login_page(self):
        self.driver= webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.loginpage_lp = Login_Page(self.driver)
        self.loginpage_lp.enter_username(self.username)
        self.loginpage_lp.enter_password(self.password)
        self.loginpage_lp.click_login()
        act_swag_text = self.driver.find_element(By.XPATH,"//div[@class='app_logo']").text
        if act_swag_text == "Swag Labs":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_invalid_login_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.login_page_url)
        self.loginpage_lp = Login_Page(self.driver)
        self.loginpage_lp.enter_username(self.invalid_username)
        self.loginpage_lp.enter_password(self.password)
        self.loginpage_lp.click_login()
        act_swag_text = self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']/h3/button").text
        if act_swag_text == "Epic sadface: Username and password do not match any user in this service":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

