from selenium.webdriver.common.by import By
from conftest import browser


def test_wishlist_page(browser):

    open_wishlist_button = browser.find_element(by=By.ID, value='wishlist-total')
    open_wishlist_button.click()

    assert browser.current_url == 'http://localhost/en-gb?route=account/wishlist'
