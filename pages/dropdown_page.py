from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Locators.dropdown_locators import dropdown_xpath, dropdown_select


class Dropdown:
    def __init__(self, driver):
        self.driver = driver
        element = driver.find_element(By.XPATH, dropdown_xpath)
        element.click()
        self.wait = WebDriverWait(driver, 3)

    def make_sure_that_dropdown_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, dropdown_select)))
        except Exception as e:
            raise print("dropdown does not appears", format(e))

