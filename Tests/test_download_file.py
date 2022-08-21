import os
import time

import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from Locators.file_download_locators import file_download_xpath, image_to_download_xpath


@pytest.mark.usefixtures('set_up')
class TestDownloadFile(Base):

    def test_download_file(self):
        driver = self.driver

        element = driver.find_element(By.XPATH, file_download_xpath)
        element.click()

        # Check page header
        page_header = driver.find_element(By.TAG_NAME, 'h3')
        assert page_header.text == 'File Downloader'

        # download image
        image_xpath = driver.find_element(By.XPATH, image_to_download_xpath)
        image_xpath.click()
        time.sleep(2)
        print(self.latest_download_file())

    def latest_download_file(self):
        path = r'C:\Users\lmasri\Downloads'
        os.chdir(path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        newest = files[-1]

        return newest
