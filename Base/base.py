import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from conftest import website_url


class Base:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(website_url)
        yield self.driver
