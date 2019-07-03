import time

import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get("http://www.vinwij.nl/selenium/factuur.html")
    driver.get("http://www.vinwij.nl/selenium/form.html")
    yield driver
    driver.quit()


def test(driver):
    wait = WebDriverWait(driver, 3)
    kenteken = wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'kt')))
    kenteken.clear()
    kenteken.send_keys("test")
    time.sleep(5)

