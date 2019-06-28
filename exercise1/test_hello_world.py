import pytest
from selenium import webdriver


# def test_hello_world():
    # driver = webdriver.Chrome()
    # driver.get("http://www.vinwij.nl/selenium/factuur.html")
    # header = driver.find_element_by_tag_name("h3")
    # assert header.text == "Factuur 14325g6", "Header is not equal to expected value"

    # driver.maximize_window()
    # driver.get("http://www.vinwij.nl/selenium/form.html")
    # # trekhaak =  driver.find_element_by_xpath("//input[@id='trek']")
    # trekhaak = driver.find_element_by_xpath("//input[contains(text(),\"Trekhaak\")]")
    # assert trekhaak.is_displayed()
    #
    # driver.quit()
from exercise1.test_cssSelectorTwo import test


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.vinwij.nl/selenium/factuur.html")
    yield driver
    driver.quit()

# def test_excercise4(browser):
#     checkBoxElement = browser.find_element_by_xpath("//input[@id='trek']")
#     checkBoxElement.click()

def test_excercise5(browser):
    total_Amount = browser.find_element_by_css_selector("div#tot_amount")
    assert total_Amount.is_displayed()









