from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATORS = By.XPATH, "//*[@id= 'accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, "//*[@id= 'accordion__panel-{}']"
    SCROLL_TO_LAST_QUESTION = By.XPATH, "//*[@id= 'accordion__heading-7']"
    HOME_MAIN_PAGE = By.XPATH, "//*[contains(@class, 'Home_HomePage')]"
    BUTTON_ORDER_DOWN = By.XPATH, "//*[contains(@class, 'Home_FinishButton')]/descendant::button"
