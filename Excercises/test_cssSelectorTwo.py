import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.vinwij.nl/selenium/factuur.html")
    yield driver
    driver.quit()



def test(browser):
    total_Amount = browser.find_element_by_css_selector("div#tot_amount")
    assert total_Amount.is_displayed()