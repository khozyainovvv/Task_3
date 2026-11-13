from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")