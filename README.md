## Описание
Данный файл содержит функции для класса BasePage, MainPage, OrderPage
Данный файл содержит тесты для класса TestMainPage, TestOrderPage, TestTransitionsPage

## Функции для класса BasePage
### go_to_url 
Переходит по указанному адресу
### find_element_with_wait
Ожидает и находит видимый элемент
### click_to_element
Выполняет клик по элементу после проверки его кликабельности
### add_text_to_element
Вводит текст в поле
### get_text_from_element
Получает текст из элемента
### format_locators
Форматирует локатор с номером
### scroll_to_element
Прокручивает к нужному элементу
### switch_to_last_window
Переключается на последнее окно 

## Функции для класса MainPage
### click_to_question
Нажимает на вопрос
### get_answer_text
Получает ответ на вопрос
### check_question_and_answer
Проверяет ответ на вопрос

## Функции для класса OrderPage
### set_order_step_1
Заполняет шаг 1 данными
### set_order_step_2
Заполняет шаг 2 данными
### set_order
Заполняет шаг 1 и шаг 2 данными 
### get_text_order_placed
Получает текст после оформления заказа

## Тесты для класса TestMainPage
### test_questions_and_answer
Тест проверяет соответствие фактического ответа ожидаемому для каждого вопроса 
## Тесты для класса TestOrderPage
Тест проверяет оформление через две кнопки заказа, 
а также проверяет всплывающее окно с сообщением об успешном создании заказа.
## Тесты для класса TestTransitionsPage
Тест проверяет переход на главную страницу по логотипу
