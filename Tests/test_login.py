import pytest

from Base.base import Base
from selenium.webdriver.common.by import By

from Locators.login_locators import logout_button_xpath, login_xpath, message_error_id
from conftest import password, username
from pages.login_page import Login


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):
    def test_go_to_login(self):
        driver = self.driver
        self.login_screen = driver.find_element(By.XPATH, login_xpath)
        self.login_screen.click()

        page_header = driver.find_element(By.TAG_NAME, 'h2')
        assert page_header.text == 'Login Page'

    def test_login_logout(self):
        # initiate main page
        login_page = Login(self.driver)

        # check the visibility of the login fields
        login_page.make_sure_that_username_field_exist()
        login_page.make_sure_that_username_field_exist()
        login_page.make_sure_that_login_button_exist()

        # valid_username = 'tomsmith' and valid_pass = 'SuperSecretPassword!'
        # Fill the form with invalid username and valid password
        message_error = login_page.fill_information("aaa", password)
        # make sure that the message error correct
        assert message_error == 'Your username is invalid!\n×'

        # Fill the form with valid username and invalid password
        message_error = login_page.fill_information(username, 'aaa')
        # make sure that the message error correct
        assert message_error == 'Your password is invalid!\n×'

        # Fill the form with valid username and valid password
        message = login_page.fill_information(username, password)
        # make sure that the message correct
        assert message == 'You logged into a secure area!\n×'

        # logout
        logout_btn = self.driver.find_element(By.XPATH, logout_button_xpath)
        logout_btn.click()
        message = self.driver.find_element(By.ID, message_error_id)
        assert message.text == 'You logged out of the secure area!\n×'





