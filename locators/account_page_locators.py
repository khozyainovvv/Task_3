from selenium.webdriver.common.by import By

class AccountPageLocators:

    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button')]")