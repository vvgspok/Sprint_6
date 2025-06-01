from selenium.webdriver.common.by import By

class GeneralLocators:

    BUTTON_LOGO_YANDEX = By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]"
    BUTTON_LOGO_SCOOTER = By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]"
    BUTTON_ORDER_UP = By.XPATH, "//*[contains(@class, 'Header_Nav')]/child::button[1]"
