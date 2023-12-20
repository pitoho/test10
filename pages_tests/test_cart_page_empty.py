from selenium.webdriver.common.by import By
from conftest import browser, CSS_SELECTORS


def test_cart_page_empty(browser):
    open_cart_button = browser.find_element(by=By.CSS_SELECTOR, value=CSS_SELECTORS[0])
    open_cart_button.click()
    browser.implicitly_wait(2)

    content = browser.find_element(by=By.ID, value='content')
    result = content.find_element(by=By.TAG_NAME, value='p').text

    assert result == 'Your shopping cart is empty!'
