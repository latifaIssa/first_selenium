import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from Locators.forgot_password_locators import retrieve_password_button_class_name, email_name, forgot_password_xpath


class ForgotPass:
    def __init__(self, driver):
        self.driver = driver
        element = driver.find_element(By.XPATH, forgot_password_xpath)
        element.click()
        self.wait = WebDriverWait(driver, 3)


    def make_sure_that_email_field_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, email_name)))
        except Exception as e:
            raise print("email does not appears", format(e))

    def make_sure_that_retrieve_password_button_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, retrieve_password_button_class_name)))
        except Exception as e:
            raise print("Retrieve password button does not appears", format(e))

    def fill_email(self, text):
        self.wait.until(EC.element_to_be_clickable((By.NAME, email_name)))
        self.driver.find_element(By.NAME, email_name).send_keys(text)

    def click_retrieve_password_button(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, retrieve_password_button_class_name)))
        time.sleep(1)
        btn_click = self.driver.find_element(By.TAG_NAME, 'button')
        btn_click.click()
        time.sleep(1)

    def fill_information(self, email):
        self.fill_email(email)
        self.click_retrieve_password_button()
        time.sleep(1)

    def clear_email(self):
        self.driver.find_element(By.NAME, email_name).clear()

