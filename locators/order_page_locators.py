from selenium.webdriver.common.by import By
from helpers import random_metro, random_rental_period, random_color_scooter


class OrderPageLocators:

    ORDER_HEADER_STEP_1 = By.XPATH, "//*[text()='Для кого самокат']"

    FIELD_INPUT_NAME = By.XPATH, "//*[@placeholder='* Имя']"
    FIELD_INPUT_SURNAME = By.XPATH, "//*[@placeholder='* Фамилия']"
    FIELD_INPUT_ADDRESS = By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_METRO = By.XPATH, "//*[@placeholder='* Станция метро']"
    FIELD_METRO_DROPDOWN = By.XPATH, "//*[@class='select-search has-focus']"
    FIELD_METRO_DROPDOWN_CLICK = By.XPATH, f"//*[text()='{random_metro()}']"
    FIELD_INPUT_PHONE = By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"

    BUTTON_FURTHER = By.XPATH, "//*[text()='Далее']"

    ORDER_HEADER_STEP_2 = By.XPATH, "//*[text()='Про аренду']"
    FIELD_INPUT_DELIVERY_DATA = By.XPATH, "//*[@placeholder='* Когда привезти самокат']"
    FIELD_RENTAL_PERIOD_DROPDOWN = By.XPATH, "//*[text()='* Срок аренды']"
    CLICK_RANDOM_RENTAL_PERIOD = By.XPATH, f"//*[@class='Dropdown-menu']/*[text()='{random_rental_period()}']"
    CHECKBOX_RANDOM_COLOR_SCOOTER = By.XPATH, f"//*[contains(@class, 'Order_Checkboxes')]/*[text()='{random_color_scooter()}']"
    FIELD_COMMENT_COURIER = By.XPATH, "//*[@placeholder='Комментарий для курьера']"
    BUTTON_ORDER_ON_ORDER_PAGE = By.XPATH, "//*[contains(@class, 'Order_Buttons')]/*[text()='Заказать']"

    MODAL_HEADER_IN_ORDER = By.XPATH, "//*[text()='Хотите оформить заказ?']"
    BUTTON_ORDER_YES = By.XPATH, "//*[text()='Да']"
    TEXT_ORDER_PLACED = By.XPATH, "//*[contains(text(),'Заказ оформлен')]"
