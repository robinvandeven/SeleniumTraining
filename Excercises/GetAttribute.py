import pytest
import logging
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get("http://www.vinwij.nl/selenium/factuur.html")
    driver.get("http://www.vinwij.nl/selenium/form.html")
    yield driver
    driver.quit()

# Avond 3, oefening 1
# def test(driver):
#     totaal = driver.find_element_by_id("tot_amount")
#     print(totaal.get_attribute("outerHTML"))

# Avond 3, oefening 2
def test(driver):
    trekhaak = driver.find_element_by_id("trek")
    isSelected(trekhaak)
    trekhaak.click()
    isSelected(trekhaak)


def isSelected(element):
    print(element.is_selected())