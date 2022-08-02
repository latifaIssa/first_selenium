import time

import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from Locators.drag_and_drop_locators import box_a_xpath, box_b_xpath, drag_and_drop_xpath, box_a_id, box_b_id
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures('set_up')
class TestDragAndDrop(Base):

    def test_drag_and_drop(self):
        driver = self.driver

        element = driver.find_element(By.XPATH, drag_and_drop_xpath)
        element.click()

        # Check page header
        page_header = driver.find_element(By.TAG_NAME, 'h3')
        assert page_header.text == 'Drag and Drop'

        # get the elements
        box_a = driver.find_element(By.ID, box_a_id)
        box_b = driver.find_element(By.ID, box_b_id)

        # get elements location
        box_a_location = box_a.location
        box_b_location = box_b.location

        action = ActionChains(driver)
        action.drag_and_drop_by_offset(box_b, box_a_location['x'], box_a_location['y']).build().perform()
        time.sleep(2)
        action.drag_and_drop_by_offset(box_a, box_b_location['x'], box_b_location['y']).build().perform()
        time.sleep(2)

