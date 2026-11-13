from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    def click_order_history(self):
        self.click(AccountPageLocators.ORDER_HISTORY_LINK)

    def click_logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)

    def wait_for_order_in_history(self, order_number: str):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_number}')]")
            )
        )

    def is_order_in_history(self, order_number: str) -> bool:
        locator = (
            By.XPATH,
            f"//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_number}')]"
        )
        return self.is_element_visible(locator)