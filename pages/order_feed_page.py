from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def click_first_order(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER)

    def is_order_modal_visible(self):
        return self.is_element_visible(OrderFeedPageLocators.ORDER_MODAL)

    def get_total_orders_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    def get_today_orders_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))

    def wait_for_feed_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
            )
        )

    def is_feed_not_empty(self) -> bool:
        locator = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
        return self.is_element_visible(locator)

    def is_order_in_feed(self, order_number: str) -> bool:
        locator = (
            By.XPATH,
            f"//p[contains(@class, 'text_type_digits-default') and contains(text(), '{order_number}')]"
        )
        return self.is_element_visible(locator)

    def is_order_in_progress(self, order_number: str) -> bool:
        formatted = f"{int(order_number):06d}"
        locator_progress = (
            By.XPATH,
            f"//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(., '{formatted}')]"
        )
        locator_ready = (
            By.XPATH,
            f"//ul[contains(@class, 'OrderFeed_orderList__cBvyi') and not(contains(@class, 'Ready'))]//li[contains(., '{formatted}')]"
        )
        return self.is_element_visible(locator_progress) or self.is_element_visible(locator_ready)