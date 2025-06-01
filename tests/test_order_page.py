import allure
import pytest
from data import URL, text_order_placed
from locators.main_page_locators import MainPageLocators
from locators.general_page_locators import GeneralLocators


class TestOrderPage:

    @pytest.mark.parametrize(
        'locator',
        [
            GeneralLocators.BUTTON_ORDER_UP,
            MainPageLocators.BUTTON_ORDER_DOWN
        ]
    )
    @allure.title('Тест добавления заказа через верхнюю и нижнюю кнопку')
    @allure.description('Тестирование оформления заказа при нажатии на обе кнопки "Заказать"')
    def test_orders(self, order_page, locator):
        order_page.go_to_url(URL)
        order_page.scroll_to_element(locator)
        order_page.click_to_element(locator)
        order_page.set_order()
        assert text_order_placed in order_page.get_text_order_placed()
