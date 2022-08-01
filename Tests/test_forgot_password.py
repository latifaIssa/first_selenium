import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from pages.Forgot_password_page import ForgotPass


@pytest.mark.usefixtures('set_up')
class TestForgotPassword(Base):

    def test_forgot_password(self):
        driver = self.driver
        # initiate main page
        forgot_pass_page = ForgotPass(driver)

        # Check page header
        page_header = driver.find_element(By.TAG_NAME, 'h2')
        assert page_header.text == 'Forgot Password'

        # Check the visibility of the forgot password form elements
        forgot_pass_page.make_sure_that_email_field_exist()
        forgot_pass_page.make_sure_that_retrieve_password_button_exist()

        # Always receive server error when perform this action
        # Fill the form with invalid email
        forgot_pass_page.fill_information('latifa.masri')

        # return to previous page
        driver.back()

        # Clear email field
        forgot_pass_page.clear_email()

        # Fill the form with valid email
        forgot_pass_page.fill_information('lmasri@asaltech.com')




