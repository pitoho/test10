from selenium.webdriver.common.by import By
from conftest import browser


def test_phone_search(browser):

    search_elem = browser.find_element(by=By.NAME, value='search')
    search_elem.send_keys('phone')

    send_button = browser.find_element(by=By.CLASS_NAME, value='btn-light')
    send_button.click()

    content_block = browser.find_element(by=By.ID, value='content')
    search_result = content_block.find_element(by=By.TAG_NAME, value='h1')

    assert search_result.text == 'Search - phone'
