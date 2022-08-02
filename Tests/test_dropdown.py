import time

import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from Locators.dropdown_locators import dropdown_select
from pages.dropdown_page import Dropdown
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('set_up')
class TestDropdown(Base):

    def test_select_dropdown(self):
        driver = self.driver

        # initiate checkbox page instance
        dropdown_page = Dropdown(driver)

        # Check page header
        page_header = driver.find_element(By.TAG_NAME, 'h3')
        assert page_header.text == 'Dropdown List'

        # Check the status of the checkbox1
        dropdown = driver.find_element(By.XPATH, dropdown_select)

        # Check the visibility of the dropdown
        dropdown_page.make_sure_that_dropdown_exist()

        # test dropdown
        dd_select = Select(dropdown)
        for option in range(2):
            dd_select.select_by_index(option)
            time.sleep(3)
            dd_select.select_by_visible_text(f'Option {option+1}')
            time.sleep(3)
            dd_select.select_by_value(f'{option+1}')
            time.sleep(3)

