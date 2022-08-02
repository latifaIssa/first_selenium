import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from Locators.checkboxes_locators import checkboxes_xpath, checkbox_1_xpath, checkbox_2_xpath


class Checkboxes:
    def __init__(self, driver):
        self.driver = driver
        element = driver.find_element(By.XPATH, checkboxes_xpath)
        element.click()
        self.wait = WebDriverWait(driver, 3)


    def make_sure_that_checkbox_1_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, checkbox_1_xpath)))
        except Exception as e:
            raise print("checkbox 1 does not appears", format(e))

    def make_sure_that_checkbox_2_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, checkbox_2_xpath)))
        except Exception as e:
            raise print("checkbox 2 does not appears", format(e))


    def checkbox_test(self, checkbox):
        is_selected = checkbox.is_selected()
        checkbox.click()
        is_selected_now = checkbox.is_selected()
        assert is_selected != is_selected_now




