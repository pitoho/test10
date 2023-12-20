import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="default")


@pytest.fixture
def browser(request):
    browser_option = request.config.getoption("--browser")
    options = Options()
    service = Service()

    if browser_option == "chrome":

        driver = webdriver.Chrome(options=options, service=service)
    elif browser_option == "firefox":
        options = FirefoxOptions()
        service = FirefoxService()
        driver = webdriver.Firefox(options=options, service=service)
    else:
        driver = webdriver.Chrome(options=options, service=service)

    driver.get("http://localhost/")
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


# Functions and constants for tests
def scroll_to_position(browser, position):
    browser.execute_script(f"window.scrollTo(0, {position});")


CSS_SELECTORS = ['#top > div > div.nav.float-end > ul > li:nth-child(4) > a', '#form-currency > div > a > strong']
