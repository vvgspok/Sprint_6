import pytest
from data import answers, URL
import allure


class TestMainPage:

    @pytest.mark.parametrize(
        'num',
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ]
    )
    @allure.title('Тест соответствия фактического ответа ожидаемому')
    @allure.description('Получаем ответ на вопрос и сравниваем с ожидаемым значением')
    def test_questions_and_answer(self, main_page, num):
        main_page.go_to_url(URL)
        assert main_page.check_question_and_answer(num) == answers[num]
