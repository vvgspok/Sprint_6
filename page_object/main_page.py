from page_object.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Нажать на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATORS, num)
        self.scroll_to_element(MainPageLocators.SCROLL_TO_LAST_QUESTION)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)
