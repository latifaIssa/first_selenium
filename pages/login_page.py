import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Locators.login_locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver
        element = driver.find_element(By.XPATH, login_xpath)
        element.click()
        self.wait = WebDriverWait(driver, 3)

    def __str__(self):
        return self.message

    def make_sure_that_username_field_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, username_name)))
        except Exception as e:
            raise print("Username does not appears", format(e))

    def make_sure_that_Password_field_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, password_name)))
        except Exception as e:
            raise print("Password does not appears", format(e))

    def make_sure_that_login_button_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, login_button_class_name)))
        except Exception as e:
            raise print("login button does not appears", format(e))

    def fill_username_login(self, text):
        self.wait.until(EC.element_to_be_clickable((By.NAME, username_name)))
        self.driver.find_element(By.NAME, username_name).send_keys(text)

    def fill_password_login(self, text):
        self.wait.until(EC.element_to_be_clickable((By.NAME, password_name)))
        self.driver.find_element(By.NAME, password_name).send_keys(text)

    def click_login_button(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, login_button_class_name)))
        time.sleep(1)
        btn_click = self.driver.find_element(By.TAG_NAME, 'button')
        btn_click.click()
        time.sleep(1)

    def get_validation_error_message(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, message_error_id)))
        return self.driver.find_element(By.ID, message_error_id).text

    def fill_information(self, username, password):
        self.fill_username_login(username)
        self.fill_password_login(password)
        self.click_login_button()
        time.sleep(1)
        # get message
        message = self.get_validation_error_message()
        # make sure that the message correct
        return message
