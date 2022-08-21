import os
import time

import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from Locators.file_upload_locators import file_upload_xpath, choose_file_id


@pytest.mark.usefixtures('set_up')
class TestUploadFile(Base):

    def test_upload_file(self):
        driver = self.driver

        element = driver.find_element(By.XPATH, file_upload_xpath)
        element.click()

        # Check page header
        page_header = driver.find_element(By.TAG_NAME, 'h3')
        assert page_header.text == 'File Uploader'

        # download image
        choose_file = driver.find_element(By.ID, choose_file_id)
        choose_file.click()
        time.sleep(5)


