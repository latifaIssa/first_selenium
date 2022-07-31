import pytest
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait

from Base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.main_page import MainPage


@pytest.mark.usefixtures('set_up')
class TestHeaders(Base):
    def test_header(self):
        driver = self.driver

        # initiate main page
        main_page = MainPage(driver)

        # check the visibility of the headers text
        main_page.make_sure_that_page_title1_exist()
        main_page.make_sure_that_page_title2_exist()

        header1 = driver.find_element(By.TAG_NAME, 'h1')

        # check the text color
        header1_color_rgba = header1.value_of_css_property('color')
        header1_color_hex = Color.from_string(header1_color_rgba).hex
        assert header1_color_hex == '#222222'

        

