import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser, scroll_to_position


def test_add_shopping_cart(browser):
    scroll_to_position(browser, 500)

    good = browser.find_element(by=By.CLASS_NAME, value='product-thumb')

    buttongroup = good.find_element(by=By.CLASS_NAME, value='button-group')

    button_add_to_cart = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(buttongroup.find_element(By.TAG_NAME, 'button'))
    )
    time.sleep(1)
    button_add_to_cart.click()

    scroll_to_position(browser, 0)

    time.sleep(1)
    result = browser.find_element(by=By.CLASS_NAME, value='btn-inverse').text

    IsEqualizeDollar = result == '1 item(s) - $602.00'
    IsEqualizeEuro = result == '1 item(s) - 472.33€'

    assert IsEqualizeEuro or IsEqualizeDollar
