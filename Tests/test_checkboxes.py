import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from Locators.checkboxes_locators import checkboxes_xpath, checkbox_1_xpath, checkbox_2_xpath
from pages.checkboxes_page import Checkboxes


@pytest.mark.usefixtures('set_up')
class TestCheckboxes(Base):

    def test_check_checkboxes(self):
        driver = self.driver

        # initiate checkbox page instance
        checkbox_page = Checkboxes(driver)

        # Check page header
        page_header = driver.find_element(By.TAG_NAME, 'h3')
        assert page_header.text == 'Checkboxes'

        # Check the status of the checkbox1
        checkbox_1 = driver.find_element(By.XPATH, checkbox_1_xpath)
        checkbox_2 = driver.find_element(By.XPATH, checkbox_2_xpath)

        # Check the visibility of the checkboxes
        checkbox_page.make_sure_that_checkbox_1_exist()
        checkbox_page.make_sure_that_checkbox_2_exist()

        # test checkboxes
        checkbox_page.checkbox_test(checkbox_1)
        checkbox_page.checkbox_test(checkbox_2)
