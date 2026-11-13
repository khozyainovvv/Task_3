from selenium.webdriver.common.by import By

class BasePageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")