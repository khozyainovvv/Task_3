from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        import time
        for _ in range(5):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except Exception:
                time.sleep(1)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        return self.find_element(locator).is_displayed()

    def click_constructor(self):
        self.click(BasePageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click(BasePageLocators.ORDER_FEED_BUTTON)

    def click_personal_account(self):
        self.click(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)
        