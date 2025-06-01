import pytest
from selenium import webdriver
from page_object.main_page import MainPage
from page_object.order_page import OrderPage
from selenium.webdriver.firefox.options import Options
from page_object.base_page import BasePage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page


@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    return page


@pytest.fixture
def link_page(driver):
    return BasePage(driver)
