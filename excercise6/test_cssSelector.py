import pytest
import logging
from selenium import webdriver


logging.basicConfig(level=logging.INFO)


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
    logging.info("debug level logging")
    logging.debug("info level logging")
    logging.warning("warning level logging")
    logging.error("error level logging")
    logging.critical("critical level logging")



