import time

import pytest

from Base.base import Base
from selenium.webdriver.common.by import By

from Locators.login_locators import LoginLocators
from pages.login_page import Login


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):
    def test_go_to_login(self):
        driver = self.driver
        self.login_screen = driver.find_element(By.XPATH,LoginLocators.login_xpath)
        self.login_screen.click()

        page_header = driver.find_element(By.TAG_NAME, 'h2')
        assert page_header.text == 'Login Page'

    def test_login(self):
        # initiate main page
        login_page = Login(self.driver)

        # check the visibility of the login fields
        login_page.make_sure_that_username_field_exist()
        login_page.make_sure_that_username_field_exist()
        login_page.make_sure_that_login_button_exist()

        # valid_username = tomsmith and valid_pass = SuperSecretPassword!
        username = "tomsmith"
        password = 'SuperSecretPassword!'
        # Fill the form with invalid username and valid password
        login_page.fill_username_login('latifa')
        login_page.fill_password_login(password)
        login_page.click_login_button()
        time.sleep(1)
        # get message error
        message_error = login_page.get_validation_error_message()
        # make sure that the message error correct
        assert message_error == 'Your username is invalid!\n×'

        # Fill the form with valid username and invalid password
        login_page.fill_username_login(username)
        login_page.fill_password_login('aaaa')
        login_page.click_login_button()
        time.sleep(1)
        # get message error
        message_error = login_page.get_validation_error_message()
        # make sure that the message error correct
        assert message_error == 'Your password is invalid!\n×'

        # Fill the form with valid username and valid password
        login_page.fill_username_login(username)
        login_page.fill_password_login(password)
        login_page.click_login_button()
        time.sleep(1)
        # get message
        message = login_page.get_validation_error_message()
        # make sure that the message correct
        assert message == 'You logged into a secure area!\n×'



