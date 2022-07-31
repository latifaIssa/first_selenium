from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def make_sure_that_page_title1_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        except Exception as e:
            raise print("Title text does not appears", format(e))

    def make_sure_that_page_title2_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h2')))
        except Exception as e:
            raise print("Title2 text does not appears", format(e))