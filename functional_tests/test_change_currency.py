from selenium.webdriver.common.by import By
from conftest import browser, CSS_SELECTORS


def test_change_currency(browser):

    currency_change = browser.find_element(By.CLASS_NAME, 'dropdown-toggle')

    currency_change.click()

    list_of_currencies = browser.find_element(By.CLASS_NAME, 'dropdown-menu.show')

    euro_currency = list_of_currencies.find_element(By.TAG_NAME, 'li').find_element(By.TAG_NAME, 'a')
    euro_currency.click()

    current_currency = browser.find_element(by=By.CSS_SELECTOR, value=CSS_SELECTORS[1])

    assert current_currency.text == '€'
