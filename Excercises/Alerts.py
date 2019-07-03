import time

import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.select import Select

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get("http://www.vinwij.nl/selenium/factuur.html")
    driver.get("http://www.vinwij.nl/selenium/form.html")
    yield driver
    driver.quit()


def test(driver):
    submit_button = driver.find_element_by_xpath("//*[text()='Submit']")
     # submit_button = driver.find_element_by_xpath("//*[@onclick ='myFunction()']")
    submit_button.click()
    alert = driver.switch_to.alert
    alert_message = alert.text
    assert alert_message == "Error processing request!"
    time.sleep(5)
    # alert.accept()
    alert.dismiss()