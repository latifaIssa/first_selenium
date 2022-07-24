# to install the packages use: "pip install chromedriver-binary" & "pip install webdriver-manager"
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager

# To start testing the web pages using the keys & by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# you can use on of these:
# 1. If you've placed chromedriver on your System Path, you can shortcut by just doing the following:

# browser = webdriver.Chrome()

# 2. If not using a system path
# browser = webdriver.Chrome(executable_path=r"C:\Users\lmasri\Documents\chromedriver_win32 (1)\chromedriver.exe")

# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("http://www.python.org")


def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://www.python.org")

    print(driver.title)
    assert "Python" in driver.title

    # get element by name
    elem = driver.find_element(By.NAME, "q")
    # elem.clear()

    # get element by tag name
    # elem2 = driver.find_element(By.TAG_NAME, 'div')
    # print(f'{elem2.text}')

    # get element by ID
    # click_on_downloads = driver.find_element(By.ID, 'downloads')
    # click_on_downloads.click()

    # Enter keyboard keys using the keys
    # test the search box
    elem = driver.find_element(By.NAME, "q")
    elem.clear()  # clear the search field
    elem.send_keys('list')  # send the search text
    elem.send_keys(Keys.ENTER)
    assert "No results found." not in driver.page_source

    driver.close()
    # driver.quit()

@pytest.mark.skip(reason="only runs on Windows")
def test_ie_session():
    service = IEService(executable_path=IEDriverManager().install())

    driver = webdriver.Ie(service=service)
    driver.get("http://www.python.org")

    # driver.quit()