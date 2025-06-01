import allure
import pytest
from data import URL
from locators.general_page_locators import GeneralLocators
from locators.yandex_page_locators import YandexPageLocators
from locators.main_page_locators import MainPageLocators


class TestTransitionsPage:
    @pytest.mark.parametrize(
        'locator, element',
        [
            (GeneralLocators.BUTTON_LOGO_SCOOTER, MainPageLocators.HOME_MAIN_PAGE),
            (GeneralLocators.BUTTON_LOGO_YANDEX, YandexPageLocators.FIELD_SEARCH_YANDEX)
        ]
    )
    @allure.title('Тест перехода по логотипу')
    @allure.description('Проверяем, что нажатие на логотип корректно перенаправляет на главную страницу')
    def test_go_by_logo(self, link_page, locator, element):
        link_page.go_to_url(URL)
        link_page.click_to_element(locator)
        link_page.switch_to_last_window()
        assert link_page.find_element_with_wait(element) != []
