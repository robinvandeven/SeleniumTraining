from selenium import webdriver

def test_hello_world():
    browser = webdriver.Chrome()
    browser.get("http://www.vinwij.nl/selenium/factuur.html")
    header = browser.find_element_by_tag_name("h3")
    assert header.text == "Factuur 143256"
    browser.quit()