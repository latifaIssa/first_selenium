import time

import pytest

from Base.base import Base
from selenium.webdriver.common.by import By
from Locators.drag_and_drop_locators import drag_and_drop_xpath, box_a_id, box_b_id
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

        action = ActionChains(driver)
        action.click_and_hold(box_a).move_to_element(box_b).release().perform()
        time.sleep(2)
        action.click_and_hold(box_b).move_to_element(box_a).release().perform()
        time.sleep(2)
