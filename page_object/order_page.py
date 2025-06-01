from page_object.base_page import BasePage
import allure
from locators.order_page_locators import OrderPageLocators
from helpers import (random_address, random_name, random_surname, random_phone, generation_random_data,
                     random_comment_for_courier)
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step('Заполняем 1-ый шаг заказа')
    def set_order_step_1(self):
        self.find_element_with_wait(OrderPageLocators.ORDER_HEADER_STEP_1)
        self.add_text_to_element(OrderPageLocators.FIELD_INPUT_NAME, random_name())
        self.add_text_to_element(OrderPageLocators.FIELD_INPUT_SURNAME, random_surname())
        self.add_text_to_element(OrderPageLocators.FIELD_INPUT_ADDRESS, random_address())
        self.click_to_element(OrderPageLocators.FIELD_METRO)
        self.scroll_to_element(OrderPageLocators.FIELD_METRO_DROPDOWN_CLICK)
        self.click_to_element(OrderPageLocators.FIELD_METRO_DROPDOWN_CLICK)
        self.add_text_to_element(OrderPageLocators.FIELD_INPUT_PHONE, random_phone())
        self.click_to_element(OrderPageLocators.BUTTON_FURTHER)

    @allure.step('Заполняем 2-ый шаг заказа')
    def set_order_step_2(self):
        self.find_element_with_wait(OrderPageLocators.ORDER_HEADER_STEP_2)
        self.add_text_to_element(OrderPageLocators.FIELD_INPUT_DELIVERY_DATA, generation_random_data())
        self.add_text_to_element(OrderPageLocators.FIELD_INPUT_DELIVERY_DATA, Keys.ENTER)
        self.click_to_element(OrderPageLocators.FIELD_RENTAL_PERIOD_DROPDOWN)
        self.click_to_element(OrderPageLocators.CLICK_RANDOM_RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.CHECKBOX_RANDOM_COLOR_SCOOTER)
        self.add_text_to_element(OrderPageLocators.FIELD_COMMENT_COURIER, random_comment_for_courier())
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_ON_ORDER_PAGE)
        self.find_element_with_wait(OrderPageLocators.MODAL_HEADER_IN_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_YES)

    @allure.step('Заполняем все шаги заказа')
    def set_order(self):
        self.set_order_step_1()
        self.set_order_step_2()

    @allure.step('Получаем сообщение об успешном оформлении заказа')
    def get_text_order_placed(self):
        self.find_element_with_wait(OrderPageLocators.TEXT_ORDER_PLACED)
        return self.get_text_from_element(OrderPageLocators.TEXT_ORDER_PLACED)
