import os
import time

import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from Locators.file_upload_locators import file_upload_xpath, choose_file_id, upload_btn_id


@pytest.mark.usefixtures('set_up')
class TestUploadFile(Base):

    def test_upload_file(self):
        driver = self.driver

        element = driver.find_element(By.XPATH, file_upload_xpath)
        element.click()

        # Check page header
        page_header = driver.find_element(By.TAG_NAME, 'h3')
        assert page_header.text == 'File Uploader'

        # Click on upload without choose a file
        upload_btn = driver.find_element(By.ID, upload_btn_id)
        upload_btn.click()
        page_header_error = driver.find_element(By.TAG_NAME, 'h1')
        time.sleep(2)
        assert page_header_error.text == 'Internal Server Error'

        # upload file
        driver.back()
        time.sleep(1)
        choose_file = driver.find_element(By.ID, choose_file_id)
        driver.execute_script("arguments[0].style.display = 'block';", choose_file)
        choose_file.send_keys(r'C:\Users\lmasri\Documents\a.json')
        time.sleep(2)
        upload_btn = driver.find_element(By.ID, upload_btn_id)
        upload_btn.click()

        # check
        page_header_uploaded = driver.find_element(By.TAG_NAME, 'h3')
        file_name = driver.find_element(By.CLASS_NAME, 'text-center').text
        assert page_header_uploaded.text == 'File Uploaded!'
        assert file_name == 'a.json'
        time.sleep(1)


